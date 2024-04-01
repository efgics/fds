import pandas as pd
from sklearn.linear_model import SGDClassifier
from sklearn.feature_extraction.text import TfidfVectorizer
import time
import sys
sys.path.insert(0,'../..')
from my_evaluation import my_evaluation
from GA import GA

class my_model():

    def obj_func(self, predictions, actuals, pred_proba=None):
        # One objectives: higher f1 score
        eval = my_evaluation(predictions, actuals, pred_proba)
        return [eval.f1()]

    def fit(self, X, y):
        # do not exceed 29 mins
        self.preprocessor = TfidfVectorizer(stop_words='english', norm='l2', use_idf=False, smooth_idf=False)
        XX = self.preprocessor.fit_transform(X["description"])
        XX = pd.DataFrame(XX.toarray())
        # Use your GA to optimize hyperparemters for a model to get "best_parameters"
        self.clf = SGDClassifier(best_parameters)
        self.clf.fit(XX,y)
        return

    def predict(self, X):
        # remember to apply the same preprocessing in fit() on test data before making predictions
        XX = self.preprocessor.transform(X["description"])
        predictions = self.clf.predict(XX)
        return predictions
