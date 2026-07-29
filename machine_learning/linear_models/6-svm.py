#!/usr/bin/env python3
"""
--- TASK 6 ---
Support Vector Machine classifier with specified kernel
"""

from sklearn import svm


def get_SVM_model(name, random_state):
    """
    Support Vector Machine (SVM) classifier

    - name: string indicating type of model
        - linear
        - poly
        - rbf
    - random_state int

    return:
    - untrained SVC
    """

    if name == 'linear':
        svc = svm.SVC(kernel='linear', random_state=random_state)
    elif name == 'poly':
        svc = svm.SVC(kernel='poly', random_state=random_state)
    elif name == 'rbf':
        svc = svm.SVC(kernel='rbf', random_state=random_state)
    else:
        raise ValueError('name not allowed')

    return svc
