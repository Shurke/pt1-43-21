'''
3.Реализовать функцию get_ranges которая получает на вход непустой список
неповторяющихся целых чисел,отсортированных по возрастанию,
которая этот список “сворачивает”
 get_ranges([0, 1, 2, 3, 4, 7, 8, 10]) // "0-4,7-8,10"
 get_ranges([4,7,10]) // "4,7,10"
 get_ranges([2, 3, 8, 9]) // "2-3,8-9"
'''


def get_ranges(in_lst):
    in_lst.sort()   # precaution
    result_str = ''
    range_begin = True
    for ind in range(len(in_lst)):
        item = in_lst[ind]
        if ind < len(in_lst) - 1:
            if item + 1 == in_lst[ind + 1]:
                if range_begin:
                    result_str = result_str + str(in_lst[ind])
                    range_begin = False
            else:
                if range_begin:
                    result_str = result_str + str(in_lst[ind]) + ','
                else:
                    result_str = result_str + '-' + str(in_lst[ind]) + ','
                    range_begin = True
        else:
            if range_begin:
                result_str = result_str + str(in_lst[ind])
            else:
                result_str = result_str + '-' + str(in_lst[ind])
    print('Result:', result_str)


get_ranges([0, 1, 3, 2, 4, 7, 8, 10])
get_ranges([4, 7, 10])
get_ranges([2, 3, 8, 9])
