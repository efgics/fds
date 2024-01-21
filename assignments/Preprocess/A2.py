import my_preprocess
import pandas as pd
from collections import Counter
from sklearn.tree import DecisionTreeClassifier
import numpy as np
##################################################

if __name__ == "__main__":
    # Load training data
    data_train = pd.read_csv("../data/Iris_train.csv")
    
    # Separate independent variables and dependent variables
    independent = ["SepalLengthCm", "SepalWidthCm", "PetalLengthCm", "PetalWidthCm"]
    X = data_train[independent]
    y = data_train["Species"]
    
    print("Before normalization:")
    print("Min Sepal Length = " + str(np.min(X["SepalLengthCm"])))
    print("Mean Sepal Length = " + str(np.mean(X["SepalLengthCm"])))
    print("Max Sepal Length = " + str(np.max(X["SepalLengthCm"])))

    print("\nIris class distribution:")
    print(Counter(y))

    # Preprocess (train)
    normalizer = my_preprocess.my_normalizer(norm = "L2", axis = 1)
    X_norm = normalizer.fit_transform(X)

    # Perform stratified sampling
    sample = my_preprocess.stratified_sampling(y, ratio = 0.5, replace = False)
    X_sample = X_norm[sample]
    y_sample = y[sample].to_numpy()
    print("\nSample class distribution:")
    print(Counter(y_sample))
    
    # Fit model
    clf = DecisionTreeClassifier()
    clf.fit(X_sample, y_sample)
    
    # Load testing data
    data_test = pd.read_csv("../data/Iris_test.csv")
    X_test = data_test[independent]
    
    # Preprocess (test)
    X_test_norm = normalizer.transform(X_test)

    # Predict
    predictions = clf.predict(X_test_norm)
    
    # Output predictions on test data
    print("\nModel predictions:")
    print(predictions)
