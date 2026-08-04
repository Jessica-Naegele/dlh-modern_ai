#!/usr/bin/env python3
"""
--- TASK 1 ---
function creating neural network with single hidden layer,
without using Sqeuential class
"""

from tensorflow import keras


def build_model(input_dim, neurons_h):
    """
    neural network performing multi-class classification,
    wihtout using sequential class
    - sigmoid: activation for hidden layer
    - softmas: activation function for output layer
    args:
    - input_dim: # input features
    - neurons_h: # neurons in hidden layer

    return: 
    - model
    """
    input = keras.Input(shape = (input_dim,))
    h = keras.layers.Dense(neurons_h, activation='sigmoid')(input)
    output = keras.layers.Dense(10, activation="softmax")(h)
    model = keras.Model(inputs=input, outputs=output)

    return model
    