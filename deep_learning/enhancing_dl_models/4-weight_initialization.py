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
    # initial layer
    model = keras.Sequential()
    model.add(keras.layers.Input(shape=(input_dim,)))

    # hidden layers
    if activation == "sigmoid" or activation == "tanh":
        model.add(keras.layers.Dense(units=hidden_units, kernel_initializer=keras.initializers.GlorotUniform(), activation=activation))
    elif activation == "relu" or activation == "leaky_relu":
        model.add(keras.layers.Dense(units=hidden_units, kernel_initializer=keras.initializers.HeNormal(), activation=activation))

    # output layer
    model.add(keras.layers.Dense(units=10, activation="softmax"))

    return model