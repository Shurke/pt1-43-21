"""
1)Используйте генератор списков чтобы получить следующий: ['ab', 'ac', 'ad', 'bb', 'bc', 'bd'].
2)Используйте на предыдущий список slice чтобы получить следующий: ['ab', 'ad', 'bc'].
3)Используйте генератор списков чтобы получить следующий ['1a', '2a', '3a', '4a'].
4)Одной строкой удалите элемент  '2a' из прошлого списка и напечатайте его.
5)Скопируйте список и добавьте в него элемент '2a' так,
  чтобы в исходном списке этого элемента не было.
"""


def main():
    first_list = [i + j for i in 'ab' for j in 'bcd']
    print('Первый искомый список', first_list)
    print('Первый список после slice', first_list[::2])
    second_list = [str(i) + 'a' for i in range(1, 5)]
    print('Второй искомый список', second_list)
    print('Печатаем удаленный элемент', second_list.pop(1))
    # print('Второй список после удаления элемента', second_list)
    third_list = second_list.copy()
    third_list.insert(1, '2a')
    print('Копия 2 списка с элементом "2а"', third_list)


main()
