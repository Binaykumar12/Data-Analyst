import numpy as np

arr = np.array([[1, 2, 3, 4], [5, 6, 7, 8]])

print(np.array_split(arr, 3, axis=1))  # columnwise
print(np.split(arr, 2, axis=0))  # rowwise
