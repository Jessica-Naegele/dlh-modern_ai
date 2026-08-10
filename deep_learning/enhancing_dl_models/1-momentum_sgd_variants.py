#!/usr/bin/env python3
"""
functions returning a SGD optimizer
"""

from tensorflow import keras


def get_optimizer_SGD(name, lr, momentum=0.0, nesterov=False):
    """
    SGD-based optimizer based on specific args

    args:
    - name: (str) optimizer variant
        - 'SGD', 'SGD+Momentum', or 'SGD+Momentum+Nesterov'
        - SGD: Standard stochastic gradient descent
        - SGD+Momentum: SGD with classical momentum
        - SGD+Momentum+Nesterov: SGD with momentum and Nesterov acceleration
    - lr: (float): learning rate
    - momentum: (float) momentum factor
    - nesterov: (boolean)

    returns:
    - optimizer
    """
    if name == "SGD":
        momentum = 0.0
        nesterov = False
    elif name == "SGD+Momentum":
        nesterov = False
    
    optimizer = keras.optimizers.SGD(
        learning_rate=learning_rate,
        momentum=momentum,
        nesterov=nesterov
    )

    return optimizer
