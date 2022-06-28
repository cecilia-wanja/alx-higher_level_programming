#!/usr/bin/python3
"""Defines a text-indentation function."""


def text_indentation(text):
    """Print text with two new lines after each '.', '?', and ':'."""
    if type(text) != str or text is None or len(text) < 0:
        raise TypeError("text must be a string")
    i = 0
    for c in text:
        if c == '?' or c == ':' or c == '.':
            print(c, end="\n\n")
            i = 1
        else:
            if i == 0:
                print(c, end="")
            else:
                if c == ' ' or c == '\t':
                    pass
                else:
                    print(c, end="")
                    i = 0
