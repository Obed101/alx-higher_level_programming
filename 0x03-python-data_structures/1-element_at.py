#!/usr/bin/python3
def element_at(my_list, idx):
    ind = len(my_list) - 1
    if idx < 0:
        return my_list
    elif idx > ind:
        return None
    else:
        return (my_list[idx])
