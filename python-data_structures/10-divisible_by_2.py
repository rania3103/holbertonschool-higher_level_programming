#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    if not my_list:
        return
    new = []
    for numb in my_list:
        if numb % 2 == 0:
            new.append(True)
        else:
            new.append(False)
    return (new)
