#!/usr/bin/env python3
"""
--- TASK 6 ---
function retriving cost-complexity runing path
"""


def get_pruning_path(clf, X, y):
    """
    retrieves cost-complexity pruning path for decion tree classifier

    args:
    - clf: DecisionTreeClassifier instance
    - X: Input featuers
    - y: Target labels

    returns:
    - ccp_alphas: ndarray containing effective alpha values
    - impurities: ndarray containing total impurity of leaves
    """

    path = clf.cost_complexity_pruning_path(X, y)

    return path.ccp_alphas, path.impurities