[<img width=900 src="../img/title.png?raw=yes">](../README.md)   
[Syllabus](../README.md) |
[Slides and Assignments](README.md) |
[Project](project.md) |
[Lecturer](https://www.rit.edu/directory/efgics-erik-golen) 

## Hyperparameter Tuning

### Make sure your repo is up to date

Assignment code is pushed weekly during the semester, so please pull from this repo first and copy the Tuning folder to your repo. 

### Make sure your Assignment 3 is correct

This assignment uses my_evaluation from Assignment 3 to compute the macro F1 score of a DecisionTreeClassifier.

### Use a Genetic Algorithm for tuning model parameters

You will be using a Python library called [geneticalgorithm](https://pypi.org/project/geneticalgorithm/) for this assignment in order to tune hyperparameters for the DecisionTreeClassifier using the Breast Cancer data set from Assignment 6. You will need to install geneticalgorithm using pip. For example, "pip install geneticalgorithm". The geneticalgorithm library expects matplotlib to be installed. If you do not already have it installed in miniconda, use the command "conda install matplotlib" to install it.

The geneticalgorithm library requires you to specify the search space for the problem, as well as an objective function. In [GA.py](Tuning/GA.py), you have been given an example search space and objective function for the well known Rastrigin function. The 2-dimensional Rastrigin function has a global minimum of 0 at (0, 0) and its input values range from -5.12 to 5.12 for each dimension. When you run the example code, you will find that the Genetic Algorithm will find a solution very close to (0, 0), with an objective function value near 0.

In addition, you have been given a search space for the DecisionTreeClassifier in the variable "varbound", where the first dimension represents two possible criterion (0 for gini and 1 for entropy) and max_depth values ranging from 1 to 12. You will need to add in code train a DecisionTreeClassifier using breast_cancer.csv as part of the function f, which will be maximizing the macro F1 score across the two classes in the Breast cancer data set, no-recurrence-events and recurrence-events.

Currently, the function f is maximizing the values of the integers in each dimension, as an example. Notice that the objective function value, OF, is negated because the function is trying to maximize the result. You will want to do the same thing, except with the macro F1 score for the DecisionTreeClassifier. 

Expected output:
```
(base) Tuning % python GA.py
 
 The best solution found:
 [ 0. 12.]

 Objective function:
 -0.915927902839019
```
Results may be slightly different due to randomness. Try executing it multiple times.

### Do not forget to push your local changes to the Github server.
 
## Grading Policy
 - 4 (out of 7) points will be received if GA.py successfully runs and finds a parameter set.
 - The remaining 3 points will be given based on the correctness of the implementation (TA will examine it manually).
