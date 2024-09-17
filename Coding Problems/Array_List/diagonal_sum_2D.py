def diagonal_sum(matrix):
    total=0
    for i in range(len(matrix)):
        total+=matrix[i][i]
    return total
myList2D=[[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]]
print(diagonal_sum(myList2D))