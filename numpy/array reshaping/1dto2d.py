import numpy as np

arr = np.array([1,2,3,4,5,6,7,8,9,10])
print(arr)
print(arr.reshape(2,5))

reshaped = np.reshape(arr,(5,2))
print(reshaped)
