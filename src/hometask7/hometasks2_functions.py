"""
Module 1
Here are  collected
all of hometask2's functions
"""


def total_price():
    """
    task2.1
    Вводится M рублей и N копеек цена, а также количество S товара
    Посчитайте общую цену в рублях и копейках за L товаров.
    """

    ruble = int(input("стоимость товара (рубли) "))
    penny = int(input("Введите стоимость товара (копейки) "))
    volume = int(input("Введите количество товара "))
    ruble_result = volume * (ruble * 100 + penny) // 100
    penny_result = volume * (ruble * 100 + penny) % 100
    print(ruble_result, 'руб.', penny_result, 'коп.')


def the_longest_word():
    """
    task2.2
    Найти самое длинное слово в введенном предложении.
    """

    import string

    input_str = input("Введите строку ").split()
    ans = ''
    max_counter = 0
    for element in input_str:
        temp = element.strip(string.punctuation)
        if len(temp) > max_counter:
            max_counter = len(temp)
            ans = temp
    print('Самое длинное слово -', ans)


def replace_spaces_and_not_unique_symbols():
    """
    task2.3
    Вводится строка. Требуется удалить из нее повторяющиеся символы и все пробелы.
    """

    input_str = input("Введите строку ").replace(' ', '')
    ans = ''
    for element in input_str:
        if element not in ans:
            ans += element
    print(ans)


def counting_upper_and_lower():
    """
    task2.4
    Посчитать количество строчных (маленьких) и прописных (больших) букв в введенной строке.
    Учитывать только английские буквы.
    """
    import string

    input_str = input("Введите Вашу строку ")
    lower_count = 0
    upper_count = 0
    for letter in input_str:
        if letter in string.ascii_uppercase:
            upper_count += 1
        if letter in string.ascii_lowercase:
            lower_count += 1
    print('lower', lower_count, '\n', 'upper', upper_count)


def fib():
    """
    task2.5
    Выведите n-ое число Фибоначчи
    """

    num = int(input("Введите n-ое число Фибоначчи "))
    if num == 0:
        print('0')
        exit()
    prev1 = 0
    prev2 = 1
    ans = 1
    num -= 2
    while num:
        num -= 1
        ans = prev1 + prev2
        prev1 = prev2
        prev2 = ans
    print(ans)


def is_palindrome():
    """
    task2.6
    Определите, является ли число палиндромом
    """

    num = int(input("Введите ваше число "))
    reverse_num = 0
    num1 = num
    while num1 > 0:
        reverse_num = reverse_num * 10 + num1 % 10
        num1 = num1 // 10
    if reverse_num == num:
        print("YES")
    else:
        print("NO")


def is_a_triangle():
    """
     task2.7
     Даны: три стороны треугольника.
     Требуется: проверить, действительно ли это стороны треугольника.
     Если стороны определяют треугольник, найти его площадь.
     Если нет, вывести сообщение о неверных данных.
    """

    import math

    first = int(input("Введите 1 сторону треугольника "))
    second = int(input("Введите 2 сторону треугольника "))
    third = int(input("Введите 3 сторону треугольника "))
    if first + second > third and first + third > second and second + third > first:
        p = (first + second + third) / 2
        print(math.sqrt(p * (p - first) * (p - second) * (p - third)))
    else:
        print("Error, Wrong input data format, please try again!")


def the_longest_zero_sequence():
    """
     task8.1
     acmp.ru problem № 43
     Требуется найти самую длинную непрерывную цепочку нулей в последовательности нулей и единиц.
    """

    input_string = input("Введите строку из 0 и 1 ")
    max_null = 0
    current_null = 0
    for symbol in input_string:
        if symbol == '0':
            current_null += 1
        else:
            max_null = max(max_null, current_null)
            current_null = 0
    max_null = max(max_null, current_null)
    print('Длина самой длинной последовательности нулей равна', max_null)


def total_price_calc():
    """
     task8.2
     codewars problem ---- Transportation on vacation
     Every day you rent the car costs $40. If you rent the car for 7 or more days,
     you get $50 off your total. Alternatively,
     if you rent the car for 3 or more days, you get $20 off your total.
    """

    days = int(input("Введите продолжительность отпуска в днях "))
    discount = 0
    if 3 <= days < 7:
        discount = 20
    if days >= 7:
        discount = 50
    print('Итоговая цена', days * 40 - discount)


def number_of_particular_words():
    """
    task8.3
      codewars problem ---- Sum of a Beach
      Beaches are filled with sand, water, fish, and sun. Given a string,
      calculate how many times the words "Sand", "Water",
      "Fish", and "Sun" appear without overlapping (regardless of the case).
    """

    beach = input("Введите строку ")
    beach = beach.lower()
    ans = 0
    words = ["sand", "water", "fish", "sun"]
    for i in words:
        ans += beach.count(i)
    print('Количество искомых слов', ans)


def vowel_count():
    """
     task8.4
     codewars problem ---- Vowel Count
     Return the number (count) of vowels in the given string.
    """

    input_string = input("Введите строку ")
    ans = 0
    ans += input_string.count('a')
    ans += input_string.count('e')
    ans += input_string.count('i')
    ans += input_string.count('o')
    ans += input_string.count('u')
    print('Количество гласных', ans)


def text_encryption():
    """
     task8.5
     codewars problem ---- Simple Pig Latin
     Move the first letter of each word to the end of it,
     then add "ay" to the end of the word. Leave punctuation marks untouched.
     pigIt('Pig latin is cool'); // igPay atinlay siay oolcay
     pigIt('Hello world !');     // elloHay orldway !
    """

    import string

    s = input("Введите строку ")
    ans = []
    for word in s.split():
        if word in string.ascii_letters:
            ans.append(word[1:] + word[0] + 'ay')
        else:
            ans.append(word)
    print(' '.join(ans))
