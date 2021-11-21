'''Реализовать функцию get_ranges которая получает на вход
непустой список неповторяющихся целых чисел, отсортированных по возрастанию,
которая этот список “сворачивает”
 get_ranges([0, 1, 2, 3, 4, 7, 8, 10]) // "0-4,7-8,10"
 get_ranges([4,7,10]) // "4,7,10"
 get_ranges([2, 3, 8, 9]) // "2-3,8-9"
'''


def get_ranges(sorted_list=list) -> list:
    collapsed_list = []
    collapsed_list.append(sorted_list[0])
    counter = 0
    for num in sorted_list:
        counter += 1
        if num - sorted_list[(counter - 2)] > 1:
            collapsed_list.append(num)
        elif num - sorted_list[(counter - 2)] == 1 and collapsed_list[-1] != '-':
            collapsed_list.append('-')

    collapsed_string = ','.join(str(e) for e in collapsed_list)
    print(f'Результат свернутого списка: {collapsed_string}')


get_ranges([1, 3, 4, 5, 6, 8, 10])
