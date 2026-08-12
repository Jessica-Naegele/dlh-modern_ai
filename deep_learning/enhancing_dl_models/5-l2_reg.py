#!/usr/bin/env python3
"""
--- TASK 5 ---
function creating a model with L2 regularization
"""

from tensorflow import keras


def build_model_with_L2_regularization(input_dim, hidden_units, n_layers, lambda_l2):
    """
    - multiple hidden layers (defined by n)
        - dense layer
        - relu activation
        - l2 regularization
    - output layer: softmax activation

    - args:
        - input_dim: # input feautres (int)
        - hidden_units: # neurons in hid layers (int)
        - n_layers: # hidden layers (int)
        - lambda_l2: l2 weight

    - returns:
        -model
    """

    # Step 1: Connect the layers using the Functional API
    inputs = keras.layers.Input(shape=(input_dim,))
    x = inputs
        
    # Step 2: Loop hidden layers
        
    for units in range (0, n_layers):
        x = keras.layers.Dense(
        units = hidden_units,
        activation = "relu",
        kernel_regularizer=keras.regularizers.l2(lambda_l2)
        )(x)
        
    # Step 3 Hidden layer
    outputs = keras.layers.Dense(units=10, activation="softmax")(x)

    # Step 4: Bundle into a Model object
    model = keras.Model(inputs=inputs, outputs=outputs)

    return model
