#!/usr/bin/env python3
"""
--- TASK 6 ---
function creating a model with dropout regularization
"""

from tensorflow import keras


def build_model_with_dropout(
        input_dim,
        hidden_units,
        n_layers,
        dropout_rate_input,
        dropout_rate_hidden
        ):
    """
    model with dropout regularization
    - input layer followed by a droupout layer
    - multiple hidden layers
        - dense layer
        - Relu activation
        - followed by a dropout layer
    - output layer with softmax


    args:
    - input_dim: (int) # features
    - hidden_units: (int) # neurons in hidden layer
    - n_layers: (int) # number of hidden layers
    - droput_rate_input: (float) input layer
    - droput_rate_hidden: (float) ouptut layer

    return:
    model
    """

    # Step 1: Connect the layers using the Functional API
    inputs = keras.layers.Input(shape=(input_dim,))
    x = keras.layers.Dropout(dropout_rate_input)(inputs)

    # Step 2: Loop hidden layers

    for units in range(0, n_layers):
        x = keras.layers.Dense(
            units=hidden_units,
            activation="relu"
            )(x)
        x = keras.layers.Dropout(dropout_rate_hidden)(x)

    # Step 3 Hidden layer
    outputs = keras.layers.Dense(units=10, activation="softmax")(x)

    # Step 4: Bundle into a Model object
    model = keras.Model(inputs=inputs, outputs=outputs)

    return model
