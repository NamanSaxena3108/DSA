#Searching
l=[10,20,30,40,50,60,70,80,90]
#in operator
tar=50
if tar in l:
    print("Present")
else:
    print("Not present")

#Linear Search
def linear_search(p_list,p_tar):
    for i,value in enumerate(p_list):
        if value==p_tar:
            return 1
    return -1
print(linear_search(l,tar))