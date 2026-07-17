#!/usr/bin/env python3
"""
--- TASK 1 ---
function performing PCA
"""

from sklearn import decomposition


def Apply_PCA(X, n_components, random_state):
    """
    function performing PCA

    args:
    - X (numpy.ndarray): shape (n_samples, n_features)
    - n_components (int float None):
        - int: number of principal components to keep
        - float [0-1] Minimum fraction
        - None: Keep all components
    - random_state (int) - random seed for reproducibility
    Returns:
    - numpy.ndarray (data transformed)
    - fitted pca instance
    """

    pca = decomposition.PCA(
        n_components=n_components, random_state=random_state
        )
    pca_fit = pca.fit(X)
    df_pca = pca_fit.transform(X)

    return df_pca, pca_fit
