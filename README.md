# _moai_: Accelerating modern data-driven workflows

**moai** is an AI Model Development Kit (MDK) that aims at improving data-driven models' workflows, design and understanding.
It is currently based on [PyTorch](https://pytorch.org/) and is in early development _alpha_ version.
Nonetheless, since it is based on other [open-source established packages](#Dependencies), it can be readily used to improve most AI workflows, simply [install](#Installation) the package and follow the [examples](https://github.com/ai-in-motion/moai/tree/master/conf/examples).  

# Features & Design Goals

- **Modularity via Monads**: Use _moai_'s existing pool of modular _model building blocks_.
- **Reproducibility via Configuration**: _moai_ manages the hyper-parameter sensitive AI R&D workflows via its built-in _configuration-based design_.
- **Productivity via Minimizing Coding**: _moai_ offers a _data-driven domain modelling language_ (DML) that can facilitates quick & easy model design.
- **Extensibility via Plugins**: Easily integrate external code using _moai_'s built-in metaprogramming and _external code integration_. 
- **Understanding via Analysis**: _moai_ supports _inter-model performance and design aggregation_ [**actions**](#) to consolidate knowledge between models and query differences.

# Dependencies

_moai_ stands on the shoulders of giants as it relies on various large scale open-source projects:

1. [PyTorch](https://pytorch.org/) `> 1.7.0`, which needs to be customly installed on your system/environment.
2. [Lightning](https://www.pytorchlightning.ai/) `> 1.0.0`, which is the currently supported training backend.
3. [Hydra](https://hydra.cc/) `> 1.0`, which drives _moai_'s DML that sets up model configurations, and additionally manages the hyper-parameter complexity of modern AI models.
4. [Visdom](https://github.com/fossasia/visdom), which is the currently supported visualization engine.
5. [HiPlot](https://github.com/facebookresearch/hiplot), which drives _moai_'s inter-model analytics.
6. [Various PyTorch Open Source Projects](#Dependencies):
    
    - [Kornia](https://github.com/kornia/kornia) for a set of computer vision operations integrated as _moai_ monads.
    - [Albumentations](https://github.com/albumentations-team/albumentations) as the currently supported data augmentation framework.

7. [The Wider Open Source Community](www.github.com) that conducts accessible R&D and drives most of _moai_'s capabilities.

8. [A set of awesome Python libraries](#Dependencies) as found in our [**requirements**](https://github.com/ai-in-motion/moai/tree/master/requirements.txt) file.

# Installation

## Package
To install the currently **released** _moai_ version package run:

`pip install moai-mdk`

## Source
Download the master branch source and install it by opening a command line on the source directory and running:

`pip install .` or `pip install -e .` (in editable form)

# Getting Started

Visit the [**documentation**](#) site to learn about _moai_'s DML and the overall MDK design and usage.

Examples can be found at [**conf/examples**](https://github.com/ai-in-motion/moai/tree/master/conf/examples).

# Licence

_moai_ is Apache 2.0 licenced, as found in the corresponding [LICENCE](https://github.com/ai-in-motion/moai/blob/main/LICENSE) file.

However, some code integrated from external projects may carry their own licences.

# Citation
```
@misc{moai,
    author = {The AI-in-Motion Team},
    title = {{moai, accelerating modern data-driven workflows}},
    year = {2021},
    publisher = {GitHub},
    journal = {GitHub repository},
    howpublished = {\url{https://github.com/ai-in-motion/moai}},
}
```

# Contact

Either use the:

- [GitHub issue tracker](https://github.com/ai-in-motion/moai/issues), or,
- send an email to [moai `at` ai-in-motion `dot` dev](mailto:moai@ai-in-motion.dev)
