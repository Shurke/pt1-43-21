
def task1_4():
    """ Условие задачи 1, FizzBuzz

        Напишите программу, которая печатает цифры от 1 до 100, но вместо чисел, кратных 3 пишет Fizz,
     вместо чисел кратный 5 пишет Buzz, а вместо чисел одновременно кратных и 3 и 5 - FizzBuzz
    """
    for number in range(1, 101):
        divisible3 = number % 3 == 0
        divisible5 = number % 5 == 0
        if divisible3 and divisible5:
            print("FizzBuzz")
        elif divisible3:
            print("Fizz")
        elif divisible5:
            print("Buzz")
        else:
            print(number)


def task2_4():
    """ Условие задачи 2, List practice

    1. Используйте генератор списков чтобы получить следующий: ['ab', 'ac', 'ad', 'bb', 'bc', 'bd'].
    2. Используйте на предыдущий список slice чтобы получить следующий: ['ab', 'ad', 'bc'].
    3. Используйте генератор списков чтобы получить следующий ['1a', '2a', '3a', '4a'].
    4. Одной строкой удалите элемент  '2a' из прошлого списка и напечатайте его.
    5. Скопируйте список и добавьте в него элемент '2a' так чтобы в исходном списке
    этого элемента не было."""

    list1 = [i + j for i in "ab" for j in "bcd"]
    list2 = list1[::2]
    list3 = [str(i) + "a" for i in range(1, 5)]
    print(list3.pop(1))
    list4 = list3.copy()
    list4.append("2a")


def task3_4():
    """ Условие задачи 3, Tuple practice

    Создайте кортеж из одного элемента, чтобы при итерировании по этому элементу последовательно
    выводились значения 1, 2, 3. Убедитесь что len() исходного кортежа возвращает 1."""

    tuple1 = ([1, 2, 3],)
    for i in tuple1:
        for j in i:
            print(j)
    print(len(tuple1))


def task4_4():
    """ Условие задачи 4, Пары элементов

    Дан список чисел. Посчитайте, сколько в нем пар элементов, равных друг другу.
    Считается, что любые два элемента, равные друг другу образуют одну пару, которую
    необходимо посчитать.Входные данные - строка из чисел, разделенная пробелами.
    Выходные данные - количество пар.
    Важно: 1 1 1 - это 3 пары, 1 1 1 1 - это 6 пар
    Задачу поместите в файл task4.py в папке src/homework3."""

    str1 = input("Ведите список чисел: ")
    list1 = str1.split()
    quantity_of_pairs = 0
    for i in range(0, len(list1) - 1):
        for j in range(i + 1, len(list1)):
            if list1[i] == list1[j]:
                quantity_of_pairs += 1

    print(quantity_of_pairs)


def task5_4():
    """ Условие задачи 5, Уникальные элементы в списке
    Дан список. Выведите те его элементы, которые встречаются в списке только один раз.
     Элементы нужно выводить в том порядке, в котором они встречаются в списке."""
    str1 = input("Ведите список чисел: ")
    list1 = str1.split()
    for i in list1:
        if list1.count(i) == 1:
            print(i)


def task6_4():
    """ Условие задачи 6, Упорядоченный список.

    Дан список целых чисел. Требуется переместить все ненулевые элементы в левую часть списка,
    не меняя их порядок, а все нули - в правую часть. Порядок ненулевых элементов изменять нельзя,
    дополнительный список использовать нельзя, задачу нужно выполнить за один проход по списку.
    Распечатайте полученный список."""

    str1 = input("Ведите список чисел: ")
    list1 = str1.split()
    i = 0
    end_index = len(list1) - 1
    while i < end_index:
        if int(list1[i]) == 0:
            el = list1.pop(i)
            list1.append(el)
            end_index -= 1
        else:
            i += 1
    print(list1)

