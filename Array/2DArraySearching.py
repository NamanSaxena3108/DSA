import numpy as np 
twoDarray=np.array([[11,15,10,6],[10,14,11,5],[12,17,12,8],[15,18,14,9]])
print(twoDarray)

def search2DArray(array,value):
  for i in range(len(array)):
    for j in range(len(array[0])):
      if array[i][j]==value:
        return 'the value is at index '+str(i)+" "+str(j)
  return 'the value is not found'

print(search2DArray(twoDarray,14))