#!/usr/bin/env python3
"""
--- TASK 2 ---
function displaying textual structure of a trained decision tree
"""

from sklearn import tree


def draw(clf, feature_names, class_names):
    """
    displaying the textual structure of a decision tree

    args:
    - clf: trained Decision Tree Classifier
    - feature_names: list of input feature names
    - class_names: list of target class names
    """

    r = tree.export_text(clf, feature_names=feature_names, class_names=class_names)
    print(r)

    return None
