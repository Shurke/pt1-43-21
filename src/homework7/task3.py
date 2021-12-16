'''Реализовать функцию get_ranges которая получает на вход
непустой список неповторяющихся целых чисел, отсортированных по возрастанию,
которая этот список “сворачивает”
 get_ranges([0, 1, 2, 3, 4, 7, 8, 10]) // "0-4,7-8,10"
 get_ranges([4,7,10]) // "4,7,10"
 get_ranges([2, 3, 8, 9]) // "2-3,8-9"
'''


def get_rangie(get_ranges):
    '''Функция форматирует ранжированный список из get_ranges'''

    for i in get_ranges:
        if i == '-':
            index_dash = get_ranges.index('-')

            num_start = str(get_ranges[index_dash - 1])
            num_end = str(get_ranges[index_dash + 1])
            get_ranges.insert(index_dash, num_start + '-' + num_end)
            get_ranges.remove('-')
            get_ranges.pop(index_dash - 1)
            get_ranges.pop(index_dash)

    collapsed_string = ','.join(str(e) for e in get_ranges)

    return print(f'Результат свернутого списка: {collapsed_string}')


def get_ranges(sorted_list=list) -> list:
    '''Функция сворачивает полученный непустой список неповторяющихся целых чисел,

    отсортированных по возрастанию
    '''

    collapsed_list = []
    collapsed_list.append(sorted_list[0])
    counter = 0
    for num in sorted_list:
        counter += 1
        if num > sorted_list[(counter - 2)] + 1 or len(sorted_list) == counter:
            collapsed_list.append(num)
        elif num == sorted_list[(counter - 2)] + 1:
            if sorted_list[counter] - num > 1:
                collapsed_list.append(num)
            elif collapsed_list[-1] != '-':
                collapsed_list.append('-')
        else:
            pass
    get_rangie(collapsed_list)


get_ranges([0, 1, 2, 3, 4, 7, 8, 10])  # "0-4,7-8,10"
get_ranges([4, 7, 10])  # "4,7,10"
get_ranges([2, 3, 8, 9])  # "2-3,8-9"
