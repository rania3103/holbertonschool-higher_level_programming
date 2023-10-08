#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    try:
        for i in range(x):
            print(my_list[i], end="")
        print()
        return x
    except BaseException:
        list_len = sum(1 for i in my_list)
        print()
        return list_len
