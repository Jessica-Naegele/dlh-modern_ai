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

    # Step 1: Pick the right Initializer and Activation object
    if activation in ["sigmoid", "tanh"]:
        initializer = keras.initializers.GlorotUniform()
        act_func = activation
    elif activation == "relu":
        initializer = keras.initializers.HeNormal()
        act_func = activation
    elif activation == "leaky_relu":
        initializer = keras.initializers.HeNormal()
        act_func = keras.layers.LeakyReLU()

    # Step 2: Connect the layers using the Functional API
    inputs = keras.Input(shape=(input_dim,))
    hidden = keras.layers.Dense(
        units=hidden_units,
        activation=act_func,
        kernel_initializer=initializer,
    )(inputs)
    outputs = keras.layers.Dense(units=10, activation="softmax")(hidden)

    # Step 3: Bundle into a Model object
    model = keras.Model(inputs=inputs, outputs=outputs)

    # Step 4: Compile the model
    model.compile(
        optimizer="adam",
        loss="categorical_crossentropy",
        metrics=["accuracy"],
    )

    return model
