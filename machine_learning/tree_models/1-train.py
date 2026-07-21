#!/usr/bin/env python3
"""
--- TASK 1 ---
train a tree-based classifier
"""


def train_tree(clf, X, y):
    """
    function training a tree-based classifier

    args:
    - clf: scikit-learn classifier instance
    - X: input features
    y: Target labels
    """

    return clf.fit(X, y)
