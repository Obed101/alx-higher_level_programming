#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    list = my_list[::-1]
    listln = len(my_list) - 1
    for i in range(listln):
        list = int(list)
        print("{}".format(list[i]), end="\n")
