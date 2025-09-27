import numpy as np

arr = np.array([10, 20, 30, 40, 50, 60, 70])

# res = np.split(arr, 2)
# print(res)  # equal parts
print(np.array_split(arr, 6))             #unequal parts
