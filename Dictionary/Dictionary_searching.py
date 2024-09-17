#Searching
def searchDict(dict,value):
    for key in dict:
        if dict[key]==value:
            return key,value
    return 'The value is not present'

my_dict={'name': 'Edy', 'age': 27, 'address': 'London'}
print(searchDict(my_dict,27))