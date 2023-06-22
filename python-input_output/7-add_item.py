#!/usr/bin/python3
"""adds all arguments to a Python list,
    and then save them to a file.

    tests:
    ./7-add_item.py
    ./7-add_item.py Best School
    ./7-add_item.py 89 Python C

    cat add_item.json ; echo ""
    ["Best", "School", "89", "Python", "C"]
    """

import json
import sys

save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file

if __name__ == "__main__":
    try:
        JSON_list = load_from_json_file('add_item.json')
    except FileNotFoundError:
        JSON_list = []

    for i in range(1, len(sys.argv)):
        JSON_list.append(sys.argv[i])

    save_to_json_file(JSON_list, "add_item.json")
