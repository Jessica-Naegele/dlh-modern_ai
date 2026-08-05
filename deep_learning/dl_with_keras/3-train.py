#!/usr/bin/env python3
"""
--- TASK 3 ---
function training a model
"""

from tensorflow import keras


def train_model(model, X, Y, epochs, verbose=1):
    """
    training a model

    args:
    - model
    - X : Input data, shape (# of examples, input features)
    - Y: labels, shape (# of examples, 1)
    - epochs: # of training epochs
    - verbose: verbosity mode (0=silent, 1 = progress bar)

    returns: 
    - None
    """

    model.fit(
        X,
        Y,
        epochs=epochs,
        verbose=verbose
    )

    return None