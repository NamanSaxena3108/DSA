pre=[1,2,3]
new_list=[i*2 for i in pre]
print(new_list)

lang="Python"
new_list1=[letter for letter in lang]
print(new_list1)

#Conditional
pre1=[-1,10,-20,2,-90,60,45,20]
new_list2=[num for num in pre1 if num>0]
print(new_list2)

new_list3=[num if num>0 else 'Negative Number' for num in pre1]
print(new_list3)