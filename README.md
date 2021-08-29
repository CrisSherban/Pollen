# Pollen

## Table of Contents

* [About the Project](#about-the-project)
* [Prerequisites](#prerequisites)
* [Installation](#installation)
* [Usage](#usage)
* [Results](#results)
* [Authors](#authors)
* [Acknowledgments](#acknowledgments)

## About The Project
```Pollen``` is a project that aims at finding and understanding how pollen
concentration is affected by weather. The main idea stands in the usage of Bayesian Networks
that effectively explain out the relationships in the model.




## Prerequisites

To get a local copy up and running follow these simple steps.

The project provides a ```Pipfile``` file that can be managed with [pipenv](https://github.com/pypa/pipenv).  
```pipenv``` installation is **strongly encouraged** in order to avoid dependency/reproducibility problems.

* pipenv

```sh
pip install pipenv
```

## Installation

1. Clone the repo

```sh
git clone https://github.com/CrisSherban/Pollen
```

2. Enter in the project directory and install Python dependencies

```sh
cd Pollen
pipenv install
```

## Usage

Here's a brief description of the .py files:

* ```kernel.py```: Class that represents a kernel, thus provides a kernel function
* ```svm.py```: SVM class, provides fit() and predict() methods.
* ```main.py```: Verifies that the SVM class works, loads the dataset and shows the result with various kernels.
* ```test_svm.py```: Contains a simple unit test on the SVM class by fitting and predicting over the MNIST dataset.
* ```tools.dataset_tools.py```: Provides the loading, preprocessing, and splitting of the personal EEG dataset.
* ```tools.validation_tools.py```: Provides functions to predict using several SVMs, and cross validate.

To run the ```main.py``` script just run from the project directory:

```sh
python main.py
```

Along fitting several SVMs and show results, it will also show how a sample of the dataset looks like after bandpass and
standardization.

<p align='center'>
  <img src="pictures/eeg_sample.png" />
</p>

## Results

As we can appreciate, the RBF kernel in this situation with default parameters is the one that performs best:
<p align='center'>
  <img src="pictures/kernel_comparison.png" />
</p>

## Authors

* [**Serban Cristian Tudosie**](https://github.com/CrisSherban)

## Acknowledgments

CDMO-2 © Course held by Professor [Vittorio Maniezzo](https://scholar.google.com/citations?user=pSalOJAAAAAJ&hl=en)
