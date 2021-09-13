#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    lists = my_list[::-1]
    listln = len(my_list)
    for i in range(listln):
        print("{}".format(lists[i]), end="\n")
