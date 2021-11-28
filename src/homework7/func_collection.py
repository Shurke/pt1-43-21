''' 1. Напишите программу, которая считает общую цену.
Вводится M рублей и N копеек цена, а также количество S товара Посчитайте
общую цену в рублях и копейках за L товаров.
Пример:
Input: Цена одной вещи 3 рубля 20 копеек, посчитать 3 предмета.
Output: Общая цена 9 рублей 60 копеек
'''


def total_value_of_goods(cost_rubles=1, cost_copecks=10, quantity=1):
    '''Вводится M рублей и N копеек цена, а также количество S товара.

    Выводит общую стоимость в рублях и копейках
    '''

    while not cost_rubles.isnumeric():
        print('Please enter a positive number.')
        cost_rubles = input('Enter the cost, rubles - ')
    else:
        print('Thanks!')

    while not cost_copecks.isnumeric() or int(cost_copecks) > 99:
        print('Please enter a positive number from 0 to 99')
        cost_copecks = input('Enter the cost, copecks - ')
    else:
        print('Thanks!')

    print('Cost of one item is - ' + cost_rubles + ' rubles ' + cost_copecks + ' copecks')

    while not quantity.isnumeric():
        print('Please enter a positive number.')
        quantity = input('Enter the quantity - ')
    else:
        print('Thanks!')

    print('Wait for it...')

    cost_rubles = int(cost_rubles)
    cost_copecks = int(cost_copecks)
    quantity = int(quantity)

    value_copecks = (cost_rubles * 100 + cost_copecks) * quantity
    rubles_part = value_copecks // 100  # Total value, rubles
    copecks_part = value_copecks % 100  # Total value, copecks
    result = print('Total value: ' + str(rubles_part) + ' rubles ' +
                   str(copecks_part) + ' copecks.')
    return result


''' 2. Найти самое длинное слово в введенном предложении.
Учтите что в предложении есть знаки препинания.
'''


def longest_word(entered_text='Longest word'):
    '''Находит самое длинное слово во введенном предложении.

    Учитывает наличие знаков препинания.
    '''

    import string

    stripped = entered_text.translate(str.maketrans('', '', string.punctuation))
    entered_text = stripped.split(' ')

    max_lenght = 0
    longest_word = ''
    for word in entered_text:
        if len(word) > max_lenght:
            max_lenght = len(word)
            longest_word = word

    result = print('Result of longest_word function is - ' + longest_word)
    return result


''' 3. Вводится строка. Требуется удалить из нее повторяющиеся символы и все пробелы.
Например, если было введено "abc cde def", то должно быть выведено "abcdef".
'''


def unique_string(entered_string='abrakadabra'):
    '''На ввод - строка.

    Вывод - строка без пробелов и повторяющихся символов
    '''

    str_no_space = entered_string.replace(' ', '')
    unique_string = str_no_space[0]
    for letter in str_no_space:
        if letter not in unique_string:
            unique_string += letter

    return print(unique_string)


''' 4. Посчитать количество строчных (маленьких) и прописных (больших) букв в введенной строке.
Учитывать только английские буквы.
'''


def counter_low_up_words(entered_symbols='sdsdFSFSFDFdfsdfsfsdf fsdsf'):
    '''Вводится строка.

    Считает кол-во строчных и прописных англ. букв в ней.
    '''

    lowercased_words = 0
    uppercase_words = 0

    for symbol in entered_symbols:
        if symbol.isupper():
            uppercase_words += 1
        elif symbol.islower():
            lowercased_words += 1

    result_low = 'Quantity of lowercase English letters is ' + str(lowercased_words)
    result_up = 'Quantity of uppercase English letters is ' + str(uppercase_words)
    return print(result_low, result_up)


'''
5. Выведите n-ое число Фибоначчи, используя только временные переменные,
циклические операторы и условные операторы.
n - вводится
'''


