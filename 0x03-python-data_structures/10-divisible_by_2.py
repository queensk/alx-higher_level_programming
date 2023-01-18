#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    boolen_list = []
    for i in my_list:
        if i % 2 == 0:
            boolen_list.append(True)
        else:
            boolen_list.append(False)
    return boolen_list
