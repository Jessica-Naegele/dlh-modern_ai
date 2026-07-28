#!/usr/bin/env python3
"""
--- TASK 1 ---
function computing common evaluation metrics for regression
"""

from sklearn import metrics
import numpy as np


def evaluation_metrics_for_regression(y_true, y_pred):
    """
    evaluating regression tasks

    args:
    - y_true: np array: true target values
    - y_pred: np - containing predited values

    result:
    - tuple (mse, rmse, mae, r2)
    - mse: Mean Squared Error
    - rmse: Root Mean squared Error
    - mae: Mean absolute Error
    - r2: r2-score
    """

    mse = metrics.mean_squared_error(y_true, y_pred)
    rmse = mse ** 0.5
    r2 = metrics.r2_score(y_true, y_pred)
    mae = metrics.mean_absolute_error(y_true, y_pred)

    return (mse, rmse, mae, r2)
