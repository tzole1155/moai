from moai.utils.arguments import (
    ensure_numeric_list,
    ensure_string_list,
)

import torch
import hydra.utils as hyu
import omegaconf.omegaconf
import inspect
import typing
import itertools
import toolz
import logging

log = logging.getLogger(__name__)

__all__ = ["Weighted"]

class Weighted(torch.nn.ModuleDict):
    def __init__(self,
        losses: omegaconf.DictConfig,
        **kwargs: typing.Mapping[str, typing.Any]
    ):
        super(Weighted, self).__init__()
        self.execs, self.weights, self.reductions = [], [], []
        if not len(losses):
            log.warning("A weighted combination of losses is being used for supervising the model, but no losses have been assigned.")
        loop = ((key, params) for key, params in kwargs.items() if key in losses)
        self.keyz = []
        for k, p in loop:
            self.add_module(k, hyu.instantiate(getattr(losses, k)))
            last_module = toolz.last(self.modules()) # moduledict is ordered
            sig = inspect.signature(last_module.forward)
            p = toolz.valmap(ensure_string_list, p)
            if 'out' not in p:
                length = len(ensure_string_list(next(iter(p.values()))))
                p['out'] = [k] if length == 1 else [f'{k}_{i}' for i in range(length)]
            if 'weight' in p:
                wgts = iter(ensure_numeric_list(p['weight']))
            else:
                log.warning(f"{k} loss has no assigned weights, automatically reverting to a weight of one (1.0).")
                wgts = itertools.cycle([1.0 / len(p['out'])])
            reduction = p['reduction'] if 'reduction' in p else 'mean'
            #TODO: there is a bug if you pass in keys that are not bracketed ([]), i.e. as a list, even for a single arg
            for keys in zip(*list(p[prop] for prop in itertools.chain(sig.parameters, ['out']) if p.get(prop) is not None)):
                self.execs.append(lambda tensor_dict, k=keys, p=sig.parameters.keys(), f=last_module:
                    tensor_dict.update({
                        k[-1]: f(**dict(zip(p, 
                            list(tensor_dict[i] for i in k[:-1])
                        )))
                    })
                )
                self.keyz.append(keys[-1])
                self.weights.append(next(wgts)) #TODO: error if no weight has been set? or implicit 1.0 ?
                self.reductions.append(reduction)
            
    def forward(self,
        tensors: typing.Dict[str, torch.Tensor]
    ) -> torch.Tensor:
        device = next(toolz.take(1, 
            filter(lambda t: isinstance(t, torch.Tensor), tensors.values())
        )).device
        error = torch.tensor(0.0, dtype=torch.float32, device=device)
        per_error_map = { }
        for exe, w, k, r in zip(self.execs, self.weights, self.keyz, self.reductions):
            exe(tensors)
            e = w * (torch.sum(tensors[k]) if r == 'sum' else torch.mean(tensors[k]))
            per_error_map[k] = e
            error += e
        return error, per_error_map