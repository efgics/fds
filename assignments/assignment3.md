[<img width=900 src="../img/title.png?raw=yes">](../README.md)   
[Syllabus](../README.md) |
[Slides and Assignments](README.md) |
[Project](project.md) |
[Lecturer](https://www.rit.edu/directory/efgics-erik-golen) 

## Evaluation

### Make sure your repo is up-to-date

Assignment code is added during the semester, so please pull from this repo first and copy the Evaluation folder to your repo. 

### Build your own evaluation methods

#### Implement every function in [my_evaluation.py](Evaluation/my_evaluation.py)
Hint: compute self.confusion once and use it to calculate other model performance metrics, including precision, recall, F1 score, as well as macro, micro, and weighted F1 score.

### Test my_evaluation Algorithm with [A3.py](Evaluation/A3.py)

Expected output:
```
(base) Evaluation % python A3.py 
['Iris-setosa' 'Iris-setosa' 'Iris-setosa' 'Iris-setosa' 'Iris-setosa'
 'Iris-setosa' 'Iris-setosa' 'Iris-setosa' 'Iris-setosa' 'Iris-setosa'
 'Iris-setosa' 'Iris-setosa' 'Iris-setosa' 'Iris-setosa' 'Iris-setosa'
 'Iris-setosa' 'Iris-setosa' 'Iris-setosa' 'Iris-setosa' 'Iris-setosa'
 'Iris-setosa' 'Iris-setosa' 'Iris-setosa' 'Iris-setosa' 'Iris-setosa'
 'Iris-setosa' 'Iris-setosa' 'Iris-setosa' 'Iris-setosa' 'Iris-setosa'
 'Iris-setosa' 'Iris-setosa' 'Iris-setosa' 'Iris-setosa' 'Iris-setosa'
 'Iris-setosa' 'Iris-setosa' 'Iris-setosa' 'Iris-setosa' 'Iris-setosa'
 'Iris-setosa' 'Iris-setosa' 'Iris-setosa' 'Iris-setosa' 'Iris-setosa'
 'Iris-versicolor' 'Iris-versicolor' 'Iris-versicolor' 'Iris-versicolor'
 'Iris-versicolor' 'Iris-versicolor' 'Iris-versicolor' 'Iris-versicolor'
 'Iris-versicolor' 'Iris-versicolor' 'Iris-versicolor' 'Iris-versicolor'
 'Iris-versicolor' 'Iris-versicolor' 'Iris-versicolor' 'Iris-virginica'
 'Iris-versicolor' 'Iris-versicolor' 'Iris-versicolor' 'Iris-versicolor'
 'Iris-versicolor' 'Iris-versicolor' 'Iris-versicolor' 'Iris-versicolor'
 'Iris-versicolor' 'Iris-versicolor' 'Iris-versicolor' 'Iris-versicolor'
 'Iris-versicolor' 'Iris-versicolor' 'Iris-versicolor' 'Iris-versicolor'
 'Iris-versicolor' 'Iris-versicolor' 'Iris-versicolor' 'Iris-versicolor'
 'Iris-versicolor' 'Iris-versicolor' 'Iris-versicolor' 'Iris-versicolor'
 'Iris-versicolor' 'Iris-versicolor' 'Iris-versicolor' 'Iris-versicolor'
 'Iris-versicolor' 'Iris-virginica' 'Iris-virginica' 'Iris-virginica'
 'Iris-virginica' 'Iris-virginica' 'Iris-virginica' 'Iris-versicolor'
 'Iris-virginica' 'Iris-virginica' 'Iris-virginica' 'Iris-virginica'
 'Iris-virginica' 'Iris-virginica' 'Iris-virginica' 'Iris-virginica'
 'Iris-virginica' 'Iris-virginica' 'Iris-virginica' 'Iris-virginica'
 'Iris-versicolor' 'Iris-virginica' 'Iris-virginica' 'Iris-virginica'
 'Iris-virginica' 'Iris-versicolor' 'Iris-virginica' 'Iris-virginica'
 'Iris-virginica' 'Iris-versicolor' 'Iris-versicolor' 'Iris-virginica'
 'Iris-virginica' 'Iris-virginica' 'Iris-virginica' 'Iris-virginica'
 'Iris-virginica' 'Iris-virginica' 'Iris-virginica' 'Iris-virginica'
 'Iris-virginica' 'Iris-virginica' 'Iris-virginica' 'Iris-virginica'
 'Iris-virginica' 'Iris-virginica']
{'Iris-setosa': {'prec': 1.0, 'recall': 1.0, 'f1': 1.0}, 'Iris-versicolor': {'prec': 0.8979591836734694, 'recall': 0.9777777777777777, 'f1': 0.9361702127659575}, 'Iris-virginica': {'prec': 0.975609756097561, 'recall': 0.8888888888888888, 'f1': 0.9302325581395349}}
Average F1 scores:
{'macro': 0.9554675903018307, 'micro': 0.9555555555555556, 'weighted': 0.9554675903018307}
```

### Do not forget to push your local changes to the Github server.

 ## Grading Policy
 - Importing additional packages that can compute these model performance metrics, such as sklearn, is not allowed.
 - 4 (out of 7) points will be received if A3.py successfully runs and evaluates the performance.
 - The remaining 3 points will be given based on the percentage of the same performance metrics with the correct implementation.

## Hint
 - If you would like some hints or are looking for help getting started, take a look at [my_evaluation_hint.py](Evaluation/my_evaluation_hint.py).
 - Remember to rename it as my_evaluation.py before submitting. 
