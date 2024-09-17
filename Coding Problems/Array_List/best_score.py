#this will return the first and second best from the given list
def best_score(arr):
    max1,max2=0,0
    for i in arr:
        if i>max1:
            max2=max1
            max1=i
        elif i>max2 and i!=max1:
            max2=i
    return max1,max2

mylist=[84,85,85,90,85,83,23,45,84,1,2,0]
print(best_score(mylist))