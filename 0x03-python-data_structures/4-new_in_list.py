#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    temporary_list = my_list[:]
    if idx < 0 or idx > len(my_list) - 1:
        return temporary_list
    else:
        new_list = my_list.copy()
        new_list[idx] = element
        return new_list
