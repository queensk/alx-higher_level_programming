#!/usr/bin/python3
def roman_to_int(roman_string):
    if roman_string is None or type(roman_string) is not str:
        return (0)
    
    roman = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
    number_list = [roman[i] for i in roman_string.upper() if i in roman]
    return sum([i if i >= number_list[min(j+1, len(number_list)-1)] else -i for j, i in enumerate(number_list)])
