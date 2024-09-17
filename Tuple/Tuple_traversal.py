#Traversing
t=('a','b','c','d','e')
#Method 1:
for i in t:
    print(i,end=" ")

#Method 2:
for i in range(len(t)):
    print(t[i],end=" ")

#Time Complexity = O(n)
#Space Complexity = O(1)