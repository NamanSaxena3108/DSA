def concatenate_strings(input_tuple):
    return ' '.join(input_tuple)

input_tuple   = ('Hello', 'World', 'from', 'Python')
output_string = concatenate_strings(input_tuple)
print(output_string)

#Time Complexity = O(n)
#Space Complexity = O(n)