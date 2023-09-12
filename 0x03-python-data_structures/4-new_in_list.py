#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    new_listing = my_list[:]
    if 0 <= idx < len(my_list):
        new_listing[idx] = element
    return new_listing
