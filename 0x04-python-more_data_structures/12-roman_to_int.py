#!/usr/bin/python3
def to_subtract_a(list_num):
    to_sub_a = 0
    max_list_a = max(list_num)

    for n in list_num:
        if max_list_a > n:
            to_sub_a += n
    return (max_list_a - to_sub_a)


def roman_to_int(roman_string):
    if not roman_string:
        return 0

    if not isinstance(roman_string, str):
        return 0

    roman_num = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M':1000}
    get_keys = list(roman_num.keys())

    num_a = 0
    last_rom_a = 0
    list_num_a = [0]

    for char in roman_string:
        for r_num in get_keys:
            if r_num == char:
                if roman_num.get(char) <= last_rom_a:
                    num_a += to_subtract_a(list_num_a)
                    list_num_a = [roman_num.get(char)]
                else:
                    list_num_a.append(roman_num.get(char))
                last_rom_a = roman_num.get(char)
    num_a += to_subtract_a(list_num_a)
    return (num_a)
