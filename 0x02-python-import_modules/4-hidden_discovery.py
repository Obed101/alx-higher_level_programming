#!/usr/bin/python3
import hidden_4
for fn in dir(hidden_4):
    if fn.startswith('__'):
        continue
    print("{}".format(fn))
