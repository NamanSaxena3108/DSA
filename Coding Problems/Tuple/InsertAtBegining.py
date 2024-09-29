def insert_value_front(input_tuple, value_to_insert):
    temp=(value_to_insert,)
    new_tuple=temp+input_tuple
    return new_tuple
    
input_tuple = (2, 3, 4)
value_to_insert = 1
output_tuple = insert_value_front(input_tuple, value_to_insert)
print(output_tuple)  

#Time Complexity = O(n)
#Space Complexity = O(n)