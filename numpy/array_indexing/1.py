import numpy as np

# arr = np.arange(10,51,2)
# print(arr)
# print(arr[:5])

# arr = np.random.randint(1,21,(5,5))
# print("Array: \n",arr)
# print("First Row :\n",arr[0])
# print(f"Last column:{arr[:,-1]}")
# print("subarray:\n",arr[1:5,2:4])

# arr = np.array([1,2,3,4,5,6,7,8,9])
# print("Reversed array : \n",arr[::-1])

# arr = np.arange(1, 13)
# print("Reshape : \n", arr.reshape(3, 4))
# print("Reshape : \n", arr.reshape(2, 6))

arr = np.array([[1, 2, 3], [4, 5, 6]])
print("Array:\n", arr)
print("Flattened :\n", arr.flatten())
