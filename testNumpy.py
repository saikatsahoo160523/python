import numpy as np

# conver 1-d array to numpy array
arry1 = [12,67,34]
np_arry1 = np.array(arry1)
print(np_arry1)

# conver 2-d array to numpy array
arry2 = [ [4,5,5],[7,2,2],[67,45,7] ]
np_arry2 = np.array(arry2)
print(np_arry2)

# to access data elements - can use matrix notation
print(np_arry2[2,1])

# np_arry3 = np.matrix(arry2)
# print(np_arry3)

# to check the number of rows and colloms
print(np_arry2.shape())
# to check the total number of element
print(np_arry2.size)
# can perform matrix operation
print(np_arry2.T)
print(np_arry2.min())
print(np_arry2.max())
print(np_arry2.sum())
print(np_arry2.sum(axis=0))
print(np_arry2.sum(axis=1))
# to check dimension detx
print(np_arry2.ndim)
# to check data-typ
print(np_arry2.dtype)
print(np_arry1.dtype)


#can initialize 0  with row X col
np_arry4=np.zeros((2,3))
print(np_arry4)

#can initialize 1  with row X col = 2 x 3
np_arry5=np.ones((2,3))
print(np_arry5)
# or
np_arry6=np.empty((2,3))
print(np_arry6)

# reshape and return as new variable
# it is not possible to change the original
# use -1 for auto adjust
print(np_arry2.reshape(3,-1))

#Spliting - horizontal format & vertical format
print(np.hsplit(np_arry2,3))
