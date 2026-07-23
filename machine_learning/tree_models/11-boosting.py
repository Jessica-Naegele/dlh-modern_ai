#!/usr/bin/env python3
"""
--- TASK 11 ---
function returning an untrained boosting classifier
"""

from sklearn import ensemble
import xgboost as xgb
import lightgbm as lgb


def compare_boosting_classifiers(name, n_estimators, random_state):
    """
    initiatlize and returns untrained boosting classifier
    - initialize with specified n_estimators and random_state
    - for LightGBM: verbose is -1 (no training logs)
    - raise ValueError: if model name is invalid

    args:
    - name: str
        - 'adaboost'  - adaBoostClassifier
        - 'gradientboosting' - GradienBoostingClassifier
        - xgboost - returns XGBClassifier
        - lightgbm - LGBMClassifier
    - random state int
    - n_estimators int

    return: untrained instance
    """

    classifier = ['adaboost', 'gradientboosting', 'xgboost', 'lightgbm']

    if name not in classifier:
        raise ValueError(f"Unknown model name '{name}'")

    if name == 'adaboost':
        boost = ensemble.AdaBoostClassifier(
            n_estimators=n_estimators, random_state=random_state
            )
    if name == 'gradientboosting':
        boost = ensemble.GradientBoostingClassifier(
            n_estimators=n_estimators, random_state=random_state
            )
    if name == 'xgboost':
        boost = xgb.XGBClassifier(
            n_estimators=n_estimators, random_state=random_state
            )
    if name == 'lightgbm':
        boost = lgb.LGBMClassifier(
            n_estimators=n_estimators, random_state=random_state,
            verbose=-1
            )

    return boost
