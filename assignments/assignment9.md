[<img width=900 src="../img/title.png?raw=yes">](../README.md)   
[Syllabus](../README.md) |
[Slides and Assignments](README.md) |
[Project](project.md) |
[Lecturer](https://www.rit.edu/directory/efgics-erik-golen) 

## Silhouette Coefficient

### Make sure your repo is up-to-date

Assignment code is pushed weekly during the semester, so please pull from this repo first and copy the Silhouette folder to your repo. Four new data files (k2.csv, k3.csv, k5.csv, k7.csv) have been added to the data directory; be sure to pull these as well.

### Calculate the silhouette coefficient for clusters of size "k" to determine the best "k" value

#### Implement code to calculate the silhouette coefficient for the iris data set
You will be calculating the average silhouette coefficient for runs of k-means on the iris data with a k of 2, 3, 5, and 7 clusters. Input files are in the data folder and are k2.csv, k3.csv, k5.csv, and k7.csv, respectively.

Each data file contains 150 iris flowers that were clustered using k-means clustering. Clustering was done using SepalLength, SepalWidth, PetalLength, and PetalWidth. The Cluster column denotes which cluster each data instance ended up in once k-means converged. Note that the Instance column is of no use and should be ignored. You should use Euclidean distance to calculate the distances between data instances.

#### Suggested functions to implement
Your code should iterate over all four runs of k-means, meaning that the code has to be generic enough to handle any number of clusters in the data. The structure of silhouette.py has been left to you, but below are some suggested functions. 

1. determine_clusters - Returns a collection containing the "names" of all of the clusters in the data set. This will be critical for calculating the cluster cohesion and separation.

2. calculate_cohesion - Returns the cohesion of each data instance (ai) in the given set of clusters. Be sure to NOT include the data point itself in the cohesion calculation since the distance to itself is 0.

3. calculate_separation - Returns the separation of each data instance (bi) in the given set of clusters. Each data instance will have k - 1 "candidate" separation values; the separation for that data instance will be the minimum of those separations.

4. calculate_silhouette - Returns the silhouette coefficient of each data instance (si) in the given set of clusters. You MUST use the following equation to calculate the silhouette coefficient: si = abs(1 - (ai / bi)). If you do not use the absolute value, you will not get the expected output shown below. If you do not receive the expected output, something in the code is incorrect!
 
 - Expected output:
 ```
 (base) Silhouette % python silhouette.py 

Avg silhouette coefficient for k of 2 = 0.689
Avg silhouette coefficient for k of 3 = 0.551
Avg silhouette coefficient for k of 5 = 0.450
Avg silhouette coefficient for k of 7 = 0.306

 ```
### Do not forget to push your local changes to the Github server.

## Grading Policy
 - Importing additional packages, such as sklearn, to calculate the silhouette coefficient for a set of clusters is not allowed.
 - 7 (out of 7) points will be received if silhouette.py produces the same results as those shown above.
