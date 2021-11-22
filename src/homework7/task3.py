"""Реализовать функцию get_ranges, которая получает на вход непустой список неповторяющихся целых чисел,
отсортированных по возрастанию, которая этот список “сворачивает”.
get_ranges([0, 1, 2, 3, 4, 7, 8, 10]) // "0-4,7-8,10"
get_ranges([4,7,10]) // "4,7,10"
get_ranges([2, 3, 8, 9]) // "2-3,8-9"
"""


def get_ranges(list_):
    ranges = []
    prev_item = ''
    for item in list_:
        if not ranges:
            ranges.append([item])
        elif prev_item != '' and int(item) - prev_item == 1:
            ranges[-1].append(item)
        else:
            ranges.append([item])
        prev_item = int(item)
    final_ranges = []
    for r in ranges:
        if len(r) > 1:
            add_range = str(r[0]) + '-' + str(r[-1])
            final_ranges.append(add_range)
        else:
            final_ranges.append(str(r[0]))
    print('Результат сворачивания списка: ' + ','.join(final_ranges))


get_ranges([4, 7, 10, 11])
