#!/usr/bin/env python3
"""
--- TASK 4 ---
creating a classification report
"""

from sklearn import metrics


def evaluate(true_labels, predicted_labels, class_names):
    """
    function generating a detailed classification

    args:
    - true_labels: ground truth labels
    - predicted_labels
    - class_names: list of class names corresponding to label indices

    return:
    - sring
    - precision
    - recall
    - f1-score
    """

    report = metrics.classification_report(
        y_true=true_labels, y_pred=predicted_labels,
        target_names=class_names
        )

    return report
