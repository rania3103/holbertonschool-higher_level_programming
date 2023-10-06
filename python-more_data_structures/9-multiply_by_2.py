#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    new = a_dictionary.copy()
    for k, v in new.items():
        new[k] *= 2
    return (new)
