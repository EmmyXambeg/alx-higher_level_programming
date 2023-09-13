#!/usr/bin/python3
def weight_average(my_list=[]):
    if not my_list:
        return 0

    weighted_score_add = 0
    frequency_add = 0

    for tup in my_list:
        weighted_score_add += tup[0] * tup[1]
        frequency_add += tup[1]

    return (weighted_score_add / frequency_add)
