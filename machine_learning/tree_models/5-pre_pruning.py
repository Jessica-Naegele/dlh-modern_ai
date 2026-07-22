#!/usr/bin/env python3
"""
--- TASK 5 ---
function performin a grid Search for best pre-pruning parameters
"""

from sklearn import model_selection


def prepruning(X, y, clf):
    """
    creating Grid Search for best pre-pruning hyperparameters for
    a decision tree classifier

    search explorse:
    - criterion: gini or entropy
    - max_depth: int [2,  5)
    - min_samples_leaf: int [2,  5)
    - min_samples_split: int [2,  5)

    args:
    - X: input features
    - y: Target labels
    - clf: untrained DecisionTreeClassifier

    result:
    - dict: containing best combi

    """
    parameters = {
        "criterion": ("gini", "entropy"),
        "max_depth": range(2, 5),
        "min_samples_leaf": range(2, 5),
        "min_samples_split": range(2, 5)
    }
    grid = model_selection.GridSearchCV(
        estimator=clf, param_grid=parameters, refit=True
        )

    grid.fit(X, y)

    return grid.best_params_
