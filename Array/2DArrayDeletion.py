import numpy as np
twoDarray=np.array([[11,15,10,6],[10,14,11,5],[12,17,12,8],[15,18,14,9]])
print(twoDarray)

new2Darray=np.delete(twoDarray,0,axis=1)# axis=1 for column and 0 for row
print(new2Darray)