def remove_suplicates(arr):
    new_list=[]
    s=set()
    for i in arr:
        if i not in s:
            new_list.append(i)
            s.add(i)
    return new_list
print(remove_suplicates([1,1,2,2,3,3,4,5]))