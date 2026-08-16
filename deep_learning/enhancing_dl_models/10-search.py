#!/usr/bin/env python3
"""
--- TASK 10 ---
Function performing hyperparameter tuning and retrieving the best
hyperaparmeters. It returns the hyperparameter configuraiton
that led to the best model, as an object. args: tuner, training
(target) data, epochs, validation_split and verbose
"""

import keras_tuner


def search_and_return_best_model(
        tuner,
        x_train,
        y_train,
        epochs,
        validation_split,
        verbose=0
        ):
    """
    function returning best hyperparameter configuration

    args:
    - tuner:
        - Hyperband,
        - RandomSearch,
        - BayesianOptimization
    - x_train (ndarray): input data
    - y_train (ndarray): target output data
    - epochs (int): # training epochs
    - validation_split (float): fraction of training data to use
    - verbose

    returns:
    - best_hyperparameters
    """

    search = tuner.search(
        x_train,
        y_train,
        epochs=epochs,
        validation_split=validation_split,
        verbose=verbose
        )

    best = tuner.get_best_hyperparameters(num_trials=1)[0]

    return best
