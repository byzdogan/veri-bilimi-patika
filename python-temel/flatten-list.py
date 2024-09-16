# FLATTING A LIST

"""
input: +

output: [1,'a','cat',2,3,'dog',4,5]
"""

import ast

def list_flatter(nested_list):
    flatten_list = []
    for i in nested_list:
        if isinstance(i, list):  # if i is a list
            flatten_list.extend(list_flatter(i))
        else:
            flatten_list.append(i)
    return flatten_list

nested_list = input('Enter the list that you want to be flatten : ')
# turning the input to a list
nested_list = ast.literal_eval(nested_list)
print('input :', nested_list)

flattened_list = list_flatter(nested_list)
print('Flattened list:', flattened_list)

