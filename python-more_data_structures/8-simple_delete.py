#!/usr/bin/python3
def simple_delete(a_dictionary, key=""):
    if key not in a_dictionary.keys():
        return
    else:
        del (a_dictionary[key])