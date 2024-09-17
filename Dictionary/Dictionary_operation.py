my_dict={3:'three',5:'five',9:'nine',2:'two',1:'one',4:'four'}

#in
print(3 in my_dict) #True
print("three" in my_dict) #False
print("three" in my_dict.values()) #True

#not in
print(3 not in my_dict) #False
print("three" not in my_dict) #True
print("three" not in my_dict.values()) #False

#len()
print(len(my_dict)) #6

#all() check if all keys are True or iterable
#NOTE:- 0 is considered as False
print(all(my_dict)) #True
my_dict1={0:'zero',False:'False'}
print(all(my_dict1)) #False

#any() if any one is True or iterable it returns True
print(any(my_dict)) #True
print(any(my_dict1)) #False
my_dict2={1:'one',False:'False'}
print(all(my_dict2)) #True

#sorted() returns a list of keys in sorted way
print(sorted(my_dict))
