#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    get_keys = list(a_dictionary.keys())

    for values_of_keys in get_keys:
        if value == a_dictionary.get(values_of_keys):
            del a_dictionary[values_of_keys]

    return (a_dictionary)
