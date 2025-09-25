import numpy as np

a = np.array([[1, 2, 3], [10, 20, 30]])
b = np.array([[4, 5, 6], [40, 50, 60]])

c1 = np.stack((a, b), axis=0)  # row wise
c2 = np.stack((a, b), axis=1)  # column wise
c3 = np.stack((a, b), axis=-1)  # last wise

print(c1, "\n")
print(c2, " \n")
print(c3)
