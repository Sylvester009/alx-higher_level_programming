#!/usr/bin/python3
def to_subtract(list_num):
    subtract = 0
    maxList = max(list_num)

    for i in list_num:
        if maxList > i:
            subtract += i

    return (maxList - subtract)


def roman_to_int(roman_string):
    if not roman_string or not isinstance(roman_string, str):
        return 0

    roman_num = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    keys_list = list(roman_num.keys())

    num = 0
    last_roman = 0
    list_num = [0]

    for j in roman_string:
        for i in keys_list:
            if i == j:
                if roman_num[j] <= last_roman:
                    num += to_subtract(list_num)
                    list_num = [roman_num[j]]
                else:
                    list_num.append(roman_num[j])

                last_roman = roman_num[j]

    num += to_subtract(list_num)

    return num
