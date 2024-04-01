[<img width=900 src="../img/title.png?raw=yes">](../README.md)   
[Syllabus](../README.md) |
[Slides and Assignments](README.md) |
[Project](project.md) |
[Lecturer](https://www.rit.edu/directory/efgics-erik-golen) 

## Predict whether a job posting is real or fake

### Goal
Train a model (in [project.py](project/project.py)) to predict whether a job posting is real or fake on the provided [dataset](data/job_train.csv).

### Requirements

- Can use any classification model, preprocessing, tuning method. 
- Can use (but do not have to use) all data in the [dataset](data/job_train.csv) to train the model.
- Make sure there are no errors when executing [test.py](project/test.py) (do not modify this file).
- Total runtime < 30 min (if tuning is performed as part of the process, its runtime is included)
- Can only install packages: 
  + scikit-learn, nltk, gensim, pandas, geneticalgorithm
  + packages such as numpy can be used because installing scikit-learn will also install numpy
  
### Assessment

- F1 score for *fraudulent == 1* 

### Grading

- **Performance**
  + all submissions will be ranked by their F1 score on a test set (not given to you).
  + submissions with higher F1 score will receive higher grades.
  + points will range from 20 to 30 (as long as your algorithm successfully gives predictions, you will earn 20 points).

- **Cost**
  + for submissions with similar performances
  + those with lower runtime will receive higher grades.

- **Innovation**
  + submissions with innovative solutions (different solutions from your classmates) will receive up to 3 extra points.
  + submissions with really strong innovative solutions (different solutions from basic standard models) can receive up to 10 extra points.
  
- **Violations**
  + submissions with runtime > 30 min on the TA's machine will have (runtime in min - 30) deducted from their earned points.
  + submissions that require extra packages will not be graded.


