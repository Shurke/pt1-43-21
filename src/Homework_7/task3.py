"""
Реализовать функцию get_ranges которая получает на вход непустой список неповторяющихся целых
чисел, отсортированных по возрастанию, которая этот список “сворачивает”
 get_ranges([0, 1, 2, 3, 4, 7, 8, 10]) // "0-4,7-8,10"
 get_ranges([4,7,10]) // "4,7,10"
 get_ranges([2, 3, 8, 9]) // "2-3,8-9"
Задачу поместите в файл task3.py в папке src/homework7
"""


def get_ranges(num_list: list = None) -> str:
    """This function collapses sequences of consecutive digits"""
    total = []
    list_tmp = []
    result = ''
    if num_list is None:
        num_list = [0, 1, 2, 3, 4, 7, 8, 10]
    for i in range(len(num_list) - 1):
        if num_list[i] + 1 == num_list[i + 1]:
            list_tmp.append(num_list[i])
        else:
            list_tmp.append(num_list[i])
            total.append(list_tmp)
            list_tmp = []
        if i == len(num_list) - 2:
            if num_list[i] + 1 == num_list[i + 1]:
                if num_list[i] in list_tmp:
                    list_tmp.append(num_list[-1])
                    total.append(list_tmp)
            else:
                list_tmp.append(num_list[-1])
                total.append(list_tmp)
    for i in total:
        if len(i) > 1:
            result += str(i[0]) + '-' + str(i[-1]) + ','
        else:
            result += str(i[-1]) + ','
    return result[:-1]


print(get_ranges())
