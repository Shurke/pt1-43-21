"""Задача 3, Здесь задча из прошлоой домашней работы. Сам тест будет находится в файле test_task3

Свернуть список.
Реализовать функцию get_ranges которая получает на вход непустой
список неповторяющихся целых чисел, отсортированных по возрастанию,
которая этот список “сворачивает”
get_ranges([0, 1, 2, 3, 4, 7, 8, 10]) // "0-4,7-8,10"
get_ranges([4,7,10]) // "4,7,10"
get_ranges([2, 3, 8, 9]) // "2-3,8-9"
"""


def add_range(string_of_ranges, first_number, middle_number):
    """Функция добавляет диапазон к строке"""
    if len(string_of_ranges) != 0:
        string_of_ranges = string_of_ranges + ", "
    if first_number == middle_number:
        string_of_ranges = string_of_ranges + str(first_number)
    else:
        string_of_ranges = string_of_ranges + str(first_number) + "-" + str(middle_number)
    return string_of_ranges


def get_ranges(list_of_number):
    """Функция сворачивает список"""
    first_number = int(list_of_number[0])
    middle_number = first_number
    string_of_ranges = ""
    for i in range(1, len(list_of_number)):
        current_number = int(list_of_number[i])
        if middle_number + 1 == current_number:
            middle_number += 1
        else:
            string_of_ranges = add_range(string_of_ranges, first_number, middle_number)
            first_number = current_number
            middle_number = current_number
    string_of_ranges = add_range(string_of_ranges, first_number, middle_number)
    return string_of_ranges




