#Creation
t=('a','b','c','d','e')
print(t)
t1=('a',)  #comma is important to make it a tuple
print(t1)
t2=tuple()
print(t2)  #create an empty tuple
t3=tuple('abcde')
print(t3)  #('a','b','c','d','e')
t4=('a')
print(type(t4))  #this will create a string

#Time Complexity = O(1)
#Space Complexity = O(n)