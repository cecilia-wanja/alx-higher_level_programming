#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    new = []
    for key, key_value in a_dictionary.items():
        if key_value is value:
            new.append(key)
    for x in new:
        del a_dictionary[x]
    return(a_dictionary)
