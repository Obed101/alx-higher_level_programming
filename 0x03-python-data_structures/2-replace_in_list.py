#!/usr/bin/python3
def replace_in_list(my_list, idx, element):
    ind = len(my_list) - 1
    if idx < 0 or idx > ind:
        return my_list
    else:
        my_list[idx] = element
        new_list = my_list
        return new_list
