#!/usr/bin/python3
def roman_to_int(roman_string):
    sum_total = 0
    ps = False
    rom_num = {
        'I': 1,
        'X': 10,
        'C': 100,
        'M': 1000,
        'V': 5,
        'L': 50,
        'D': 500
        }

    val3 = {'I': 'V', 'X': 'L', 'C': 'D', 'M': None}
    val4 = {'I': 'X', 'X': 'C', 'C': 'M', 'M': None}

    for i, c in enumerate(roman_string):
        if ps:
            ps = False
            continue
        if c in val3.keys():
            if i != len(roman_string) - 1:
                if roman_string[i + 1] == val3[c]:
                    sum_total += rom_num[val3[c]] - rom_num[c]
                    ps = True
                elif roman_string[i + 1] == val4[c]:
                    sum_total += rom_num[val4[c]] - rom_num[c]
                    ps = True
                else:
                    sum_total += rom_num[c]
            else:
                sum_total += rom_num[c]
        else:
            sum_total += rom_num[c]
    return sum_total
