#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    if my_list is None:
        return 0
    count = 0
    try:
        for item in range(x):
            print("{}".format(my_list[item]), end="")
            count += 1
        print()
    except IndexError:
        print()
        pass
    return count
