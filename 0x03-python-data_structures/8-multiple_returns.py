#!/usr/bin/python3
def multiple_returns(sentence):
    if len(sentence) > 0:
        stat = (len(sentence), sentence[0])
    else:
        sentence[0] = None
    return stat
