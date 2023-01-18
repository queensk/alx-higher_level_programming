#!/usr/bin/python3
def no_c(my_string):
    list_string = list(my_string)
    for item in list_string:
        if item == "c":
            list_string.remove('c')
        if item == "C":
            list_string.remove('C')
    my_string = "".join(list_string)
    return (my_string)
