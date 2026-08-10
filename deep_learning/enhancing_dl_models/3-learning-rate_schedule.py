#!/usr/bin/env python3
"""
--- TASK 3 ---
function returning a Keras SGD optimizer
"""

from tensorflow import keras


def get_optimizer_SGD_with_schedule(schedule_type, initial_lr, decay_steps, decay_rate, momentum):
    """
    returning SGD optimizer with momentum and learning rate schedule

    args:
    - schedule_type: (str) 
        - 'exponential'
        - 'inverse_time'
    - initial_lr: (float)
    - decay_steps: (int) # of steps before applying decay
    - decay_rate: (float)
    - momentum: (float)
    - learning rate decay is stepwise

    returns:
    - optimizer
    - lr_schedule
    """
    if schedule_type == "exponential":
        lr_schedule = keras.optimizers.schedules.ExponentialDecay(
            initial_learning_rate=initial_lr,
            decay_steps=decay_steps,
            decay_rate=decay_rate,
            staircase=True
            )

    elif schedule_type == 'inverse_time':
        lr_schedule = keras.optimizers.schedules.InverseTimeDecay(
            initial_learning_rate=initial_lr,
            decay_steps=decay_steps,
            decay_rate=decay_rate,
            staircase=True
            )
        
    optimizer = keras.optimizers.SGD(
        learning_rate=lr_schedule,
        momentum=momentum
    )

    return optimizer, lr_schedule
