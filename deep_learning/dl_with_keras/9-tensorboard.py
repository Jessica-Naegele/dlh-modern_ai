#!/usr/bin/env python3
"""
--- TASK 9 ---
function to log model's training metrics to TensorBoard
"""

from tensorflow import keras
import datetime


def log_to_tensorboard(log_dir, model, X, Y, epochs, verbose=1):
    """
    log of training metrics to TensorBoard
    configure a callback that:
    - logs training metrics (loss, accuracy etc) after each epoch
    - logs weight histograms and activation histogram 
        (histogram_freq = 1) to help visualize weights evolve
    - Saves logs with unique timepstamp in format YYYYMMDD-HHMMSS

    args:
    - log_dir: Base directoy
    - model
    - X: Input data, shpae (# examples, input featuers)
    - Y: labesl, shape(# of examples)
    - epochs: # epochs
    - verbose: verbosity model 0 - silent, 1 - progress bar
    
    return: None
    """

    log_name = datetime.datetime.now().strftime("%Y%m%d-%H%M%S")
    log_dir = log_dir + "/" + log_name
    cb = keras.callbacks.TensorBoard(
        log_dir=log_dir,
        histogram_freq=1
        update_freq='epoch'
    )

    model.fit(X, Y, epochs=epochs, verbose=verbose, callbacks=cb)

    return None
