#!/usr/bin/env python3
"""
--- TASK 4 ---
function performing agglomerative hierarchical clustering
"""

from sklearn import cluster
from sklearn import metrics
Apply_PCA = __import__('1-pca').Apply_PCA


def Agglomerative_Clustering(X, n_clusters, random_state, n_components, use_pca_data=True):
    """
    function performing agglomerative hierarchical clustering
    3 Tasks:
    1) Dimensionality reduction (optional): only if use_pca_data=True
    2) Clustering: using Ward linkage
    Evaluation: Compute silhouerte score for clustering (n_clusters > 1)


    args:
    - X (ndarray) shape: n_samples, n_features
    - n_clusters (int) number of clusters
    - random_state (int)
    - n_components: number of pca compoments if use_pca_data)true
    - use_pca_data (bool)

    returns:
    - aggloClust: fitted agglomerative Clustering instance
    ndarray: (PCA reduced or original)
    float: silhouete score of clustering (None if n_clusters=1)
    """

    # dimensionality reduction
    if use_pca_data:
        pca = Apply_PCA(X, n_components, random_state)
    else:
        pca = X
    
    # Clustering
    model = cluster.AgglomerativeClustering(n_clusters)
    y_means = model.fit_predict(pca)

    # silhouette
    silhouette = metrics.silhouette_score(pca, y_means)

    return y_means, pca, silhouette
