# REVERSE LIST ITEMS
"""
input: [[1, 2], [3, 4], [5, 6, 7]]

output: [[[7, 6, 5], [4, 3], [2, 1]]
"""

import ast

def reverse_list_elements(list_input):
    reversed_list = []
    for i in list_input:
        if isinstance(i, list):
            reversed_list.append(reverse_list_elements(i)) 
        else:
            reversed_list.append(i)
    # reversed_list.reverse() or reversed_list[::-1]
    return reversed_list[::-1]


list_input = input('Enter the list that you want its items to be reversed : ')
# turning the input to a list
list_input = ast.literal_eval(list_input)
print('input :', list_input)

reversed_list = reverse_list_elements(list_input)
print('Reversed list:', reversed_list)