#!/usr/bin/python3
"""
script that adds all arguments to a Python list,
and then save them to a file.
"""
import sys
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file


if __name__ == '__main__':

    filename = "add_item.json"

    try:
        arg_list = load_from_json_file(filename)
    except BaseException:
        arg_list = []

    for arg in sys.argv[1:]:
        arg_list.append(arg)

    save_to_json_file(arg_list, filename)
