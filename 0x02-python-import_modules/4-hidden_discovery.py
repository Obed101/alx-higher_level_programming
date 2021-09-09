#!/usr/bin/python3
import sys
for fn in dir(sys):
    if fn.startswith('__'):
        continue
    print("{}".format(fn))
