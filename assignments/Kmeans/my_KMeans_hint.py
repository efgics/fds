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

    def dist(self, a, b):
        # Compute Euclidean distance between a and b
        return np.sum((np.array(a)-np.array(b))**2)**(0.5)

    def initiate(self, X):
        # Initiate cluster centers
        # Input X is numpy.array
        # Output cluster_centers (list)
        cluster_centers = "write your own code"
        return cluster_centers

    def fit_once(self, X):
        # Fit once
        # Input X is numpy.array
        # Output: cluster_centers (list), sse

        # Initiate cluster centers
        cluster_centers = self.initiate(X)
        last_sse = None
        # Iterate
        for i in range(self.max_iter+1):
            # Assign each training data point to its nearest cluster_centers
            clusters = [[] for i in range(self.n_clusters)]
            sse = 0
            for x in X:
                # calculate distances between x and each cluster center
                dists = [self.dist(x, center) for center in cluster_centers]
                # calculate sse
                sse += "write your own code"
                # find the cluster that x belongs to
                cluster_id = "write your own code"
                # add x to that cluster
                clusters[cluster_id].append(x)

            if (last_sse and last_sse - sse < self.tol) or i==self.max_iter:
                break
            
            # Update cluster centers
            cluster_centers = "Write your own code"
            last_sse = sse

        return cluster_centers, sse

    def fit(self, X):
        # X: pd.DataFrame, independent variables, float
        # repeat self.n_init times and keep the best run
            # (self.cluster_centers_, self.sse_) with the lowest self.sse_.
        X_feature = X.to_numpy()
        for i in range(self.n_init):
            cluster_centers, sse = self.fit_once(X_feature)
            if self.sse_==None or sse < self.sse_:
                self.sse_ = sse
                self.cluster_centers_ = cluster_centers
        return

    def transform(self, X):
        # Transform to cluster-distance space
        # X: pd.DataFrame, independent variables, float
        # return dists = list of [dist to centroid 1, dist to centroid 2, ...]
        dists = [[self.dist(x,centroid) for centroid in self.cluster_centers_] for x in X.to_numpy()]
        return dists

    def predict(self, X):
        # X: pd.DataFrame, independent variables, float
        # return predictions: list
        predictions = [np.argmin(dist) for dist in self.transform(X)]
        return predictions

    def fit_predict(self, X):
        self.fit(X)
        return self.predict(X)
