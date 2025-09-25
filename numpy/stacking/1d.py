import numpy as np

arr1 = np.array([1,2,3,4,5,6])
arr2 = np.array([7,8,9,10,11,12])

c1 = np.stack((arr1,arr2),axis=0)     #row wise
c2 = np.stack((arr1,arr2),axis=1)       #column wise
c3 = np.stack((arr1,arr2),axis=-1)       #last wise

print(c1,"\n")
print(c2," \n")
print(c3)