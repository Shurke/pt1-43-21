"""    3. Реализовать функцию get_ranges которая получает на вход непустой список неповторяющихся
целых чисел, отсортированных по возрастанию, которая этот список “сворачивает”
 get_ranges([0, 1, 2, 3, 4, 7, 8, 10]) // "0-4,7-8,10"
 get_ranges([4,7,10]) // "4,7,10"
 get_ranges([2, 3, 8, 9]) // "2-3,8-9"""


def get_ranges(list1):
    str1 = str(list1[0])
    for item in range(1, len(list1)):
        if list1[item] == list1[item - 1] + 1:
            if str1[-1] != '-':
                str1 = str1 + '-'
            elif str1[-1] == '-' and item == len(list1) - 1:
                str1 = str1 + str(list1[item])
        else:
            if str1[-1] != '-':
                str1 = str1 + ',' + str(list1[item])
            else:
                str1 = str1 + str(list1[item - 1]) + ',' + str(list1[item])
    print('"Свернутый" список: ', str1)
    return list1


print(get_ranges([0, 1, 2, 3, 4, 7, 8, 10]))
print(get_ranges([4, 7, 10]))
print(get_ranges([2, 3, 8, 9]))
