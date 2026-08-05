#!/usr/bin/env python3
"""
--- TASK 6 ---
two functions:
- save model weights
- load model weights
"""

from tensorflow import keras


def save_model_weights(model, filepath):
    """
    save only model weights
    
    args:
    - model: trained model
    - filepath: string

    return:
    - None
    """

    model.save_weights(filepath)

    return None 


def load_model_weights(model, filepath):
    """
    model: compatibile model in which weights be loaded
    filepath: string

    returns: none
    """

    model.load_weights(filepath)

    return None