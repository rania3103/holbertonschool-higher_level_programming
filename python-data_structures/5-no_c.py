#!/usr/bin/python3
def no_c(my_string):
    for ch in my_string:
        if ch.upper() == 'C':
            my_string = my_string.replace(ch, '')
    return (my_string)
