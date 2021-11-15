"""
3.	Реализовать функцию get_ranges которая получает на вход непустой список
неповторяющихся целых чисел,
отсортированных по возрастанию, которая этот список “сворачивает”
 get_ranges([0, 1, 2, 3, 4, 7, 8, 10]) // "0-4,7-8,10"
 get_ranges([4,7,10]) // "4,7,10"
 get_ranges([2, 3, 8, 9]) // "2-3,8-9"
"""


def get_ranges(list_):
    global prev_item
    result = []
    ranges = []
    for item in list_:
        if not ranges:
            ranges.append([item])
        elif item - prev_item == 1:
            ranges[-1].append(item)
        else:
            ranges.append([item])
        prev_item = int(item)
    for item2 in ranges:
        if len(item2) > 1:
            list1 = [item2[0], item2[-1]]
            list2 = '-'.join(str(i) for i in list1)
            result.append(list2)
        else:
            result.append(str(item2[0]))
    return result


print(get_ranges([2, 3, 8, 9]))

# идея взята из гугла.
# У меня по-прежнему не появляется понимание как выстраивать мысли для поиска решения самостоятельно
# В сложных для меня задачах
