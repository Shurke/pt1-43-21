def persistence(my_digit):
    # Write a function, persistence, that takes in a positive parameter num
    # and returns its multiplicative persistence, which
    # is the number of times you must multiply the digits
    # in num until you reach a single digit
    #
    # Examples:
    #     persistence(39) === 3 // because 3*9 = 27, 2*7 = 14, 1*4=4
    #                    // and 4 has only one digit
    #     persistence(999) === 4 // because 9*9*9 = 729, 7*2*9 = 126,
    #                     // 1*2*6 = 12, and finally 1*2 = 2
    #     persistence(4) === 0 // because 4 is already a one-digit number

    def get_digit(dgt):
        s = 1
        while dgt > 0:
            s *= dgt % 10
            dgt //= 10
        return s

    if my_digit // 10 == 0:
        return 0
    else:
        nmb_times = 0
        while my_digit // 10 > 0:
            my_digit = get_digit(my_digit)
            nmb_times += 1
        return nmb_times


k = int(input('Введите число: '))
print('Количество умножений цифр числа до получения однозначного числа: ', persistence(k))
