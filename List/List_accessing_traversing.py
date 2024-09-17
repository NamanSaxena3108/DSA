#Accessing List
shList=['milk','cheese','butter']
print(shList.all())
print(shList[0])
print(shList[1])
#print(shList[3])  error-index out of bound

print('milk' in shList)

print(shList[-1])
#print(shList[-4])  error-index out of bound

#Traversing
for i in shList:
    print(i)

for i in range(len(shList)):
    shList[i]=shList[i]+"+"
    print(shList[i])
