#!/usr/bin/env python3
"""
--- TASK 3 ---
function evaluates K-Mean clusting qulaity using silhouette scores
"""

from sklearn import metrics
K_Means = __import__('2-k_means').K_Means


def optimal_k(X, max_clusters, random_state):
    """
    function evaluating K-Means clustering quality by silhouette scores
    computing the inertia to be used for the elbow method

    args:
    - X (ndarray) shape: (n_samples, n_features)
    - max_clusters (int) Max numbers clusters >=2
    - random_state (int) Random seed for reproducibility

    Return:
    - list[int]: evaluated cluster numbers
    - list[float]: inertia vales corresponding to each cluster #
        for ellbow method
    - list[float] Silhoette scores corresponding  for qulity eval
    """
    # list int = k
    k = []
    inertias = []
    silhouette_score = []
    for i in (2, max_clusters):
        k.append(i)
        kmeans = K_Means(X, k, random_state+1)
        inertias.append(kmeans.inertia_)
        silhouette_score.append(metrics.silhouette_score(X=X, kmeans.labels_, random_state=random_state))
    
    return k, inertias, silhouette_score

