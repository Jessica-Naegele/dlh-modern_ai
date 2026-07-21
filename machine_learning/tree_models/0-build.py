#!/usr/bin/env python3
"""
--- TASK 0
function creating a decision tree classifier
"""

from sklearn import tree


def build_decision_tree(min_samples_leaf, min_samples_split, random_state):
    """
    function creating a decision tree classifier
    - uses gini impurity measure
    no maximum depth is set

    args
    - min_samples_leaf
    min_samples_split
    random_sate: seed sed by random number generator

    result:
    - model: decisiontreeclassifier
    """

    model = tree.DecisionTreeClassifier(
        criterion='gini',
        min_samples_split=min_samples_split,
        min_samples_leaf=min_samples_leaf,
        random_state=random_state
        )
    
    return model
