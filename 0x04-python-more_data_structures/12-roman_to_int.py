#!/usr/bin/python3
def roman_to_int(roman_string):
    if type(roman_string) != str:
        return 0
    if roman_string is None:
        return 0
    value_map = {"I": 1, "V": 5, "X": 10, "L": 50,
                 "C": 100, "D": 500, "M": 1000}
    value = 0
    last_digit_value = 0
# 1
    for roman_digit in roman_string[::-1]:
        digit_value = value_map[roman_digit]
# 2
        if digit_value >= last_digit_value:
            value += digit_value
            last_digit_value = digit_value
# 3
        else:
            value -= digit_value
    return value

# 1: We iterate the Roman Numeral string backwards ie. [::-1]
# 2: We check if the digit we are currently looking at is larger
# than the digit we have looked at before.
# If it is, we can just add the value we read from our map
# 3: If the current digit has a smaller value than the last one,
# we know that we deal with the special case of not repeating a symbol
# more than three times. In this case
# we must substract the value from our
# result and must not update the last_digit_value
