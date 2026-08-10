#!/usr/bin/env python3
"""
--- TASK 0 ---
function creating a descent optimizer with appropriate batch size
"""

from tensorflow import keras


def train_with_gradient_descent_variant(
        variant,
        learning_rate,
        x_train,
        batch_size
        ):
    """
    configured gradient descnet optimizer with appropriate batch size
    based on graident descnet variant

    args:
    - variant: (str)
        - batch: perform updates based on entire dataset
        - stoachstic: SGD
        - mini-batch
    - learning_rate: (float)
    - x_train: training data (input data)
    - batch_size: (int: to use when mini-batch)

    return:
    - optimizer
    - bs: correct batch size based on selected variant
    """
    # optimizer
    optimizer = keras.optimizers.SGD(
        learning_rate=learning_rate
    )

    # for batch size (short: bs)
    if variant == "batch":
        # all data at once
        bs = x_train.shape[0]
    elif variant == "stochastic":
        # one single dataset after another
        bs = 1
    elif variant == "mini_batch":
        # mix between batch and stochastic. Mini-batches with
        # specifed batch sizes
        bs = batch_size

    return optimizer, bs