def fib_number(number_in_fib=1):
    '''Выводится n-ое число Фибоначчи'''

    if 2 <= number_in_fib <= 3:
        fib_element = 1
    elif number_in_fib == 1:
        fib_element = 0
    else:
        fib_element = 2
        fib_element_left = 1
        for element in range(4, number_in_fib):
            fib_element_left, fib_element = fib_element, fib_element_left + fib_element

    counter = number_in_fib

    while counter > 0:
        last_number = counter % 10
        counter //= 10

    if last_number == 1:
        result = print(str(number_in_fib) + 'st Fibonacci number is - ' + str(fib_element))
    elif last_number == 2:
        result = print(str(number_in_fib) + 'nd Fibonacci number is - ' + str(fib_element))
    elif last_number == 3:
        result = print(str(number_in_fib) + 'rd Fibonacci number is - ' + str(fib_element))
    else:
        result = print(str(number_in_fib) + 'th Fibonacci number is - ' + str(fib_element))
    return result


''' 6. Определите, является ли число палиндромом (читается слева направо и справа налево одинаково).
Число положительное целое, произвольной длины. Задача требует работать только с числами
(без конвертации числа в строку или что-нибудь еще)
'''


def polindrome_test_num(entered_number=222):
    '''Определяет, является ли введенное число палиндромом'''

    reversed_number = 0
    counter = entered_number

    while counter > 0:
        last_number = counter % 10
        reversed_number = 10 * reversed_number + last_number
        counter //= 10

    if entered_number == reversed_number:
        result = print('It is polindrome!')
    else:
        result = print('It is not polindrome(')
    return result


''' 7. Даны: три стороны треугольника.
Требуется: проверить, действительно ли это стороны треугольника.
Если стороны определяют #треугольник, найти его площадь.
Если нет, вывести сообщение о неверных данных.
'''


def triangle_test(side_a, side_b, side_c):
    '''Определяет, существует ли треугольник по 3м сторонам.

    Если да - вычисляет его площадь.
    '''

    if (side_a < side_b + side_c) and (side_b < side_a + side_c) and (side_c < side_a + side_b):
        half_p = (side_a + side_b + side_c) / 2

        # Формула Герона для площади треугольника
        triangle_square = (
            (half_p * ((half_p - side_a) * (half_p - side_b) * (half_p - side_c))) ** 0.5
        )
        result = print('Площадь треугольника: ' + str(triangle_square))
    else:
        result = print('Треугольника с заданными сторонами не существует.')
    return result


'''
here is an array with some numbers.
All numbers are equal except for one.
Try to find it!
It’s guaranteed that array contains at least 3 numbers.
The tests contain some very huge arrays, so think about performance. Done
'''


def find_uniq(list_sample=[0, 0, 0, 0.55, 0, 0, 0, 0, 0]):
    '''Finds unique number in entered array'''

    list_sample.sort()

    if list_sample[1] == list_sample[0]:
        unique_number = list_sample[-1]
    else:
        unique_number = list_sample[0]

    return print(unique_number)   # n: unique integer in the array


'''
If we list all the natural numbers below 10 that are multiples of 3 or 5,
we get 3, 5, 6 and 9. The sum of these multiples is 23.
Finish the solution so that it returns the sum of all the multiples
of 3 or 5 below the number passed in. Additionally, if the #number is negative,
return 0 (for languages that do have them).
Note: If the number is a multiple of both 3 and 5, only count it once.
'''


def solution(number):
    '''Enter number.

    Returns the sum of all the multiples
    of 3 or 5 below the number passed in
    '''

    sum_of_multiples = 0
    for i in range(number):
        if i % 3 == 0 or i % 5 == 0:
            sum_of_multiples += i

    return print(sum_of_multiples)


'''
Define a function that takes one integer argument and returns
logical value true or false depending on if the integer is a prime.
Per Wikipedia, a prime number (or a prime) is a natural number
greater than 1 that has no positive divisors other than 1 and itself.
Requirements
You can assume you will be given an integer input.
You can not assume that the integer will be only positive.
You may be given negative numbers as well (or 0).
'''


def is_prime(num):
    '''Принимает число.

    Выводит true, если число простое False, если нет
    '''

    prime_flag = True if num > 1 else False
    for i in range(2, num - 1):
        if num % i != 0:
            prime_flag = True
        else:
            prime_flag = False
        break

    return print('The num is prime?', prime_flag)


