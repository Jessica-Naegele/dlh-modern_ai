#!/usr/bin/env python3
"""
--- TASK 4 ---
function returning a model with weight initializer and softmax output layer
"""

from tensorflow import keras


def build_model_initializer_by_activation(input_dim, hidden_units, activation):
    """
    model with one hidden layer with appropriate weight initializer
    and softmax output layer

    args:
    - input_dim: (int) # input features
    - hidden_units: (int) # neurons in hidden layer
    - activation: (string)
        - sigmoid or tanh - Glorot Uniform (initalizer)
        - relu and leaky_relu - He Normal (initializer)

    returns:
    - model
    """
    if activation in ["sigmoid", "tanh"]:
        initializer = keras.initializers.GlorotUniform()
    elif activation in ["relu", "leaky_relu"]:
        initializer = keras.initializers.HeNormal()

    # Pass layers as a list into keras.Sequential()
    model = keras.Sequential(
        [
            keras.layers.InputLayer(input_shape=(input_dim,)),
            keras.layers.Dense(
                units=hidden_units,
                activation=activation,
                kernel_initializer=initializer,
            ),
            keras.layers.Dense(units=10, activation="softmax"),
        ]
    )

    model.compile(
        optimizer="adam",
        loss="categorical_crossentropy",
        metrics=["accuracy"],
    )

    return model
