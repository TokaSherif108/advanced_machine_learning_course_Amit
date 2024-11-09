#vector 
import numpy as np
'''import numpy as np
m=np.array([[1,2,3],[4,"a",6],[7,8,9]])
fmat=m.astype(float)
print(fmat)
print(fmat.dtype)'''
vec=np.array([1,2,3,4,5,6])
#mat=vec.reshape((3,2))
mat=vec.reshape((vec.shape[0],1))
print(mat)
print(mat.shape)
x=vec.reshape((-1,1))
print(x)
M=np.array([[1,2,3],[4,5,6],[7,8,9],[0,0,0]])
print(M[1:3],)
