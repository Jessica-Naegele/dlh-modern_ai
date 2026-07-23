#!/usr/bin/env python3
"""
--- TASK 10 ---
funtion computing feature importance from random forest
"""

import numpy as np


def feature_importance(rf):
    """
    computing feature importance

    args:
    - rf: trained randomforest

    return:
    - importance: nparray - feature importance scores
    - indices: nparray - feature indices sorted from least to important
    """

    importance = rf.feature_importances_
    indices = np.argsort(importance)

    return importance, indices
