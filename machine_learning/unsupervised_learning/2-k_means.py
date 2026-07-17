#!/usr/bin/env python3
"""
--- TASK 2 ---
function creating K-Means clustering model
"""

from sklearn import cluster


def K_Means(X, n_clusters, random_state):
    """
    function creating k-means cluster

    args:
    - X (ndarray) shape (n_samples, n_features)
    - n_clusters (int) - numbers of clusters
    random_state (int) - Random seed for reproducibility

    returns:
    k-means instance fitted on input data
    """
    kmean = cluster.KMeans(n_clusters=n_clusters, random_state=random_state)
    k = kmean.fit(X)

    return k