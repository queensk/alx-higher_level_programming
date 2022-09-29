#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    copy_dict = a_dictionary.copy()
    try:
        for key in copy_dict:
            if value == a_dictionary[key]:
                del a_dictionary[key]
        return (a_dictionary)
    except KeyError:
        return (a_dictionary)
