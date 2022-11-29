import numpy as np

x = [[1,2,3 ],[3,4, 3], [5,6, 3]]
x = np.array(x)

#print(np.all(x>2, axis=1))
#print(np.delete(x[np.all(x>2, axis=1)], 1, 1))

c = np.array([1,1,0])
a = np.array([1,2,3])



z = a[c==1] ** 2 #+ b[c==1] - a[c==0]


print(z.shape)