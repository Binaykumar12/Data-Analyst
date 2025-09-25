import numpy as np

arr = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9])
print(arr)
print(np.ndim(arr))   #tells dimension of arr

print(np.resize(arr, (3, 5)))  # repeat elements

arr.resize((5, 5), refcheck=False)
print(arr)
