#!/usr/bin/python3
def uniq_add(my_list=[]):
    if my_list == None:
        return
    mlist = set(my_list)
    result = 0
    for n in mlist:
        result += n
    return result
