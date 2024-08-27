import numpy as np
from scipy.linalg import logm

A1 = np.array([[3, 0, 1],
              [0, 4, 2],
              [1, 2, 5]])
for i in range(100):
    Q, R = np.linalg.qr(A1)
    A1=np.matmul(R,Q)

print(A1)
