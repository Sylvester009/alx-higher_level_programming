#!/usr/bin/python3

"""
Defines a script that adds all arguments to a Python list
"""


import json
import sys

save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file

arg_extend = len(sys.argv)

try:
    mylist = load_from_json_file('add_item.json')
except FileNotFoundError:
    mylist = []

for i in range(1, arg_extend):
    mylist.append(sys.argv[i])
save_to_json_file(mylist, 'add_item.json')
