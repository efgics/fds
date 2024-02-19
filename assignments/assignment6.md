[<img width=900 src="../img/title.png?raw=yes">](../README.md)   
[Syllabus](../README.md) |
[Slides and Assignments](README.md) |
[Project](project.md) |
[Lecturer](https://www.rit.edu/directory/efgics-erik-golen) 

## Decision Tree Classifier

### Make sure your repo is up-to-date

Assignment code is pushed weekly during the semester, so please pull from this repo first and copy the DecisionTree folder to your repo. You will also need to get two items from the data folder; breast_cancer.csv and breast_cancer_README.rtf.

### Perform an analysis using DecisionTreeClassifier
This assignment will be combining the model evaluation code you wrote for Assignment 3 (my_evaluation.py) with creating several decision tree models using sklearn's DecisionTreeClassifier. You will be using the breast_cancer data set. Be sure to go through its README file prior to working on the code so that you understand what the data set is about.

To complete this assignment, you will need to modify [A6.py](DecisionTree/A6.py) so that it creates several DecisionTreeClassifier models and prints out performance results for each model, including precision, recall, and F1 score for both class values, recurrence-events and no-recurrence-events.

You will be using two impurity metrics, Gini and entropy, and max depth values of 2, 3, 4, and 5, for a total of 8 decision tree classifier models. See the output below for results from two of them.

 Expected output:
 ```
 (base) DecisionTree % python A6.py

Impurity Metric = gini , Max Depth =  2
{'no-recurrence-events': {'prec': 0.7578125, 'recall': 0.9651741293532339, 'f1': 0.8490153172866521}, 'recurrence-events': {'prec': 0.7666666666666667, 'recall': 0.27058823529411763, 'f1': 0.39999999999999997}}

Impurity Metric = entropy , Max Depth =  2
{'no-recurrence-events': {'prec': 0.7578125, 'recall': 0.9651741293532339, 'f1': 0.8490153172866521}, 'recurrence-events': {'prec': 0.7666666666666667, 'recall': 0.27058823529411763, 'f1': 0.39999999999999997}}

 ```

### Do not forget to push your local changes to the Github server.

## Grading Policy
 - 2 (out of 7) points will be received if A6.py runs all of the DecisionTreeClassifier models using the expected parameters.
 - The remaining 5 points are based upon your answers provided in A6 Analysis Template.docx. Each question is worth 1 point and typing your performance metrics into the tables is worth 1 point. In the tables, please round your performance metrics to 3 decimal places. This document should be saved as A6.pdf and placed in your DecisionTree folder on GitHub.
 
