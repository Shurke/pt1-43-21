'''
Homework tasks 4
'''

import copy


def task_4_1():
    for i in range(1, 101):
        if i % 3 == 0 and i % 5 == 0:
            print('FizzBuzz')
        elif i % 3 == 0:
            print('Fizz')
        elif i % 5 == 0:
            print('Buzz')
        else:
            print(i)


def task_4_2():
    # 1
    lst1 = [a + b for a in 'ab' for b in 'bcd']
    print('List1:', lst1)

    # 2
    lst2 = lst1[0:5:2]
    print('List2:', lst2)

    # 3
    lst3 = [str(x) + 'a' for x in range(1, 5)]
    print('List3:', lst3)

    # 4
    lst3.remove('2a')
    print('List4:', lst3)

    # 5
    lst5 = copy.deepcopy(lst3)
    lst5.insert(1, '2a')
    print('List5:', lst5)


def task_4_3():
    tup = ('123',)
    print('Tuple len:', len(tup))
    for i in tup[0]:
        print(i)


def task_4_4():
    input_str = '1 1 1 1'
    cnt = 0
    lst = input_str.split()

    for ind1 in range(len(lst) - 1):
        l2_start_ind = ind1 + 1
        for ind2 in range(l2_start_ind, len(lst)):
            if lst[ind1] == lst[ind2]:
                cnt += 1

    print('Pairs num:', cnt)


def task_4_5():
    input_lst = [1, 2, 3, 5, 9, 0, 1, 4, 2]
    res_lst = []
    for ind in input_lst:
        if input_lst.count(ind) == 1:
            res_lst.append(ind)

    print('Result', res_lst)


def task_4_6():
    input_lst = [1, 2, 0, 3, 5, 9, 0, 1, 4, 2]
    bad_num = 0
    for ind in range(len(input_lst)):
        if input_lst[ind] != bad_num:
            continue
        input_lst.append(bad_num)
        input_lst.remove(bad_num)

    print('Result:', input_lst)


