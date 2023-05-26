#!/usr/bin/python3
def roman_to_int(roman_string):
    if roman_string is None or type(roman_string) is not str:
        return (0)
    rom_dict = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100,
                'D': 500, 'M': 1000}
    roman_list = list(roman_string.upper())
    res = 0
    prev = 0
    for let in roman_list:
        if let in rom_dict:
            res += rom_dict[let]
            if rom_dict[let] > prev:
                res -= prev * 2
            prev = rom_dict[let]
        else:
            return (0)
    return (res)
