import numpy as np

arr = np.array([10, 12, 30, 25, 14, 50])

category = np.array(["Minor", "Adult"])

res = np.where(arr>18,category[1],category[0])


print(res)
