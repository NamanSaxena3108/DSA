import array as ar
my_array=ar.array('i',[1,2,3,4])
my_array.insert(0,0)
my_array.insert(2,6)
my_array.insert(len(my_array),7)
print(my_array)