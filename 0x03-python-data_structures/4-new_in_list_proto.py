#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    if idx < 0 or idx > len(my_list):
        origin_list = my_list.copy()
        return origin_list
    else:
        answers = my_list.copy()
        answers[idx] = element
        return answers
