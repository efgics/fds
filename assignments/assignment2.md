[<img width=900 src="../img/title.png?raw=yes">](../README.md)   
[Syllabus](../README.md) |
[Slides and Assignments](README.md) |
[Project](project.md) |
[Lecturer](https://www.rit.edu/directory/efgics-erik-golen) 

## Preprocessing

### Make sure your repo is up-to-date

Assignment code will be added weekly, so please pull from this repo first and copy over that week's folder to your repo. This week's assignment folder is the Preprocess folder. 

### Build your own preprocessing
The idea in this assignment is to see the effect that normalization techniques may have on model prediction results. There are four normalization techniques that were presented in lecture that you will be implementing: Min-Max, Standard Score, L1 Normalization, and L2 Normalization. In addition, you will be writing a stratified sampling function in order to provide a sample that is hopefully representative of the full iris data set.

#### Complete the code in [my_preprocess.py](Preprocess/my_preprocess.py)
You will be implementing each of the four normalization techniques from lecture and a stratified sampling function.

### Test my_preprocess with [A2.py](Preprocess/A2.py)
A2.py will need to be modified so that it builds a Decision Tree model each of the four normalization techniques using the training data and then performs predictions on the test data.

The output below shows summary statistics of the sepal lengths of the test data, the original iris class distribution, and the expected output for all of the normalizers.
```
(base) D:\projects\DSCI-633\assignments\Preprocess>python A2.py
Before normalization:
Min Sepal Length = 4.4
Mean Sepal Length = 5.832592592592594
Max Sepal Length = 7.9

Iris class distribution:
Counter({'Iris-setosa': 45, 'Iris-versicolor': 45, 'Iris-virginica': 45})

Running Min-Max normalizer
After normalization:
Min Sepal Length = 0.0
Mean Sepal Length = 0.40931216931216924
Max Sepal Length = 1.0

Sample class distribution:
Counter({'Iris-setosa': 23, 'Iris-versicolor': 23, 'Iris-virginica': 23})

Model predictions:
['Iris-setosa' 'Iris-setosa' 'Iris-setosa' 'Iris-setosa' 'Iris-setosa'
 'Iris-versicolor' 'Iris-versicolor' 'Iris-virginica' 'Iris-versicolor'
 'Iris-versicolor' 'Iris-virginica' 'Iris-virginica' 'Iris-virginica'
 'Iris-virginica' 'Iris-virginica']

Running Standard_Score normalizer
After normalization:
Min Sepal Length = -1.7456935615254507
Mean Sepal Length = -1.2105542905542447e-15
Max Sepal Length = 2.5192506361000664

Sample class distribution:
Counter({'Iris-setosa': 23, 'Iris-versicolor': 23, 'Iris-virginica': 23})

Model predictions:
['Iris-setosa' 'Iris-setosa' 'Iris-setosa' 'Iris-setosa' 'Iris-setosa'
 'Iris-versicolor' 'Iris-versicolor' 'Iris-versicolor' 'Iris-versicolor'
 'Iris-versicolor' 'Iris-virginica' 'Iris-virginica' 'Iris-virginica'
 'Iris-virginica' 'Iris-virginica']

Running L1 normalizer
After normalization:
Min Sepal Length = 0.005588011176022352
Mean Sepal Length = 0.007407407407407406
Max Sepal Length = 0.010033020066040132

Sample class distribution:
Counter({'Iris-setosa': 23, 'Iris-versicolor': 23, 'Iris-virginica': 23})

Model predictions:
['Iris-setosa' 'Iris-setosa' 'Iris-setosa' 'Iris-setosa' 'Iris-setosa'
 'Iris-versicolor' 'Iris-versicolor' 'Iris-versicolor' 'Iris-versicolor'
 'Iris-versicolor' 'Iris-virginica' 'Iris-versicolor' 'Iris-virginica'
 'Iris-virginica' 'Iris-versicolor']

Running L2 normalizer
After normalization:
Min Sepal Length = 0.06429355118375138
Mean Sepal Length = 0.08522683872405021
Max Sepal Length = 0.11543614871628087

Sample class distribution:
Counter({'Iris-setosa': 23, 'Iris-versicolor': 23, 'Iris-virginica': 23})

Model predictions:
['Iris-setosa' 'Iris-setosa' 'Iris-setosa' 'Iris-setosa' 'Iris-setosa'
 'Iris-versicolor' 'Iris-versicolor' 'Iris-versicolor' 'Iris-versicolor'
 'Iris-versicolor' 'Iris-virginica' 'Iris-virginica' 'Iris-virginica'
 'Iris-virginica' 'Iris-virginica']
```
Model prediction results may be a little bit different due to randomness in stratified sampling (but should be very similar). 

### Do not forget to push your local changes to the Github server.
 
 ## Grading Policy
 - Importing additional packages to perform normalization and/or stratified sampling, such as in sklearn, is not allowed.
 - 4 (out of 7) points will be received if A2.py successfully runs and makes predictions
 - The 3 remaining points will be given based on the percentage of the same predictions with the correct implementation.
   
## Hint
 - If you are having difficulty implementing everything needed for my_preprocess.py, or just want to get an idea of how to start, take a look at [my_preprocess_hint.py](Preprocess/my_preprocess_hint.py).
 - If you're going to use this file as a starting point, remember to rename it as my_preprocess.py before submitting. 
