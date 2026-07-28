#!/usr/bin/env python3
"""
--- TASK 2 ---
function creating Ridge Regression model
"""

from sklearn import linear_model


def ridge_regression(random_state):
    """
    Ridge Regresion - extends ordinary linear regression
    L2 regularization, which helps stabilize the model
    by shrinking large coefficients

    args:
    - random stage: int - random seed for reproducibility

    return:
    - model: untrained Ridge
    """

    model = linear_model.Ridge(random_state=random_state)

    return model
