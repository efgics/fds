[<img width=900 src="../img/title.png?raw=yes">](../README.md)   
[Syllabus](../README.md) |
[Slides and Assignments](README.md) |
[Project](project.md) |
[Lecturer](https://www.rit.edu/directory/efgics-erik-golen) 

## K-Means Clustering

### Make sure your repo is up-to-date

Assignment code is pushed weekly during the semester, so please pull from this repo first and copy the Kmeans folder to your repo. 

### Build your own K-Means Clustering Algorithm (with continuous input)

#### Implement my_KMeans.fit() function in [my_KMeans.py](Kmeans/my_KMeans.py)
Inputs:
- X: pd.DataFrame, independent variables, each value is a continuous number of float type

#### Implement my_KMeans.predict() function in [my_KMeans.py](Kmeans/my_KMeans.py)
Input:
- X: pd.DataFrame, independent variables, each value is a continuous number of float type

Output:
- Predicted categories of each input data point. List of str or int.

#### Implement my_KMeans.transform() function in [my_KMeans.py](Kmeans/my_KMeans.py)
Transform to cluster-distance space.
Input:
- X: pd.DataFrame, independent variables, each value is a continuous number of float type

Output:
- dists = list of [dist to centroid 1, dist to centroid 2, ...]

### Test my_KMeans Algorithm with [A8.py](Kmeans/A8.py)

 - It is expected to perform similar to [sklearn.cluster.KMeans](https://scikit-learn.org/stable/modules/generated/sklearn.cluster.KMeans.html) with input (algorithm = "full").
 
 - Example output:
 ```
 (base) Kmeans % python A8.py 
Classes:
[('Iris-setosa', 0), ('Iris-setosa', 0), ('Iris-setosa', 0), ('Iris-setosa', 0), ('Iris-setosa', 0), ('Iris-setosa', 0), ('Iris-setosa', 0), ('Iris-setosa', 0), ('Iris-setosa', 0), ('Iris-setosa', 0), ('Iris-setosa', 0), ('Iris-setosa', 0), ('Iris-setosa', 0), ('Iris-setosa', 0), ('Iris-setosa', 0), ('Iris-setosa', 0), ('Iris-setosa', 0), ('Iris-setosa', 0), ('Iris-setosa', 0), ('Iris-setosa', 0), ('Iris-setosa', 0), ('Iris-setosa', 0), ('Iris-setosa', 0), ('Iris-setosa', 0), ('Iris-setosa', 0), ('Iris-setosa', 0), ('Iris-setosa', 0), ('Iris-setosa', 0), ('Iris-setosa', 0), ('Iris-setosa', 0), ('Iris-setosa', 0), ('Iris-setosa', 0), ('Iris-setosa', 0), ('Iris-setosa', 0), ('Iris-setosa', 0), ('Iris-setosa', 0), ('Iris-setosa', 0), ('Iris-setosa', 0), ('Iris-setosa', 0), ('Iris-setosa', 0), ('Iris-setosa', 0), ('Iris-setosa', 0), ('Iris-setosa', 0), ('Iris-setosa', 0), ('Iris-setosa', 0), ('Iris-versicolor', 2), ('Iris-versicolor', 1), ('Iris-versicolor', 2), ('Iris-versicolor', 1), ('Iris-versicolor', 1), ('Iris-versicolor', 1), ('Iris-versicolor', 1), ('Iris-versicolor', 1), ('Iris-versicolor', 1), ('Iris-versicolor', 1), ('Iris-versicolor', 1), ('Iris-versicolor', 1), ('Iris-versicolor', 1), ('Iris-versicolor', 1), ('Iris-versicolor', 1), ('Iris-versicolor', 1), ('Iris-versicolor', 1), ('Iris-versicolor', 1), ('Iris-versicolor', 1), ('Iris-versicolor', 1), ('Iris-versicolor', 1), ('Iris-versicolor', 1), ('Iris-versicolor', 2), ('Iris-versicolor', 1), ('Iris-versicolor', 1), ('Iris-versicolor', 1), ('Iris-versicolor', 1), ('Iris-versicolor', 1), ('Iris-versicolor', 1), ('Iris-versicolor', 1), ('Iris-versicolor', 1), ('Iris-versicolor', 1), ('Iris-versicolor', 1), ('Iris-versicolor', 1), ('Iris-versicolor', 1), ('Iris-versicolor', 1), ('Iris-versicolor', 1), ('Iris-versicolor', 1), ('Iris-versicolor', 1), ('Iris-versicolor', 1), ('Iris-versicolor', 1), ('Iris-versicolor', 1), ('Iris-versicolor', 1), ('Iris-versicolor', 1), ('Iris-versicolor', 1), ('Iris-virginica', 2), ('Iris-virginica', 1), ('Iris-virginica', 2), ('Iris-virginica', 2), ('Iris-virginica', 2), ('Iris-virginica', 2), ('Iris-virginica', 1), ('Iris-virginica', 2), ('Iris-virginica', 2), ('Iris-virginica', 2), ('Iris-virginica', 2), ('Iris-virginica', 2), ('Iris-virginica', 2), ('Iris-virginica', 1), ('Iris-virginica', 1), ('Iris-virginica', 2), ('Iris-virginica', 2), ('Iris-virginica', 2), ('Iris-virginica', 2), ('Iris-virginica', 1), ('Iris-virginica', 2), ('Iris-virginica', 1), ('Iris-virginica', 1), ('Iris-virginica', 2), ('Iris-virginica', 2), ('Iris-virginica', 2), ('Iris-virginica', 2), ('Iris-virginica', 2), ('Iris-virginica', 1), ('Iris-virginica', 2), ('Iris-virginica', 2), ('Iris-virginica', 2), ('Iris-virginica', 2), ('Iris-virginica', 1), ('Iris-virginica', 2), ('Iris-virginica', 2), ('Iris-virginica', 2), ('Iris-virginica', 1), ('Iris-virginica', 2), ('Iris-virginica', 2), ('Iris-virginica', 2), ('Iris-virginica', 1), ('Iris-virginica', 2), ('Iris-virginica', 2), ('Iris-virginica', 1)]

Centroids:
[array([4.97777778, 3.38, 1.48222222, 0.24]), array([5.88333333, 2.75740741, 4.4037037 , 1.43888889]), array([6.825, 3.075, 5.68055556, 2.06111111])]

Lowest SSE: 67.455130

Testing data:
[[0.8771981208426503, 3.908052869279141, 5.586474379038563], [1.068503048864203, 3.6537027651065976, 5.044339664844246], [1.2601273696155961, 3.498929387499919, 4.82261183141907], [0.7123738788093484, 3.5001993868349057, 4.965864184486464], [0.19924549036828546, 3.3888580245508093, 4.957914703771791], [3.7021808721180194, 0.7692633606053402, 1.3520874350790932], [2.7754336776016526, 0.8517451624010108, 2.527586989136934], [2.5600626921335974, 1.5372857897773275, 3.2197871546093912], [3.157342217204719, 0.3230459883088073, 1.8352494195881814], [3.058454382507044, 0.8245691396832467, 2.32303115894559], [6.1700647294361595, 2.9815959260298794, 1.3726804228260423], [4.04047974171507, 0.744055085206515, 1.0457992100084585], [4.921554507006105, 1.7546518614833146, 0.26103722358844833], [5.273953702330064, 2.146639796115343, 0.5713788283022926], [3.907873660088038, 0.6241345173499059, 1.1444680418279174]]

Cluster predictions:
[0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 2, 1, 2, 2, 1]

 ```
 Results can be different due to randomness. SSEs should be similar.

### Do not forget to push your local changes to the Github server.

## Grading Policy
 - Importing additional packages such as sklearn to perform clustering or making cluster predictions is not allowed.
 - 4 (out of 7) points will be received if A8.py successfully runs and makes predictions.
 - The remaining 3 points will be given based on the percentage of same predictions with the correct implementation.
   
## Hint
 - Feel free to use the hint file to help you get started [my_KMeans_hint.py](Kmeans/my_KMeans_hint.py).
 - If you use it, remember to rename it as my_KMeans.py before submitting. 
