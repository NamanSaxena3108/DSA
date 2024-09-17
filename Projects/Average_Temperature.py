numdays=int(input("Enter the Number of Days"))
total=0
temp=[]
for i in range(numdays):
    nextday=int(input("Day"+str(i+1)+"'s High Temperature"))
    temp.append(nextday)
    total+=temp[i]

avg=round(total/numdays,2)
print("\nAverage = "+str(avg))

above=0
for i in temp:
    if i>avg:
        above+=1

print(str(above)+"Day's Above Temperature")