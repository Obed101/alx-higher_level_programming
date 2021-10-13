#!/usr/bin/python3
"""Input/output module"""


def read_file(filename=""):
    """reads a txt file and prints it to stdout"""
    file = open(filename, "r")
    print(file.read())
    file.close()
