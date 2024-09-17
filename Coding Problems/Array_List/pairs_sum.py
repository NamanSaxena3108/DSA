def pair_sum(myList,sum):
    result=[]
    for i in range(len(myList)):
        for j in range(i+1,len(myList)):
            if myList[i]+myList[j]==sum:
                result.append(f"{myList[i]}+{myList[j]}")
    return result

ans=pair_sum([2,4,3,5,6,-2,4,7,8,9],7)
print(ans)