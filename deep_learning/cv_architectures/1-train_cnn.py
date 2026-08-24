#!/usr/bin/env python3
"""
--- TASK 1 ---
function training a CNN model. Herefore it compiles and trains it
with the following parameters: model, epochs, batch_size,
optimizer_name, optimizer_params
"""

from tensorflow import keras


def compile_and_train_cnn(
    model,
    epochs,
    batch_size,
    x_train,
    y_train,
    x_val,
    y_val,
    optimizer_name='adam',
    optimizer_params=None
):
    """
    function to train and compile a CNN model.

    args:
    - model: CNN model to be trained
    - epochs: int, number of trainings
    - batch_size: int, size of batches for training
    - optimizer_name str, default = adam
    - optimizer_params: dict, additional params

    returns:
    - trained CNN model, raining history object
    """
    # print(optimizer_params)
    # print(bool(optimizer_params))

    if not bool(optimizer_params):
        model.compile(
            optimizer=optimizer_name,
            loss='categorical_crossentropy',
            metrics=['accuracy']
            )
    else:
        optimizer_config = {
            'class_name': optimizer_name,
            'config': optimizer_params
        }
        optimizer_instance = keras.optimizers.get(optimizer_config)
        model.compile(
            optimizer=optimizer_instance,
            loss='categorical_crossentropy',
            metrics=['accuracy']
        )

    history = model.fit(
        x=x_train,
        y=y_train,
        batch_size=batch_size,
        epochs=epochs,
        validation_data=(x_val, y_val),
        verbose=2
    )

    return model, history
