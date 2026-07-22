#!/usr/bin/env python3
"""
--- TASK 7 ---
Train a model of multiple decisions tree classifier
"""

from sklearn import tree
train_tree = __import__('1-train').train_tree


def prune_and_evaluate_trees(
        X_train, y_train, X_test, y_test, ccp_alphas, random_state,
         min_samples_leaf, min_samples_split
         ):
    """
    function training several decision tree classifiersover cost-complexity pruning

    args:
    - X_train, y_train: Training data and labels
    -X_test, y_test: Testing data and labels
    -ccp_alphas: nparray of pruning alpha values 
    -random_state: Integer seed for reproducibility.
    -min_samples_leaf: (int)
    -min_samples_split: (int)

    returns
    - clfs: A list of trained DecisionTreeClassifier instances,
    each corresponding to a ccp_alpha value.
    - train_scores: A list of training accuracy scores
    - test_scores: A list of testing accuracy scores
    """

    train_score = []
    test_score = []
    cfl_l = []
    
    

    for i in ccp_alphas:
        cfl = tree.DecisionTreeClassifier(
            criterion='gini',
            min_samples_split=min_samples_split,
            min_samples_leaf=min_samples_leaf,
            random_state=random_state,
            ccp_alpha=i)

        cfl_train = train_tree(cfl, X_train, y_train)
        cfl_l.append(cfl_train)
        train_score.append(cfl_train.score(X_train, y_train))
        test_score.append(cfl_train.score(X_test, y_test))

    return cfl_l, train_score, test_score


