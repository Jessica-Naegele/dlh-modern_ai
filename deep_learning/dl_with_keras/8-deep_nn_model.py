#!/usr/bin/env python3
"""
--- TASK 8 ---
function creating a deep nn for mulit-class classification
"""

from tensorflow import keras


def build_deep_model(input_dim, hidden_layers):
    """
    function creating deep nn for multi-class classification
    - sequential class
    - hidden layer: ReLu activation

    args:
    - input_dim: # input features
    - hidden_layers: list of ints representing # of neurons for
      each hidden layer
    
    returns:
    - model    
    """

    model = keras.Sequential()

    # Input Layer
    model.add(keras.layers.Dense(shape=(input_dim,)))

    # hidden layers
    for unit in hidden_layers:
        model.add(keras.layers.Dense(units=unit, activation="relu"))

    # output layer
    model.add(keras.layers.Dense(10, activation='softmax'))

    return model
