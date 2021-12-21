"""
Реализовать функцию get_ranges которая получает на вход
непустой список неповторяющихся целых чисел,
отсортированных по возрастанию,
которая этот список 'сворачивает'
get_ranges([0, 1, 2, 3, 4, 7, 8, 10]) // '0-4,7-8,10'
get_ranges([4,7,10]) // '4,7,10'
get_ranges([2, 3, 8, 9]) // '2-3,8-9'
"""


class LengthError(Exception):
    """exception is raised when length of input list is 0"""


class ArgumentsError(Exception):
    """exception is rises when input arguments are not validate"""


def add_to_ans_list(ans_list: list, start_num: int, end_num: int) -> None:
    """adds to list"""

    # checks if type of ans_list is list
    if not isinstance(ans_list, list):
        raise ArgumentsError(f'Expected list, got - {type(ans_list)}')
    # checks if type of start_num is int
    if not isinstance(start_num, int):
        raise ArgumentsError(f'Expected int, not {type(start_num)}')
    # checks if type of end_num is int
    if not isinstance(end_num, int):
        raise ArgumentsError(f'Expected int, not {type(start_num)}')
    # checks if end number >= start number
    if end_num < start_num:
        raise ArgumentsError('start number should be less than end number')

    if end_num - start_num == 0:
        ans_list.append(str(start_num))
    else:
        ans_list.append(str(start_num) + '-' + str(end_num))


def get_ranges(input_list: list) -> str:
    """returns ranges of numbers in given list"""

    # checks if type of input_list is list
    if not isinstance(input_list, list):
        raise ValueError('Expected list instead!', type(input_list))
    # checks if len of input_list not zero
    if len(input_list) == 0:
        raise LengthError('Expected not empty list')

    for i in input_list:
        if not isinstance(i, int):
            raise ValueError('Should be integers in list!')

    start_num = input_list[0]
    end_num = input_list[0]
    prev = input_list[0]
    ans_list = []
    for number in input_list[1:]:
        if number == prev + 1:
            end_num += 1
        if number != prev + 1:
            add_to_ans_list(ans_list, start_num, end_num)
            start_num = number
            end_num = number
        if number == input_list[-1]:
            add_to_ans_list(ans_list, start_num, end_num)
        prev = number
    return ','.join(ans_list)
