my_dict={'name': 'Edy', 'age': 27, 'address': 'London','education':'master'}

#Deleting
#del my_dict['age']
#print(my_dict)

#Removing
removed_item=my_dict.pop('age',None)
print(removed_item)
print(my_dict)
removed_item2=my_dict.popitem()
print(removed_item2)
print(my_dict)
my_dict.clear()
print(my_dict)