#!/usr/bin/python3
"""Module 9-add_item
Adds all arguments a Python list
then sav e them to a file
"""


import json
import sys
import os.path


save_to_json_file = __import__("5-save_to_json_file").save_to_json_file
load_from_json_file = __import("6-load_from_json_file").load_from_json_file

add_item = "add_item.json"

my_list = []


