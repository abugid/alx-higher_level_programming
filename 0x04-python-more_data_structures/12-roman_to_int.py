#!/usr/bin/python3

def roman_to_int(roman_string):
    roman_num = {
        "I": 1,
        "V": 5,
        "X": 10,
        "L": 50,
        "C": 100,
        "D": 500,
        "M": 1000
    }
    if (roman_string is None or type(roman_string) != str):
        return 0
    total = 0
    for char in roman_string:
        try:
            total += roman_num[char]
        except KeyError:
            return 0

    return total
