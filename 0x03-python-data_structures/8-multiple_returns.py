#!/usr/bin/python3
def multiple_returns(sentence):
    if len(sentence) > 0:
        stat = (len(sentence), sentence[0])
    else:
        stat = None
    return stat
