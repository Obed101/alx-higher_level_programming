#!/usr/bin/python3
"""Module for file input/output"""

import sys
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file

all_args = list(sys.argv[1:])

try:
    initial = load_from_json_file('add_item.json')
except Exception:
    initial = []

initial.extend(all_args)
save_to_json_file(initial, 'add_item.json')
