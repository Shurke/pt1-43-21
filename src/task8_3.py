def printer_error(s):
    """
    Sometimes there are problems: lack of colors, technical malfunction and
    a "bad" control string is produced e.g. aaaxbbbbyyhwawiwjjjwwm
    with letters not from a to m.
    You have to write a function printer_error which given a string
    will return the error rate of the printer as a string representing
    a rational whose numerator is the number of errors and the denominator
    the length of the control string. Don't reduce this fraction to a simpler expression.
    """
    k = 0
    i = ''
    for i in s:
        if i > 'm':
            k += 1
    return str(k) + '/' + str(len(s))


str_inp = input()
print(printer_error(str_inp))
