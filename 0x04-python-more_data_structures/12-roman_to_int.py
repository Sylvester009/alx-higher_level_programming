#!/usr/bin/python3
def to_subtract(list_num):
    subtract = 0
    maxList = max(list_num)

    for i in list_num:
        if maxList > i:
            subtract += i

    return (maxList - subtract)


def roman_to_int(roman_string):
    if not roman_string:
        return 0

    if not isinstance(roman_string, str):
        return 0

    roman_num = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    keys_list = list(roman_num.keys())

    num = 0
    last_roman = 0
    list_num = [0]

    for j in roman_string:
        for rom_num in keys_list:
            if rom_num == i:
                if roman_num.get(j) <= last_roman:
                    num += to_subtract(list_num)
                    list_num = [roman_num.get(j)]
                else:
                    list_num.append(roman_num.get(j))

                last_roman = roman_num.get(j)

    num += to_subtract(list_num)

    return (num)
