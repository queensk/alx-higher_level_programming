#!/usr/bin/python3
new_in_list = __import__('4-new_in_list').new_in_list

my_list = [1, 2, 3, 4, 5]
idx = 3
new_elements = 9
new_list = new_in_list(my_list, idx, new_elements)

print(new_list)
print(my_list)
