#!/usr/bin/env python3
"""
--- TASK 8 --- Build a Model to be Tuned
This module defines the build_model function to construct and compile a Keras
Sequential model for multi-class classification using hyperparameter search
spaces provided by Keras Tuner.
"""

from tensorflow import keras


def build_model(hp):
    """
    Builds and compiles a Keras Sequential model for multi-class
    classification.

    Args:
        hp (HyperParameters): An instance of HyperParameters
        provided by Keras Tuner to define the search space.

    Returns:
        keras.Model: A compiled Keras Sequential model.
    """
    model = keras.Sequential()
    model.add(keras.layers.InputLayer(input_shape=(784,)))

    # Tunable hidden layers
    for i in range(hp.Int('num_layers', min_value=1, max_value=2)):
        model.add(keras.layers.Dense(
            units=hp.Int('units', min_value=4, max_value=12, step=4),
            activation=hp.Choice('activation', values=['relu', 'sigmoid'])
        ))

    # Output layer
    model.add(keras.layers.Dense(10, activation='softmax'))

    # Compile model
    model.compile(
        optimizer=keras.optimizers.Adam(
            learning_rate=hp.Choice('learning_rate', values=[1e-2, 1e-3])
        ),
        loss='categorical_crossentropy',
        metrics=['accuracy']
    )

    return model
