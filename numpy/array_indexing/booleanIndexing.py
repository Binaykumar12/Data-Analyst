import numpy as np

arr  = np.array([10,20,30,40,50])

print(arr[arr>10])

print(arr[(arr>10) & (arr<50)])