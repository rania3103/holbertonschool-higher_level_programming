#!/usr/bin/python3
def roman_to_int(roman_string):
    if not roman_string or not isinstance(roman_string, str):
        return 0
    roman_num = {
        'I': 1,
        'V': 5,
        'X': 10,
        'L': 50,
        'C': 100,
        'D': 500,
        'M': 1000}

    tot = 0
    for i in range(len(roman_string)):
        if roman_string[i] in roman_num.keys():
            if i == len(roman_string) - 1:
                tot += roman_num.get(roman_string[i])
            else:
                if roman_num[roman_string[i]
                             ] >= roman_num[roman_string[i + 1]]:
                    tot += roman_num.get(roman_string[i])
                else:
                    tot -= roman_num.get(roman_string[i])
    return tot
