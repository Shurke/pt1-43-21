'''Реализовать функцию get_ranges которая получает на вход
непустой список неповторяющихся целых чисел, отсортированных по возрастанию,
которая этот список “сворачивает”
 get_ranges([0, 1, 2, 3, 4, 7, 8, 10]) // "0-4,7-8,10"
 get_ranges([4,7,10]) // "4,7,10"
 get_ranges([2, 3, 8, 9]) // "2-3,8-9"
'''


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

    for i in collapsed_list:
        if i == '-':
            index_dash = collapsed_list.index('-')
            collapsed_list.insert(index_dash,
                                  str(collapsed_list[index_dash - 1]) + '-' +
                                  str(collapsed_list[index_dash + 1]))
            collapsed_list.remove('-')
            collapsed_list.pop(index_dash - 1)
            collapsed_list.pop(index_dash)

    collapsed_string = ','.join(str(e) for e in collapsed_list)

    return print(f'Результат свернутого списка: {collapsed_string}')


get_ranges([0, 1, 2, 3, 4, 7, 8, 10])  # "0-4,7-8,10"
get_ranges([4, 7, 10])  # "4,7,10"
get_ranges([2, 3, 8, 9])  # "2-3,8-9"
