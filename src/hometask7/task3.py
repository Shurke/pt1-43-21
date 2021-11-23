"""
Реализовать функцию get_ranges которая получает на вход
непустой список неповторяющихся целых чисел,
отсортированных по возрастанию,
которая этот список 'сворачивает'
get_ranges([0, 1, 2, 3, 4, 7, 8, 10]) // '0-4,7-8,10'
get_ranges([4,7,10]) // '4,7,10'
get_ranges([2, 3, 8, 9]) // '2-3,8-9'
"""


def get_ranges(input_list):
    """returns ranges of numbers in given list"""

    ans_list = []
    start_num = input_list[0]
    end_num = input_list[0]
    prev = input_list[0]

    def add_to_ans_list():
        """adds to list"""

        if end_num - start_num == 0:
            ans_list.append(start_num)
        else:
            ans_list.append(str(start_num) + '-' + str(end_num))

    for number_ in input_list[1:]:
        if number_ == prev + 1:
            end_num += 1
        if number_ != prev + 1:
            add_to_ans_list()
            start_num = number_
            end_num = number_
        if number_ == input_list[-1]:
            add_to_ans_list()
        prev = number_
    return ans_list


def main():
    input_list = [1, 2, 3, 4, 6, 8, 10, 11, 12, 15]
    print('Диапазоны значений в списке -', get_ranges(input_list))


if __name__ == '__main__':
    main()
