#!/usr/bin/env python3
"""
--- TASK 5 ---
logistic regression model
"""

from sklearn import linear_model


def Logistic_Regression_Model(random_state):
    """
    logistic regression model performing binary classifciation
    
    args:
    - random_state

    returns:
    - model
    """

    model =  linear_model.LogisticRegression(random_state=random_state)

    return model
