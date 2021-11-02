def printer_error(print_string):
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

    error_letter = 0
    i = ''
    for i in print_string:
        if i > 'm':
            error_letter += 1
    return str(error_letter) + '/' + str(len(print_string))


str_inp = input('Введите строку печати принтера: ')
print('Количество ошибок/длина строки', printer_error(str_inp))
