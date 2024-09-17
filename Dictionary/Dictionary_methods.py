my_dict={'name': 'Edy', 'age': 26, 'address': 'London','education':'master'}
#clear()
#print(my_dict.clear()) #clear all elements

#copy()
my_dict2=my_dict.copy()
print(my_dict2)

#fromkeys()
new_dict={}.fromkeys([1,2,3],0)
print(new_dict)

#get()
print(my_dict.get('age',27)) #26
print(my_dict.get('city',27)) #27
print(my_dict.get('city'))   #None

#items()
print(my_dict.items()) #List of key value pair

#keys()
print(my_dict.keys()) #List of keys

#popitem()
print(my_dict.popitem()) #pop last element

#setdefault()
print(my_dict.setdefault('name','added')) #edy
#print(my_dict.setdefault('name1','added')) #add key name1 and it's value

#pop()
print(my_dict.pop('name1',None)) #None

#values()
print(my_dict.values()) #List of values

#update()
new_dict={'a':1,'b':2,'c':3}
my_dict.update(new_dict)
print(my_dict)  #add all element of new dictionary in my_dict