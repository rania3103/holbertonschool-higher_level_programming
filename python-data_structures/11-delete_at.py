#!/usr/bin/python3
def delete_at(my_list=[], idx=0):
    if idx < 0:
        return (my_list)
    else:
        my_list[-1], my_list[idx] = my_list[idx], my_list[-1]
        my_list = my_list[:-1]
        return (my_list)
my_list = [1, 2, 3, 4, 5]
idx = -1
new_list = delete_at(my_list, idx)
print(new_list)
print(my_list)