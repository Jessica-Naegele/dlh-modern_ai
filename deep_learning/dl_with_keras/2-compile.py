#!/usr/bin/env python3
"""
--- TASK 2 ---
creating a model fr training
"""

from tensorflow import keras


def compile_model(model, learning_rate=0.01):
    """
    model for training having:
    - Optimizer: stochastic gradient descent
    - Loss function: binary cross-entropy
    - Classification performance: accuracy

    args:
    - model
    - learning_rate: for gradient descent

    return: None
    """
    model.compile(
        optimizer=keras.optimizers.SGD(learning_rate=learning_rate),
        loss='binary_crossentropy',
        metrics=['accuracy']
    )

    return None
