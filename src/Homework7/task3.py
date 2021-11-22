"""
    Реализовать функцию get_ranges которая получает на вход
    непустой список неповторяющихся целых чисел, отсортированных
    по возрастанию, которая этот список “сворачивает”.

    get_ranges([0, 1, 2, 3, 4, 7, 8, 10]) // "0-4,7-8,10"

    get_ranges([4,7,10]) // "4,7,10"

    get_ranges([2, 3, 8, 9]) // "2-3,8-9"
"""


def get_range(input_list):
    out_str = str(input_list[0])
    for item in range(1, len(input_list)):
        # Проврка наличия последовательности
        if input_list[item] == input_list[item - 1] + 1:
            if out_str[-1] != '-':
                # Проверка повторности последовательности
                out_str = out_str + '-'
            elif out_str[-1] == '-' and item == len(input_list) - 1:
                out_str = out_str + str(input_list[item])
        else:
            if out_str[-1] != '-':
                out_str = out_str + ',' + str(input_list[item])
            else:
                out_str = out_str + str(input_list[item - 1]) + ',' + str(input_list[item])
    print('"Свернутый" список: ', out_str)
    return


my_string = input('Введите список чисел через запятую: ')
my_list = list(map(int, my_string.split(',')))
get_range(my_list)
