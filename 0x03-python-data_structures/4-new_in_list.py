#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    copy_list = my_list.copy()
    for item in my_list:
        if idx < 0:
            return (copy_list)
        elif idx >= len(my_list):
            return (copy_list)
        elif idx == my_list.index(item):
            copy_list[idx] = element
            return (copy_list)
