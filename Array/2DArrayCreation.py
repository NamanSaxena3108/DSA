import numpy as np
twoDarray=np.array([[11,15,10,6],[10,14,11,5],[12,17,12,8],[15,18,14,9]])
print(twoDarray)
newTwoDarray=np.insert(twoDarray,0,[[1,2,3,4]],axis=1)
print(newTwoDarray)
new2Darray=np.insert(twoDarray,0,[[1,2,3,4]],axis=0)
print(new2Darray)
new2Darray=np.append(twoDarray,[[1,2,3,4]],axis=0)
print(new2Darray)
