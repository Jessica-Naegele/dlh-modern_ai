#!/usr/bin/env python3
"""
--- TASK 0 ---
function creating a neural network with single hidden layer
"""

from tensorflow import keras


def build_model(input_dim, neurons_h):
    """
    creating a neural network with single hidden layer
    performing mulit-class classification using sequential class

    - Sigmoid: activation function for hidden layer
    - Softmax: activation function for the output layer

    args:
    - input_dim: # of input features
    - neurons_h: # of neurons for hidden layer

    returns:
    model: keras model
    """
    model = keras.Sequential([
        keras.layers.Input(shape=(input_dim,)),  # input
        keras.layers.Dense(units=neurons_h, activation='sigmoid'),
        # hidden layer
        keras.layers.Dense(10, activation='softmax')  # output layer
    ])

    return model
