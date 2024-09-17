from array import *
#1.Create an array and traverse.
my_array =array('i',[1,2,3,4,5])
for i in my_array:
    print(i)
#2.Access individual elements thorugh indexes.
print("Step 2")
print(my_array[0])
#3.Append any value to the array using append() method
print("Step 3")
my_array.append(6)
print(my_array)
#4.Insert value in an array using insert() method
print("Step 4")
my_array.insert(0,11)
print(my_array)
#5.Extend python array using extend() method
print("Step 5")
my_array1=array('i',[10,11,12])
my_array.extend(my_array1)
print(my_array)
#6.Add items from list to an array using fromlist() method 
print("Step 6")
tempList=[20,21,22]
my_array.fromlist(tempList)
print(my_array)
#7.Remove an array element using remove() method
print("Step 7")
my_array.remove(11)
print(my_array)
#8.Remove last array element using pop() method
print("Step 8")
my_array.pop()
print(my_array)
#9.Fetch any element through its index using index() method
print("Step 9")
print(my_array.index(21))
#10.Reverse a python array using reverse() method
print("Step 10")
my_array.reverse()
print(my_array)
#11.Get array buffer information thorugh buffer_info() method
print("Step 11")
print(my_array.buffer_info())
#12.Check for number of occurrences of an element using count() method
print("Step 12")
my_array.append(11)
print(my_array)
print(my_array.count(11))   
#13.Convert array to string using tostring() method
print("Step 13")
strtemp=','.join(map(str,my_array))
print(strtemp)
#14.Convert array to a python list with same element using tolist() method
print("Step 14")
l1=my_array.tolist()
print(l1)
#15.Append a string to char array using fromstring() method
print("Step 15")
strTemp=my_array.tobytes()
print(strTemp)
ints=array('i')
ints.frombytes(strTemp)
print(ints)
#16.Slice elements from an array
print("Step 16")
print(my_array[1:4])