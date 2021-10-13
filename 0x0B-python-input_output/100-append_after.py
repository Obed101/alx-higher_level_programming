#!/usr/bin/python3
"""Find and insert"""


def append_after(filename="", search_string="", new_string=""):
    """inserts some text after finding a particular text"""
    with open(filename, 'r') as f:
        lines = f.readlines()

    with open(filename, 'r') as f:
        new_lines = []
        for i in range(len(lines)):
            new_lines.append(lines[i])
            if search_string in lines[i]:
                new_lines.append(new_string)
        f.writelines(new_lines)
