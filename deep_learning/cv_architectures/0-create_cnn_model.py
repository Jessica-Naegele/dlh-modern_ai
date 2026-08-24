#!/usr/bin/env python3
"""
--- TASK 0 ---
function creating a convolutional neural network (also called CNN) model.
Arguments: input_shape, filters, kernel_sizes, activations, pooling_type
"""

from tensorflow import keras


def create_cnn_model(
    input_shape,
    filters,
    kernel_sizes,
    activations,
    pooling_type='max'
):
    """
    creating a convolutional neural network model

    args:
    - input_shape (tuple): shape of input data
    - filters (list): # filters in each convolutional layer
    - kernel_sizes (list): size of kernels for each convolutional layer
    - activations (list): activation function for each convolutional layer
    - pooling_type (str): typoe fo pooling ('max' (default), or 'avg')

    return:
    - compiled CNN model
    """

    # set up sequential neural network with initial layer
    model = keras.Sequential([
        keras.layers.Input(shape=input_shape)
    ])

    # hidden Convolutional layers
    for i in range(0, len(filters)):
        model.add(keras.layers.Conv2D(
            filters=filters[i],
            kernel_size=kernel_sizes[i],
            activation=activations[i]
        ))
        if pooling_type == 'max':
            model.add(keras.layers.MaxPooling2D((2, 2)))
        else:
            model.add(keras.layers.AveragePooling2D(2, 2))

    # flatten to make it dense
    model.add(keras.layers.Flatten())
    model.add(keras.layers.Dense(units=10, activation='softmax'))

    # compiling
    model.compile(
        optimizer='adam',
        loss='sparse_categorical_crossentropy',
        metrics=['accuracy']
    )

    return model
