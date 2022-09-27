#!/usr/bin/python3
def replace_in_list(my_list, idx, element):
    for item in my_list:
        if idx < 0:
            return (my_list)
        elif idx >= len(my_list):
            return (my_list)
        elif idx == my_list.index(item):
            my_list.pop(idx)
            my_list.insert(idx, element)
