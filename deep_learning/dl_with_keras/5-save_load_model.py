#!/usr/bin/env python3
"""
-- Task 5 --
2 functions:
- save model
- load model
"""


def save_model(model, filepath):
    """
    function to save a model (architecture, weights and optimizer)

    args:
    - model: trained model
    - filepath: string including file path & file name

    return:
    - NONE
    """

    model.save(filepath)

    return None


def load_model(filepath):
    """
    function loading a model

    args:
    - filepath

    return: model
    """

    model = keras.models.load_model(filepath)

    return model
