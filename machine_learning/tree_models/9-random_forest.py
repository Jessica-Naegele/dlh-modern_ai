#!/usr/bin/env python3
"""
--- TASK 9 ---
function creating a random forest classifier
"""

from sklearn import ensemble


def random_forest(n_estimators, random_state):
    """
    random forest classifier

    args:
    - n_estimators: # of trees in forest
    - random_state

    return: model    
    """

    rf = ensemble.RandomForestClassifier(n_estimators=n_estimators, random_state=random_state)

    return rf
