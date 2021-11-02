"""
Sometimes there are problems: lack of colors, technical malfunction and
a "bad" control string is produced e.g. aaaxbbbbyyhwawiwjjjwwm
with letters not from a to m.
You have to write a function printer_error which given a string
will return the error rate of the printer as a string representing
a rational whose numerator is the number of errors and the denominator
the length of the control string. Don't reduce this fraction to a simpler expression.
Examples:
s="aaabbbbhaijjjm"
printer_error(s) => "0/14"
s="aaaxbbbbyyhwawiwjjjwwm"
printer_error(s) => "8/22"
"""


def printer_error(printer_string):

    error_number = 0
    for i in printer_string:
        if i > 'm':
            error_number += 1
    return str(error_number) + '/' + str(len(printer_string))


str_inp = input()
print(printer_error(str_inp))
