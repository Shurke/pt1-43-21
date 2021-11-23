"""
Module 2
Here are  collected
all of hometask4's functions
"""


def fizz_buzz_print():
    """
    task4.1
    программа, которая печатает цифры от 1 до 100, но вместо чисел,
    кратных 3 пишет Fizz, вместо чисел кратный 5
    пишет Buzz, а вместо чисел
    одновременно кратных и 3 и 5 - FizzBuzz
    """

    for num in range(1, 101):
        if num % 3 == 0 and num % 5 == 0:
            print('FizzBuzz')
        elif num % 3 == 0:
            print('Fizz')
        elif num % 5 == 0:
            print('Buzz')
        else:
            print(num)


def list_comprehension():
    """
    task4.2
    1)Используйте генератор списков чтобы получить следующий:
    ['ab', 'ac', 'ad', 'bb', 'bc', 'bd'].
    2)Используйте на предыдущий список slice чтобы получить следующий:
    ['ab', 'ad', 'bc'].
    3)Используйте генератор списков чтобы получить следующий
    ['1a', '2a', '3a', '4a'].
    4)Одной строкой удалите элемент  '2a' из прошлого списка и напечатайте его.
    5)Скопируйте список и добавьте в него элемент '2a' так,
    чтобы в исходном списке этого элемента не было.
    """

    first_list = [elem1 + elem2 for elem1 in 'ab' for elem2 in 'bcd']
    print('Первый искомый список', first_list)
    print('Первый список после slice', first_list[::2])
    second_list = [str(num) + 'a' for num in range(1, 5)]
    print('Второй искомый список', second_list)
    print('Печатаем удаленный элемент', second_list.pop(1))
    # print('Второй список после удаления элемента', second_list)
    third_list = second_list.copy()
    third_list.insert(1, '2a')
    print('Копия 2 списка с элементом "2а"', third_list)


def creating_a_tuple():
    """
    task4.3
    Создает кортеж из одного элемента, чтобы при
    итерировании по этому элементу последовательно
    выводились значения 1, 2, 3.
    len() исходного кортежа возвращает 1.
    """

    tuple1 = ((1, 2, 3), )
    print('Размер кортежа -', len(tuple1), '\nСодержимое 1 элемента -', end=' ')
    for iter_ in tuple1[0]:
        print(iter_, end=' ')


def number_of_equal_pairs():
    """
    task4.4
    Дан список чисел. Функция высчитывает,
    сколько в нем пар элементов, равных друг другу.
    Считается, что любые два элемента,
    равные друг другу образуют одну пару,
    которую необходимо посчитать.
    """

    lst = [1, 1, 3, 4, 5, 3, 1, 2, 5, 8, 9, 2, 3, 1, 1, 0, 6]
    ans = 0
    for i in range(len(lst)):
        for j in lst[i + 1:]:
            if lst[i] == j:
                ans += 1
    print('Количество пар -', ans)


def unique_elements(list_of_numbers):
    """
    task4.5
    Дан список. Выводятся те его элементы,
    которые встречаются в списке только один раз.
    Элементы выводятся в том порядке,
    в котором они встречаются в списке.
    """

    ans_list = []
    for element in list_of_numbers:
        if list_of_numbers.count(element) == 1:
            ans_list.append(element)
    return ans_list


def zero_at_the_end(input_list):
    """
    task4.6
    Дан список целых чисел.
    Все ненулевые элементы перемещаются
    в левую часть списка,
    их порядок не менятеся, а все нули - в правую часть.
    Порядок ненулевых элементов неизменный
    """

    for element in range(len(input_list)):
        if input_list[element] == 0:
            input_list.pop(element)
            input_list.append(0)
    print('Итоговый список -', input_list)
