#!/usr/bin/env python3
"""
--- TASK 4 ---
function ghelping a model explanations
"""

import shap


def get_shap_explainer_and_values(model, X_train, X_test):
    """
    generates model explanations
    
    args:
    - model: trained reg. model
    - X_Train
    - X_test

    returns
    - explainer: SHAP explainer object
    - shap_values
    """

    explainer = shap.Explainer(model, X_train)
    shap_values = explainer(X_test)

    return explainer, shap_values
