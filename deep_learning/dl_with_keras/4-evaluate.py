#!/usr/bin/env python3
"""
--- TASK 4 ---
function assesing a trained model performance given dta
"""


def evaluate_model(model, X, Y, verbose=0):
    """
    evaluate performance of a model:

    args:
    - model: trained model
    - X: input data with shape (# of examples, input features)
    - Y: labels corresponding to input data with sahpe (# examples)
    - verbose: verbosity (0 = silent, 1 = progress bar)
    
    returns:
    - loss: calculated loss on provided data
    - accuracy: accurcy of model
    """

    results = model.evaluate(X, Y, verbose=verbose)

    return results
