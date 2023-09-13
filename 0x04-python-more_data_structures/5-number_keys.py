#!/usr/bin/python3
def number_keys(a_dictionary):
    counting = 0
    listing_keys = list(a_dictionary.keys())

    for i in listing_keys:
        counting += 1

    return (counting)
