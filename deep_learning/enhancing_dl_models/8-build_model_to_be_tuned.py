#!/usr/bin/env python3
"""
--- TASK 8 ---
multi-class classification with a model tuned via Keras tuner
"""

from tensorflow import keras
from keras_tuner import HyperParameters


def build_model(hp):
    """
    model for multi-class classification wih parameter tuning

    tunable aspects:
    - input layer (input vector of shape (784,))
    - hidden layers (and config should be tunable)
        - num_layers: # int (between 1-2)
        - units: # int (number of neurons in hidden layer)
        - activation: (str) relu or sigmoid
    - output layer
        - dense output layer with 10 units
        - softmax
    - Optimizer and Learning Rate
        - adam
        - learning_rate: (float) (1e-2 or 1e-3)

    args:
    - an isntance of hyperparameters provided

    returns:
    - compiled keras sequential model based on hp defined in hp object
    """
    # input layer
    model = keras.Sequential()
    model.add(keras.layers.Input(shape=(784,)))

    # hidden layer
    'how to define 1-2 num_layers'
    for i in range(hp.Int('num_layers', min_value=1, max_value=2)):
        model.add(keras.layers.Dense(
            units=hp.Int('units', min_value=4, max_value=12, step=4),
            activation=hp.Choice('activation', values=['relu', 'sigmoid'])
        ))

    # output layer
    model.add(keras.layers.Dense(10, activation='softmax'))

    # compiler and optimizer

    model.compile(
        optimizer=keras.optimizers.Adam(
            hp.Choice('learning_rate', values=[1e-2, 1e-3])
        )
    )

    return model
