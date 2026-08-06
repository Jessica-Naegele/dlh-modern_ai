#!/usr/bin/env python3
"""
--- TASK 7 ---
function making predictions based on a model
"""

import tensorflow as tf


def predict(model, X, verbose=0):
    """
    prediction model

    args:
    - model: trained
    - X: input data with shape (# examples, features)
    - verbose: 
       0 - silent
       1 - progres bar
       2 - one line per batch

    returns:
    - predictions: list of class labels and input data
    """

    prediction = model.predict(X, verbose)

    return prediction
