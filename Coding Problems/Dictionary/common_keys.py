def merge_dicts(dict1,dict2):
    result=dict1.copy()
    for key,value in dict2.items():
        result[key]=result.get(key,0) + value
    return result

dict1 = {'a': 1, 'b': 2, 'c': 3}
dict2 = {'b': 3, 'c': 4, 'd': 5}
print(merge_dicts(dict1, dict2))

#Time Complexity = O(n+m) where n is the number of element in dict1 
                         #where m is the number of element in dict2
#Space Complexity = O(n+m)
