import numpy as np

A = np.array([ [1, 2], [3, 4], [5, 6] ])
B = np.array([ [2, 3], [2, 3] ])
C = np.matmul(A, B) # 행렬 곱셈 A * B
print(C) # 결과는 3x2 행렬