'''
Write a function that takes in a string of one or more words,
and returns the same string, but with all five or more letter
words reversed (like the name of this kata).
Strings passed in will consist of only letters and spaces.
Spaces will be included only when more than one word is present.
'''


def spin_words(sentence='It takes in a string of one or more words'):
    '''It takes in a string of one or more words.

    Returns the same string, but with all five or more letter words reversed
    '''

    sentence = sentence.split(' ')
    string_result = ''

    for word in sentence:
        if len(word) >= 5:
            string_result = string_result + word[::-1] + ' '
        else:
            string_result = string_result + word + ' '

    string_result = string_result.strip(' ')
    return print(string_result)


'''
Given an array of ones and zeroes,
convert the equivalent binary value to an integer.
Eg: [0, 0, 0, 1] is treated as 0001 which is
the binary representation of 1.
'''


def binary_array_to_number(arr=[0, 1, 0, 1]):
    """Given an array of ones and zeroes,

    convert the equivalent binary value to an integer.
    """

    n = 1
    decimal_number = 0
    for number in arr:
        decimal_number = decimal_number + number * 2 ** (len(arr) - n)
        n += 1
    return print(decimal_number)


'''
FizzBuzz
Напишите программу, которая печатает цифры от 1 до 100, но вместо чисел,
кратных 3 пишет Fizz, вместо чисел кратный 5 пишет Buzz,
а вместо чисел одновременно кратных и 3 и 5 - FizzBuzz
'''


def fizz_buzz_printer(a=1, b=101):
    '''Печатает цифры от a до b.

    Но вместо чисел, кратных 3 пишет Fizz, вместо чисел кратный 5 пишет Buzz,
    а вместо чисел одновременно кратных и 3 и 5 - FizzBuzz
    '''

    for i in range(a, b):
        if i % 3 == 0 and i % 5 == 0:
            print('FizzBuzz')
        elif i % 3 == 0:
            print('Fizz')
        elif i % 5 == 0:
            print('Buzz')
        else:
            print(i)


'''
List practice
1. Используйте генератор списков чтобы получить следующий: ['ab', 'ac', 'ad', 'bb', 'bc', 'bd'].
2. Используйте на предыдущий список slice чтобы получить следующий: ['ab', 'ad', 'bc'].
3. Используйте генератор списков чтобы получить следующий ['1a', '2a', '3a', '4a'].
4. Одной строкой удалите элемент  '2a' из прошлого списка и напечатайте его.
5. Скопируйте список и добавьте в него элемент '2a' так чтобы в исходном списке
этого элемента не было.
'''


def task2_hw3(a=['a', 'b'], b=['b', 'c', 'd']):

    lst_from1 = [(first_list + second_list) for first_list in a
                 for second_list in b]
    print(lst_from1)

    print(lst_from1[::2])

    lst_from3 = [digit + word for digit in ['1', '2', '3', '4'] for word in 'a']
    print(lst_from3)

    print(lst_from3.pop(1))

    lst_from5 = lst_from3.copy()
    lst_from5.insert(1, '2a')
    print(lst_from5)


'''
Tuple practice
Создайте кортеж из одного элемента, чтобы при итерировании по этому элементу
последовательно выводились значения 1, 2, 3. Убедитесь что len() исходного кортежа возвращает 1.
'''


def tuple_practice(tuple_sample=[1, 2, 3],):
    '''Итерирует по первому элементу кортежа, последовательно выводя значения'''

    for item in tuple_sample:
        for i in item:
            print(i)


'''
Пары элементов
Дан список чисел. Посчитайте, сколько в нем пар элементов, равных друг другу.
Считается, что любые два элемента, равные друг другу образуют одну пару,
которую необходимо посчитать.
Входные данные - строка из чисел, разделенная пробелами.
Выходные данные - количество пар.
Важно: 1 1 1 - это 3 пары, 1 1 1 1 - это 6 пар
'''


