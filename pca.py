import numpy as np
from itertools import product

# Get covariance matrix
def cov(x):
	sizex = x.shape
	meanx = np.mean(x,1)
	cv = np.empty((sizex[1],sizex[1]))
	for var in range( 0,sizex[1]):
		x1 = x[:,var]
		mx1 = meanx[var]
		for ct in range(var,sizex[1]):
			x2 = x[:,ct]
			mx2 = meanx[ct]
			v = np.dot((x1-mx1),(x2 - mx2))/(sizex[0]-1)
			cv[var,ct] = v
			cv[ct,var] = v
	evals,evecs = np.linalg.eigh(cv)
	print evals
	return cv


x = np.array([[1,2,3],[4,5,6],[7,8,9],[10,11,12]])
print cov(x)
