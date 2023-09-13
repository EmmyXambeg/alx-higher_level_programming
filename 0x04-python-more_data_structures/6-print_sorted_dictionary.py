#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    list_of_dict_keys = list(a_dictionary.keys())
    list_of_dict_keys.sort()

    for i in list_of_dict_keys:
        print(f"{i}: {a_dictionary.get(i)}")
