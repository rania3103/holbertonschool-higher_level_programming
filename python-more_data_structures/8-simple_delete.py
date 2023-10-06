#!/usr/bin/python3
def simple_delete(a_dictionary, key=""):
    if key not in a_dictionary.keys():
        return
    else:
        a_dictionary.pop(key, None)
        return (a_dictionary)
