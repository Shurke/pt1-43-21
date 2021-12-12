"""
    Оформите решение задач из прошлых домашних работ в функции.
    Напишите функцию runner. (все станет проще когда мы изучим
    модули, getattr и setattr)

        a. runner() – все фукнции вызываются по очереди
        b. runner(‘func_name’) – вызывается только функцию func_name.
        c. runner(‘func’, ‘func1’...) - вызывает все переданные функции

    Homework2
"""


def task2_1():
    """Подсчет общей цены."""

    rub = int(input('Введите количество рублей в цене товара: '))
    kop = int(input('Введите количество копеек в цене товара: '))
    items = int(input('Введите количество товара: '))
    rub_total = rub * items + (kop * items) // 100
    kop_total = (kop * items) % 100
    print('Общая стоимость товара: ', rub_total, ' рублей ', kop_total, ' копеек')
    return


def task2_2():
    """Самое длинное слово."""

    import string

    my_string = input('Введите предложение: ')
    my_string_wo_punctuation = ''
    for i in my_string:
        if i in string.punctuation:
            my_string_wo_punctuation += ' '
        else:
            my_string_wo_punctuation = my_string_wo_punctuation + i
    max_len_word = max(my_string_wo_punctuation.split(), key=len)
    print('Самое длинное слово:', max_len_word)
    return


def task2_3():
    """Удалить повторяющиеся символы."""

    my_string = input('Введите строку: ')
    my_string_out = ''
    for i in my_string:
        if i not in my_string_out and i != ' ':
            my_string_out += i
    print('Строка без повторяющихся символов: ', my_string_out)
    return


def task2_4():
    """Количество строчных и прописных букв."""

    my_string = input('Введите строку: ')
    lower_letter = 0
    upper_letter = 0
    for i in my_string:
        if i.islower():
            lower_letter += 1
        elif i.isupper():
            upper_letter += 1
    print('Строчных букв в строке:', lower_letter)
    print('Прописных букв в строке:', upper_letter)
    return


def task2_5():
    """N-ое число Фибоначчи."""

    number_fib = int(input('Введите номер числа Фибоначчи: '))
    previous_number = 0
    current_number = 1
    i = 3
    while i <= number_fib:
        temp_number = current_number
        current_number = current_number + previous_number
        previous_number = temp_number
        i += 1
    if number_fib == 0:
        print('Неверно введен номер числа')
    elif number_fib == 1:
        print(number_fib, 'число Фибоначчи: 0')
    else:
        print(number_fib, 'число Фибоначчи:', current_number)
        return


def task2_6():
    """Поиск палиндрома числа."""

    my_number = int(input('Введите число: '))
    invert_my_number = 0
    reminder = my_number
    while reminder > 0:
        invert_my_number = invert_my_number * 10 + reminder % 10
        reminder = reminder // 10
    if my_number == invert_my_number:
        print('Число', my_number, 'палиндром')
    else:
        print('Число', my_number, 'не палиндром')
    return


def task2_7():
    """Определение площади треугольника."""

    tri_str = input('Введите три стороны треугольника (через запятые):').split(',')
    tri = [int(i) for i in tri_str]
    tri.sort(reverse=True)  # Сортировка по длине сторон
    if tri[0] >= tri[1] + tri[2]:  # Условие не существования треугольника
        print('Неверные длины сторон')
    else:
        p = 0
        for i in tri:
            p += i
        p /= 2
        # Формула Герона
        s = (p * (p - tri[0]) * (p - tri[1]) * (p - tri[2])) ** 0.5
        print('Площадь треугольника', s)
    return


def task2_8_1():
    """Создание убывающего списка."""

    def reverse_seq(n):
        s = []
        i = n
        while i > 0:
            s.append(i)
            i -= 1
        return s

    n_1 = int(input('Введите количество элементов списка: '))
    print('Убывающий список: ', reverse_seq(n_1))
    return


def task2_8_2():
    """Перемножение цифр числа."""

    def persistence(my_digit):

        """Multiplicative persistence.

        Write a function, persistence, that takes in a positive parameter num
        and returns its multiplicative persistence, which
        is the number of times you must multiply the digits
        in num until you reach a single digit

        Examples:
            persistence(39) === 3 // because 3*9 = 27, 2*7 = 14, 1*4=4
                           // and 4 has only one digit
            persistence(999) === 4 // because 9*9*9 = 729, 7*2*9 = 126,
                            // 1*2*6 = 12, and finally 1*2 = 2
            persistence(4) === 0 // because 4 is already a one-digit number

        """

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


def task2_8_3():
    """Подсчет ошибок принтера."""

    def printer_error(printer_string):

        """Подсчет ошибок принтера.

        Примеры:
        s="aaabbbbhaijjjm"
        printer_error(s) => "0/14"
        s="aaaxbbbbyyhwawiwjjjwwm"
        printer_error(s) => "8/22"

        """

        error_number = 0
        for i in printer_string:
            if i > 'm':
                error_number += 1
        return str(error_number) + '/' + str(len(printer_string))

    str_inp = input('Введите строку из строчных букв: ')
    print('Количество ошибок/длина строки: ', printer_error(str_inp))
    return


def task2_8_4():
    """Поиск числа, которое отличается по четности от остальных."""

    def iq_test(numbers):

        """Поиск числа, которое отличается по четности от остальных.

        Examples:
        iq_test("2 4 7 8 10") => 3 # Third number is odd, while the rest of the numbers are even
        iq_test("1 2 1 1") => 2 # Second number is even, while the rest of the numbers are odd

        """

        numb = [int(i) for i in numbers.split()]
        evn = []
        odd = []
        for i in range(len(numb)):
            if numb[i] % 2 == 0:
                evn.append(i + 1)
            else:
                odd.append(i + 1)
        if len(evn) > 1:
            return odd[0]
        else:
            return evn[0]

    numb_str = input('Введите строку из чисел: ')
    print('Число, которое отличается от остальных по четности: ', iq_test(numb_str))
    return


def task2_8_5():
    """Проверка правильности и длины PIN кода."""

    def validate_pin(pin):

        """Проверка правильности и длины PIN кода.

        ATM machines allow 4 or 6 digit PIN codes and PIN codes cannot contain
        anything but exactly 4 digits or exactly 6 digits.
        If the function is passed a valid PIN string, return true, else return false.

        """

        if pin.isdigit() and (len(pin) == 4 or len(pin) == 6):
            return True
        else:
            return False

    str_pin = input()
    print(validate_pin(str_pin))
    return
