"""
Реализовать функцию get_ranges которая получает на вход
непустой список неповторяющихся целых чисел,
отсортированных по возрастанию,
которая этот список 'сворачивает'
get_ranges([0, 1, 2, 3, 4, 7, 8, 10]) // '0-4,7-8,10'
get_ranges([4,7,10]) // '4,7,10'
get_ranges([2, 3, 8, 9]) // '2-3,8-9'
"""


def add_to_ans_list(ans_list, start_num, end_num):
    """adds to list"""

    if end_num - start_num == 0:
        ans_list.append(str(start_num))
    else:
        ans_list.append(str(start_num) + '-' + str(end_num))
    return ans_list


def get_ranges(input_list):
    """returns ranges of numbers in given list"""

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


def main():
    input_list = [1, 2, 3, 4, 6, 8, 10, 11, 12, 15]
    print('Диапазоны значений в списке -', get_ranges(input_list))


if __name__ == '__main__':
    main()
