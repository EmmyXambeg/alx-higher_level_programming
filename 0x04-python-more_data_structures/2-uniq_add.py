#!/usr/bin/python3
def uniq_add(my_list=[]):
    unique_listing = set(my_list)
    addtion = 0

    for i in unique_listing:
        addtion += i

    return (addtion)
