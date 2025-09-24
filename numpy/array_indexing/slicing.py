import numpy as np

# arr = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
# print(arr)
# print(arr[0:2, 1:3])

arr = np.array([10, 15, 20, 25, 30])
print(arr)
print(arr[arr > 20])
print(arr[(arr > 15) & (arr < 30)])
print(arr[((arr > 10) | (arr < 25))])

