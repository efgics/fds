import pandas as pd
import numpy as np

class my_KMeans:

    def __init__(self, n_clusters=5, n_init = 10, max_iter=300, tol=1e-4):
        # use euclidean distance for sse calculation.
        # stop when either # iteration is greater than max_iter or the delta of self.sse_ is smaller than tol.
        # repeat n_init times and keep the best run (cluster_centers_, sse_) with the lowest sse_.
        self.n_clusters = int(n_clusters)
        self.n_init = n_init
        self.max_iter = int(max_iter)
        self.tol = tol

        self.classes_ = range(n_clusters)
        # Centroids
        self.cluster_centers_ = None
        # Sum of squared distances of samples to their closest cluster center.
        self.sse_ = None

    def fit(self, X):
        # X: pd.DataFrame, independent variables, float        
        # repeat self.n_init times and keep the best run 
            # (self.cluster_centers_, self.sse_) with the lowest self.sse_.
        # write your code below
        return

    def predict(self, X):
        # X: pd.DataFrame, independent variables, float
        # return predictions: list
        # write your code below
        return predictions

    def transform(self, X):
        # Transform to cluster-distance space
        # X: pd.DataFrame, independent variables, float
        # return dists = list of [dist to centroid 1, dist to centroid 2, ...]
        # write your code below
        return dists

    def fit_predict(self, X):
        self.fit(X)
        return self.predict(X)
