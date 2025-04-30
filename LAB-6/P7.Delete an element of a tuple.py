'''
7.	Delete an element of a tuple
'''
my_tuple = (1, 2, 3, 4)
element_to_remove = 2
modified_tuple = tuple(x for x in my_tuple if x != element_to_remove)
print(f"Tuple after removing element {element_to_remove}: {modified_tuple}")