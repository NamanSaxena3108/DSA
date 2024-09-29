def get_diagonal(tup):
    return tuple(tup[i][i] for i in range(len(tup)))

input_tuple = (
    (1, 2, 3),
    (4, 5, 6),
    (7, 8, 9)
)
output_tuple = get_diagonal(input_tuple)
print(output_tuple)

#Time Complexity = O(n)
#Space Complexity = O(n)