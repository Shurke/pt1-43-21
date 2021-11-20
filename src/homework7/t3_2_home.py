"""
2.	List practice
1.	Используйте генератор списков чтобы получить следующий: ['ab', 'ac', 'ad', 'bb', 'bc', 'bd'].
2.	Используйте на предыдущий список slice чтобы получить следующий: ['ab', 'ad', 'bc'].
3.	Используйте генератор списков чтобы получить следующий ['1a', '2a', '3a', '4a'].
4.	Одной строкой удалите элемент  '2a' из прошлого списка и напечатайте его.
5.	Скопируйте список и добавьте в него элемент '2a' так чтобы
в исходном списке этого элемента не было.
"""


def func():
    list1 = [a + b for a in 'ab' for b in 'bcd']
    print(list1)
    list2 = list1[::2]
    print(list2)
    list3 = [n + a for a in 'a' for n in '1234']
    print(list3)
    list4 = [i for i in list3 if i != '2a']
    print(list4)
    list5 = list4.copy()
    list5.append('2a')
    list5.sort()
    print(list5)


if __name__ == "__main__":
    func()
