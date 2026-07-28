#!/usr/bin/env python3
"""
--- TASK 3 ---
function creating a Lasso Regression model
"""

from sklearn import linear_model


def lasso_regression(random_state):
    """
    Lasso Regression extens ordinary linar regression by adding
    L1 regularization, helping to simplify the model by forcing
    some coefficients to zero, enabling automatic feature selection

    args:
    - randomg state: int

    return:
    - model
    """

    model = linear_model.Lasso(random_state=random_state)

    return model
