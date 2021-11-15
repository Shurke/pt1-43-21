'''
1.Используйте генератор списков чтобы получить следующий:['ab', 'ac', 'ad', 'bb', 'bc', 'bd'].
2.Используйте на предыдущий список slice чтобы получить следующий:['ab', 'ad', 'bc'].
3.Используйте генератор списков чтобы получить следующий ['1a', '2a', '3a', '4a'].
4.Одной строкой удалите элемент '2a' из прошлого списка и напечатайте его.
5.Скопируйте список и добавьте в него элемент '2a' так,
чтобы в исходном списке этого элемента не было.
'''
import copy


def main():
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


main()
