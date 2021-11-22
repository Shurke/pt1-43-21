'''
Homework 5 tasks
'''


def task_5_1():
    dct = {element: element * element * element for element in range(1, 21)}
    print(dct)


def task_5_2():
    main_dict = {}
    output_lst = []
    # input processing
    in_num_of_rec = int(input('Введите количество записей:'))
    for ind in range(in_num_of_rec):
        country, *cities = input('Введите запись:').split()
        for city in cities:
            # key should be unique
            main_dict[city] = country

    # output processing
    out_num_of_rec = int(input('Введите количество городов:'))
    for ind in range(out_num_of_rec):
        output_lst.append(str(input('Введите город:')))

    print('Result')
    for element in output_lst:
        print(main_dict[element])


def task_5_3():
    l1 = [1, 2, 3, 5, 7]
    l2 = [2, 9, 3, 1]
    l_res = list(set(l1) & set(l2))

    print('List1:', l1, 'List2:', l2, 'Result:', l_res, 'Len:', len(l_res), sep='\n')


def task_5_4():
    l1 = [1, 2, 3, 5, 7]
    l2 = [2, 9, 3, 1, 5, 10]
    l_res1 = list(set(l1) - set(l2))
    l_res2 = list(set(l2) - set(l1))

    print('List1:', l1, 'List2:', l2, 'Result1:', l_res1, 'Len1:', len(l_res1), sep='\n')
    print('Result2:', l_res2, 'Len2:', len(l_res2), sep='\n')


def task_5_5():
    all_students_dct = {}
    one_lang = set()
    # input processing
    in_num_of_stud = int(input('Введите количество школьников:'))
    for ind1 in range(in_num_of_stud):
        languages_lst = []
        in_num_of_lang = int(input('Введите количество языков:'))
        for ind2 in range(in_num_of_lang):
            languages_lst.append(input('Введите язык:'))
        one_lang = one_lang | set(languages_lst)
        all_students_dct[ind1] = languages_lst

    # output processing
    # If leave common_lang as (), the result will be empty set
    common_lang = set(all_students_dct.get(0))
    for ind1 in range(len(all_students_dct.values())):
        tmp_set = set(all_students_dct.get(ind1))
        common_lang = common_lang & tmp_set

    print('Кол-во общих языков:', len(common_lang))
    print('Языки:')
    for ind1 in common_lang:
        print(ind1)

    print('Кол-во общих языков, которые знает хотя бы один школьник:', len(one_lang))
    print('Языки:')
    for ind1 in one_lang:
        print(ind1)


def task_5_6():
    in_str_set = set(input('Введите текст:').split())
    print('Кол-во уникальных слов:', len(in_str_set))


def task_5_7():
    n1 = int(input('Введите первое число:'))
    n2 = int(input('Введите второе число:'))

    if n1 == n2:
        print('НОД = ', n1)
    else:
        while n1 != n2:
            if n1 > n2:
                n1 = n1 - n2
            else:
                n2 = n2 - n1
        print('НОД = ', n1)