def pair_counter(number_input='1 1 1 1'):
    '''Считает количество пар чисел в строке, равных друг другу'''

    import math

    number_input = number_input.replace(' ', '')
    counted_numbers = []
    pair_counter = 0

    for item in number_input:
        if item not in counted_numbers:
            element_counter = number_input.count(item)

            # Находим количетсво пар через сочетания
            pair_counter += math.factorial(element_counter) \
                // (2 * math.factorial(element_counter - 2))

            counted_numbers.append(item)  # Убираем числа, для которых пары посчитаны

    return print(pair_counter)  # Количество пар элементов равных друг другу


'''
Уникальные элементы в списке
Дан список. Выведите те его элементы, которые встречаются в списке только один раз.
Элементы нужно выводить в том порядке, в котором они встречаются в списке.
'''


def unique_element_in_list(list_sample=[1, 1, 2, 3, 4, 3, 5, 5, 6]):
    '''Выводит элементы списка, которые встречаются в нем только один раз'''

    for i in list_sample:
        if list_sample.count(i) == 1:
            print(f'Уникальный элемент в списке - {i}')


'''
Дан список целых чисел. Требуется переместить все ненулевые элементы в левую часть списка,
не меняя их порядок, а все нули - в правую часть. Порядок ненулевых элементов изменять нельзя,
дополнительный список использовать нельзя, задачу нужно выполнить за один проход по списку.
Распечатайте полученный список.
'''


def sort_zeroes_right(list_sample=[1, 0, 2, 3, 0, 4, 5, 0, 0, 7, 6, 0, 8, 0, 0, 9]):
    '''Перемещает все ненулевые элементы в левую часть списка,

    не меняя их порядок, а все нули - в правую часть.
    '''

    for item in list_sample:
        if item == 0:
            list_sample.append(item)
            list_sample.remove(item)

    return print(list_sample)


'''
1. Dict comprehensions
Создайте словарь с помощью генератора словарей, так
чтобы его ключами были числа от 1 до 20, а значениями кубы этих чисел.
'''


def dict_keys_in_cube(start=1, stop=21):
    '''Создает словарь с ключами от start до stop

    и значениями равными значению ключа в кубе
    '''

    dict_w_cubes = {key: key ** 3 for key in range(start, stop)}
    print(f'Словарь со значениями равными ключу в кубе - {dict_w_cubes}')


'''
2. Города
Дан список стран и городов каждой страны. Затем даны названия городов.
Для каждого города укажите, в какой стране он находится.
Входные данные
Программа получает на вход количество стран N. Далее идет N строк,
каждая строка начинается с названия страны, затем идут названия городов
этой страны. В следующей строке записано число M, далее идут
M запросов — названия каких-то M городов, перечисленных выше.
Выходные данные
Для каждого из запроса выведите название страны, в котором находится данный город.
Примеры
Входные данные
2
Russia Moscow Petersburg Novgorod Kaluga
Ukraine Kiev Donetsk Odessa
3
Odessa
Moscow
Novgorod
Выходные данные
Ukraine
Russia
Russia
'''


def countries_finder(number_of_countries=1,
                     country_input='Russia Moscow Petersburg Novgorod Kaluga'):
    '''Входные данные
    Программа получает на вход количество стран N. Далее идет N строк,
    каждая строка начинается с названия страны, затем идут названия городов
    этой страны. В следующей строке записано число M, далее идут
    M запросов — названия каких-то M городов, перечисленных выше.

    Для каждого из запроса выведите название страны, в котором находится данный город.
    '''

    number_of_countries = int(input('Введите количество стран: '))
    current_dict = {}
    countries_all = {}

    for i in range(number_of_countries):
        country_input = input('Введите строку страны: ')
        country_list = country_input.split(' ')
        country_name = country_list.pop(0)
        current_dict = current_dict.fromkeys(country_list, country_name)
        countries_all.update(current_dict)

    number_of_requests = int(input('Кол-во запросов: '))
    countries_res = str()

    for i in range(number_of_requests):
        town_input = input('Город: ')
        countries_res = countries_res + countries_all[town_input] + '\n'

    print(f'Список стран, соответствующих вашим запросам:\n{countries_res}')
