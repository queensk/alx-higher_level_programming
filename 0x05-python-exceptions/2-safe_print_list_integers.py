#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    if my_list is None:
        return 0
    count = 0
    for item in range(x):
        try:
            print("{:d}".format(my_list[item]), end="")
            count += 1
        except (ValueError, TypeError):
            pass
    print()
    return count
