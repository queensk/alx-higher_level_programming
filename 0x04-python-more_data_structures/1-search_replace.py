#!/usr/bin/python3
def search_replace(my_list, search, replace):
    new_list = []
    i = 0
    for item in my_list:
        if item is search:
            mylist[i] = replace
        i++
    return (new_list)
