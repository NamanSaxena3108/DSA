#Slicing
l=['a','b','c','d','e','f','g']
print(l[0:2])
print(l[1:])
print(l[:])
l[0:2]=['x','y']
print(l)

#Deleting
print(l.pop())
print(l.pop(1))

del l[1]
del l[0:2]

l.remove('e')
print(l)