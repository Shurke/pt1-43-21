'''
Given an array of ones and zeroes,
convert the equivalent binary value to an integer.
Eg: [0, 0, 0, 1] is treated as 0001 which is
the binary representation of 1.
'''

arr = [0, 1, 0, 1]


def binary_array_to_number(arr):
    n = 1
    decimal_number = 0
    for number in arr:
        decimal_number = decimal_number + number * 2 ** (len(arr) - n)
        n += 1
    return decimal_number


print(binary_array_to_number(arr))
