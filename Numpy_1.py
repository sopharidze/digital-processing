import numpy as np


size = 11
arr = np.zeros((size,size))


for i in range(size):
	for j in range(size):
		if (i == j):
			arr[i][j] = 1
		elif ((size - 1) - i == j):
			arr[i][j] = 1

print (arr)
