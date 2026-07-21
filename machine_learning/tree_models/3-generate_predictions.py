#!/usr/bin/env python3
"""
--- TASK 3 ---
function to generate productiosn from a trained tree
"""

def generate_predictions(clf, X):
    """
    generates preductions from a trained tree-based classifier

    args:
    - clf: trained classifier instance
    - X: feature matrix (ndarray or df)
    """

    prediction = clf.predict(X)

    return prediction