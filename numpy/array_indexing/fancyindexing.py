import numpy as np

arr = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 0])
indices = [1, 3, 5, 7, 9]
print(arr.size)
print(arr[indices])
print(arr[[0, 2, 4, 6, 8]]) #integer array indexing
