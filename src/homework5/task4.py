'''
4.Даны два списка чисел.
Посчитайте, сколько различных чисел входит
только в один из этих списков
'''


def main():
    l1 = [1, 2, 3, 5, 7]
    l2 = [2, 9, 3, 1, 5, 10]
    l_res1 = list(set(l1) - set(l2))
    l_res2 = list(set(l2) - set(l1))

    print('List1:', l1, 'List2:', l2, 'Result1:', l_res1, 'Len1:', len(l_res1), sep='\n')
    print('Result2:', l_res2, 'Len2:', len(l_res2), sep='\n')

main()
