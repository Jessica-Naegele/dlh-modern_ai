#!/usr/bin/env python3
"""write a function splitting data into train/test sets"""

from sklearn import model_selection


def split_data(df, target='Churn', test_size=0.2, random_state=42):
    """
    df: pandas DataFrame
    target: Name of target column
    test_size: Proportion for test split
    random_state: Random seed
    Uses stratified sampling to preserve class distribution
    Returns: (X_train, X_test, y_train, y_test)
    """
    # isolate feature matrix (x) by dropping target column
    X = df.drop(columns=[target])

    # isolate target vector (y)
    y = df[target]

    # perform stratified split
    X_train, X_test, y_train, y_test = model_selection.train_test_split(
        X,
        y,
        test_size=test_size,
        random_state=random_state,
        stratify=y
    )

    return X_train, X_test, y_train, y_test
