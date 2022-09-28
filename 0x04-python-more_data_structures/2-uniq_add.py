#!/usr/bin/python3
def uniq_add(my_list=[]):
    sum = 0
    unique_list = []
    for item in my_list:
        if item not in unique_list:
            unique_list.append(item)
    for item in unique_list:
        sum += item
    return sum
