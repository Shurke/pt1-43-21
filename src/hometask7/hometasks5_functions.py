"""
Module 3
Here are  collected
all of hometask5's functions
"""


def dictionary_comprehension():
    """
     task5.1
     Создает словарь с помощью генератора словарей, так чтобы его ключами
     были числа от 1 до 20, а значениями кубы этих чисел.
    """

    dictionary = {element: element ** 3 for element in range(1, 21)}
    print(dictionary)


def city_is_in_the_country():
    """
    task5.2
    Дан список стран и городов каждой страны.
    Затем даны названия городов. Для каждого города указано,
    в какой стране он находится.
    """

    def input_countries_and_cities():
        input_dict = {}
        for _ in range(int(input('Введите количество стран: '))):
            str_ = input('Введите страну и ее города ').split()
            input_dict.update({element: str_[0] for element in str_[1:]})
        return input_dict

    def input_requests():
        num_of_requests = int(input('Введите количество запросов: '))
        return [input('Город - ') for _ in range(num_of_requests)]

    input_dictionary = input_countries_and_cities()
    requests = input_requests()
    for i in requests:
        print(input_dictionary[i])


def set_intersection():
    """
    task5.3
    Даны два списка чисел.
    Функция считает, сколько различных
    чисел содержится одновременно как
    в первом списке, так и во втором.
    """

    input_list1 = [1, 2, 3, 4, 6, 8, 10]
    input_list2 = [2, 3, 7, 4, 10, 6, 7]
    ans_set = set(input_list1) & set(input_list2)
    print('Количество чисел, содержащихся как в 1 списке, так и во 2 -', len(ans_set))


def set_xor():
    """
    task5.4
    Даны два списка чисел.
    Функция высчитывает, сколько различных
    чисел входит только в один из этих списков
    """

    input_list1 = [1, 2, 2, 3, 4, 6, 7, 1, 1, 10]
    input_list2 = [2, 3, 7, 2, 4, 6, 7, 0, 11]
    print('Количество чисел входящих только в один из этих списков -', end=' ')
    print(len(set(input_list1) ^ set(input_list2)))


def about_languages_among_students():
    """
    task5.5
    Каждый из N школьников некоторой школы знает Mi языков.
    Функция определяет,
    какие языки знают все школьники и языки,
    которые знает хотя бы один из школьников.
    """

    students_num = int(input('Введите количество школьников: '))
    students_languages = []
    for _ in range(students_num):
        print('Введите количество языков, которое знает школьник: ', end='')
        languages_num = int(input())
        languages = {input('Язык - ') for _ in range(languages_num)}
        students_languages.append(languages)
    all_known_languages = students_languages[0]
    at_least_one_known = students_languages[0]
    for element in students_languages:
        all_known_languages = all_known_languages & element
        at_least_one_known.update(element)
    print('Количество языков, которые знают все школьники -', end=' ')
    print(len(all_known_languages), '\n', all_known_languages)
    print('Количесвто языков, которые знает хотя бы 1 школьник -', end=' ')
    print(len(at_least_one_known), '\n', at_least_one_known)


def number_of_different_words():
    """
    task5.6
    Во входной строке вводится текст.
    Функция определяет, сколько различных
    слов содержится в этом тексте.
    Словом считается последовательность
    непробельных символов идущих подряд,
    слова разделены одним или большим числом
    пробелов или символами конца строки.
    """

    input_text = input('Введите ваш текст ')
    answer_set = set(input_text.split())
    print('Количество различных слов в тексте -', len(answer_set))


def euclid_gcd():
    """
    task5.7
    Даны два натуральных числа.
    Функция вычисляет их
    наибольший общий делитель
    при помощи алгоритма Евклида
    """

    number1 = int(input('Введите первое число: '))
    number2 = int(input('Введите второе число: '))
    if number1 > number2:
        number1, number2 = number2, number1
    prev_number1 = number1
    prev_number2 = number2
    help_number = prev_number1
    while prev_number1 % prev_number2 > 0:
        prev_number1 = prev_number2
        prev_number2 = help_number % prev_number2
        help_number = prev_number1
    print('НОД равен -', prev_number2)
