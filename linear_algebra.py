import numpy as np
import math

# linalg.det
# The linalg.det tool computes the determinant of an array.
print(math.floor(np.linalg.det([[1 , 2], [2, 1]])))

# linalg.eig
# The linalg.eig computes the eigenvalues and right eigenvectors of a square array.
vals, vecs = np.linalg.eig([[1 , 2], [2, 1]])
print(vals)
print(vecs)

# linalg.inv
# The linalg.inv tool computes the (multiplicative) inverse of a matrix.
print(np.linalg.inv([[1 , 2], [2, 1]]))

N = int(input().strip())
ar = []

for i in range(N):
    ar.append(list(map(float, input().strip().split())))

print(round(np.linalg.det(ar), 2))
