import numpy as np

arr = np.arange(16).reshape((4, 2, 2))
print(arr)
print(np.dsplit(arr, 2))
