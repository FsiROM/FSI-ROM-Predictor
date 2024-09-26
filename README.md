# Designing Machine Learning-Enhanced Predictors for Transient Fluid-Structure Interactions

![GraphicalAbstract](./figs/GraphicalAbstract.png "Graphical Abstract")

This repository contains a presentation of the approach presented in [1] of ML-based predictors for Fluid-Structure Interaction (FSI) simulations.

The repository also contains files corresponding to the two example cases in the paper. This include configuration files for running the simulations, data files used in training the Reduced Order Models (ROMs), and notebooks and files showing the API to train and use the models and replicate the papers' results.

## Theory

See an introduction of the approach in [introduction.md](./fsi-rom-predictor/introduction.md).
We also refer to [1] and [2].

## Software

You can clone this repository using
```
git clone --depth 1 --branch CPC https://github.com/FsiROM/FSI-ROM-Predictor.git
```

The implementation of this approach is done using [KratosMultiphysics](https://github.com/KratosMultiphysics/Kratos) and the [ROM_AM](https://github.com/azzeddinetiba/ROM_AM) package. The Kratos applications used are:

&nbsp;&nbsp;&nbsp;&nbsp;* [StructuralMechanicsApplication](https://github.com/KratosMultiphysics/Kratos/tree/master/applications/StructuralMechanicsApplication) as the FEM solid solver.

&nbsp;&nbsp;&nbsp;&nbsp;* [FluidDynamicsApplication](https://github.com/KratosMultiphysics/Kratos/tree/master/applications/FluidDynamicsApplication) as the FEM fluid solver.

&nbsp;&nbsp;&nbsp;&nbsp;* [CoSimulationApplication](https://github.com/KratosMultiphysics/Kratos/tree/master/applications/CoSimulationApplication) as the black-box coupling library.

The ROM-FOM coupling approach and the new data-driven predictors are implemented in [a forked version](https://github.com/FsiROM/Kratos) from the v9.4.2 release. The implementation mainly concerns the ROM wrapper for the coupling, as well as the new predictor, both acting non-intrusively on the solvers.

The ROM methods used are implemented in the [ROM_AM](https://github.com/azzeddinetiba/ROM_AM) package. See [this demo](https://github.com/azzeddinetiba/ROM_AM/blob/main/examples/ReductionDemo.ipynb) for example.


The simulations have been tested with:

&nbsp;&nbsp;&nbsp;&nbsp;* MacOs 12.6 (arm64), Apple Clang 13.0.0 and Python 3.11 .

&nbsp;&nbsp;&nbsp;&nbsp;* Ubuntu 20.04 (X64), gcc 9.4.0 and Python 3.8 .


## Requirements
&nbsp;&nbsp;&nbsp;&nbsp;* Compiling the FsiROM version of Kratos from source (See [here](https://github.com/FsiROM/Kratos/blob/master/INSTALL.md)).

&nbsp;&nbsp;&nbsp;&nbsp;* Installing the ROM_AM package using pip (See [here](https://github.com/azzeddinetiba/ROM_AM/blob/main/README.md)).

## References

[1] [Azzeddine Tiba, Thibault Dairay, Florian De Vuyst, Iraj Mortazavi, Juan-Pedro Berro Ramirez (2024). Machine-Learning Enhanced Predictors for Accelerated Convergence of Partitioned Fluid-Structure Interaction Simulations. arXiv preprint arXiv:2405.09941](https://doi.org/10.48550/arXiv.2405.09941)

[2] [Azzeddine Tiba, Thibault Dairay, Florian De Vuyst, Iraj Mortazavi, Juan-Pedro Berro Ramirez, Non-intrusive reduced order models for partitioned fluid–structure interactions, Journal of Fluids and Structures, Volume 128, 2024, 104156, ISSN 0889-9746.](https://doi.org/10.1016/j.jfluidstructs.2024.104156)
