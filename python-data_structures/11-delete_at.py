#!/usr/bin/python3
def delete_at(my_list=[], idx=0):
    if idx < 0 or idx >= len(my_list):
        return (my_list)
    else:
        new = my_list.copy()
        new[-1], new[idx] = new[idx], new[-1]
        return (new[:-1])
