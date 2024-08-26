import numpy as np

A = np.array([[1, 2, 3], [3, 4, 5], [3, 7, 0]])

for i in range(500):
    # A = input a matrix
    Q, R = np.linalg.qr(A)
    A=np.matmul(R,Q)

print(A)
