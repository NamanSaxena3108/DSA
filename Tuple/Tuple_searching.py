#Searching
t=('a','b','c','d','e')
#In 
print('a' in t)      #True
print('f' in t)      #False
#Index
print(t.index('e'))  #4
#print(t.index('f')) #error
#Particular value
def Searchtuple(p_tuple,value):
    for i in range(0,len(p_tuple)):
        if p_tuple[i]==value:
            return f"The {value} is found at index {i}"
    return 'Element is not found'
print(Searchtuple(t,'e'))  

#Time Complexity = O(n)
#Space Complexity = O(1)