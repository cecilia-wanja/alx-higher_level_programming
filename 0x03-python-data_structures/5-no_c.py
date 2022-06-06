#!/usr/bin/env python3
def no_c(my_string):
    for i in (("c", ""), ("C", "")):
        my_string = my_string.replace(*i)
    return my_string
