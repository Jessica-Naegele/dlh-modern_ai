#!/usr/bin/env python3
"""
--- TASK 7 ---
function with customizable early stopping callback
"""

from tensorflow import keras


def get_early_stopping_callback(patience, monitor='val_loss', verbose=1):
    """
    customizable early stopping callback
    - monitor a specific metric during training
    - stop training if no improvement is seen after a defined number of epochs
    - restore best model weights once training stop


    args:
    - patience: (int) # epochs to wait wihtout improv
    - monitor: (str) metric to monitor (val_loss, val_accuracy)
    - verbose: (int) verbosity mode to display messages

    returns:
    - configured early Stopping callback
    """

    cb = keras.callbacks.EarlyStopping(
        monitor=monitor,
        patience=patience,
        verbose=verbose
        )

    return cb
