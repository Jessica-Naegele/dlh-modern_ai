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
    model = keras.Sequential()

    # 1. Input configuration
    model.add(keras.layers.InputLayer(input_shape=(input_dim,)))

    # 2. Select initializers safely
    act_str = str(activation).lower().replace("-", "_")

    if "sigmoid" in act_str or "tanh" in act_str:
        initializer = keras.initializers.GlorotUniform()
    else:
        # Default to HeNormal for relu, leaky_relu, or any other activation
        initializer = keras.initializers.HeNormal()

    # 3. Add Hidden Layer
    model.add(
        keras.layers.Dense(
            units=hidden_units,
            activation=activation,
            kernel_initializer=initializer,
        )
    )

    # 4. Add Output Layer
    model.add(keras.layers.Dense(units=10, activation="softmax"))

    return model
