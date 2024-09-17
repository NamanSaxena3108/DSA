import numpy as np 
twoDarray=np.array([[11,15,10,6],[10,14,11,5],[12,17,12,8],[15,18,14,9]])
print(twoDarray)

def accessElement(array,rowIndex,colIndex):
  if rowIndex>=len(array) and colIndex>=len(array[0]):
    print("incorrect Index")
  else:
    print(array[rowIndex][colIndex])

accessElement(twoDarray,2,3)