#!/usr/bin/python3
def delete_at(my_list=[], idx=0):
    temp_list = my_list.copy()
    if idx < 0 or idx > len(my_list) - 1:
        return my_list
    else:
        my_list = temp_list[:idx] + temp_list[idx + 1:]
        return my_list
