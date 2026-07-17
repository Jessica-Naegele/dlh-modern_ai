#!/usr/bin/env python3
"""
--- TASK 0 ---
function standardizing tabular data using Scikit learn
all feature contribute proportionaly
"""

from sklearn import preprocessing


def Standardize(X):
    """
    args:
    - X (numpy.ndarray) - shape: (n_samples, n_features)
     --> test for negative cases

     return:
     - numpy.ndarray = standardized version of input data
     - same shape as X
    """
    scaler = preprocessing.StandardScaler()
    standardized_data = scaler.fit_transform(X)

    return standardized_data
