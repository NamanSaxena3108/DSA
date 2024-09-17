#operation/Function
t=(1,4,3,2,5)
t1=(1,2,6,9,8,7)

#Concatination
print(t+t1)          #(1, 4, 3, 2, 5, 1, 2, 6, 9, 8, 7)

#Repetition
print(t*4)          #(1, 4, 3, 2, 5, 1, 4, 3, 2, 5, 1, 4, 3, 2, 5, 1, 4, 3, 2, 5)

#In operator
print(3 in t)          #True

#Count
print(t.count(2))          #1

#Index
print(t.index(4))          #1

#Length
print(len(t))          #5

#Max
print(max(t))          #5

#Min
print(min(t))          #1

#Conversion
print(tuple([1,2,3,4]))          #(1, 2, 3, 4)