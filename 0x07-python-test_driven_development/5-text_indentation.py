#!/usr/bin/python3
""" this module prints two new lines after it finds '.', '?' or ':' """


def text_indentation(text):
    """This function prints a string with many new lines
    (see module documentation)

    some edge cases:
    >>> text_indentation("name: alx.holberton")
    name:
    $
    alx.
    $
    holberton
    >>>
    """
    if type(text) is not str:
        raise TypeError("text must be a string")
    for a in text:
        print(a.strip(), end='')
        if a == '.' or a == '?' or a == ':':
            print("\n")
