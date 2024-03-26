import math
import numpy as np
import pandas as pd
from geneticalgorithm import geneticalgorithm as ga

def rastrigin(X):
    dim=len(X)         

    OF=0
    for i in range (0,dim):
        OF += (X[i]**2)-10*math.cos(2*math.pi*X[i])+10

    return OF

def f(X):
	dim = len(X)

	OF = 0

	for i in range(0, dim):
		OF += X[i]
	return -OF

rastrigin_bound=np.array([[-5.12,5.12]]*2)
rastrigin_model=ga(function=rastrigin,dimension=2,variable_type='real',variable_boundaries=rastrigin_bound)
rastrigin_model.run()

# criterion = 0 for gini, 1 for entropy and max_depth = 1-12 for a DecisionTreeClassifier
varbound = np.array([[0,1], [1,12]])
model=ga(function=f,dimension=2,variable_type='int',variable_boundaries=varbound)
model.run()
