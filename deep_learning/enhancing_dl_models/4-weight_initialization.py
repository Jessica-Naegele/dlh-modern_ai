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
    # 1. Select the weight initializer
    if activation in ["sigmoid", "tanh"]:
        initializer = keras.initializers.GlorotUniform()
    elif activation in ["relu", "leaky_relu"]:
        initializer = keras.initializers.HeNormal()

    # 2. Build using Functional API (guarantees len(model.layers) == 3)
    inputs = keras.Input(shape=(input_dim,))
    hidden = keras.layers.Dense(
        units=hidden_units,
        activation=activation,
        kernel_initializer=initializer,
    )(inputs)
    outputs = keras.layers.Dense(units=10, activation="softmax")(hidden)

    model = keras.Model(inputs=inputs, outputs=outputs)

    model.compile(
        optimizer="adam",
        loss="categorical_crossentropy",
        metrics=["accuracy"],
    )

    return model
