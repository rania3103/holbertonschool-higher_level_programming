#!/usr/bin/python3
def delete_at(my_list=[], idx=0):
    if idx < 0 or idx >= len(my_list):
        return (my_list)
    elif idx == 0:
        return (my_list[1:])
    elif (idx == len(my_list) - 1):
        return (my_list[:-1])
    else:
        new = my_list.copy()
        new = new[:idx] + new[idx + 1:]
        return (new)
