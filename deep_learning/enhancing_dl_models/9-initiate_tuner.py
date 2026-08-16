#!/usr/bin/env python3
"""
--- TASK 9 Hyperparameter Tuning - Initiate the Tuner
This function is initializing a Keras Tuner for hyperparameter tuning. Arguments
provided to this functions are tuner_type, build_model, x and y values, seed,
hyperband_iterations, max_trials)
"""

import keras_tuner


def initiate_tuner(
    tuner_type,
    build_model,
    seed,
    hyperband_iterations,
    max_trials,
    objective,
    overwrite=True
):
  """
  initiating hyperparameter tuning

    args:
    - tuner_type (str)
      - Hyperband
      - RandomSearch
      - BayesianOptimization
    - build_model (function) - returning a compiled model
    - x_train (ndarray) Training features
    - y_train (ndarray) Training labels
    - seed (int) - random seed
    - hyperband_iterations (int) - # of iterations
    - max_trials (int) max trials for RandomSearch and BaysianOptimization
    - objective (str) - Metric to optimize during tuning
    - overwrite (bool) Default True (whether to overwrite previous tuning project)

    return
    turner
  """

  if tuner_type == "Hyperband":
    tuner = keras_tuner.Hyperband(
        hypermodel=build_model,
        objective=objective,
        hyperband_iterations=hyperband_iterations,
        seed=seed
      )

  elif tuner_type == 'RandomSearch':
    tuner = keras_tuner.RandomSearch(
        hypermodel=build_model,
        objective=objective,
        max_trials=max_trials,
        seed=seed
        )

  elif tuner_type == "BayesianOptimization":
    tuner = keras_tuner.RandomSearch(
          hypermodel=build_model,
          objective=objective,
          max_trials=max_trials,
          seed=seed    
      )
      
  return tuner