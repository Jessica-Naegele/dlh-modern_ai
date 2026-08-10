#!/usr/bin/env python3
"""
functions returning an optimizer
"""

from tensorflow import keras


def get_optimizer(name, learning_rate, momentum, beta_1, beta_2, rho):
    """
    returning an optimizer

    args:
    - name: (str)
        - 'sgd': Stochastic Gradient Descent, with optional momentum
        - 'adam': adaptive Moment Estimation
        - 'rmsprop': Root Mean Square Propagation
    - learning_rate: (float)
    - momentum: (float) - only for SGD
    only ADAM:
    - beta_1: (float) exponential decay rate for first moment estimate
    - beta_2: (float) exponential decay rate for second moment estimate
    only RMSprop:
    - rho: (float) decay factor

    returns:
    - optimizer
    """

    if name == "sgd":
        if momentum is None:
            momentum = 0.0
        optimizer = keras.optimizers.SGD(
            learning_rate=learning_rate,
            momentum=momentum
        )
    elif name == "adam":
        optimizer = keras.optimizers.Adam(
            learning_rate=learning_rate,
            beta_1=beta_1,
            beta_2=beta_2
        )
    elif name == "rmsprop":
        optimizer = keras.optimizers.RMSprop(
            learning_rate=learning_rate,
            rho=rho
        )

    return optimizer
