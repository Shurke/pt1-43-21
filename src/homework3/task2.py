'''
List practice
1. Используйте генератор списков чтобы получить следующий: ['ab', 'ac', 'ad', 'bb', 'bc', 'bd'].
2. Используйте на предыдущий список slice чтобы получить следующий: ['ab', 'ad', 'bc'].
3. Используйте генератор списков чтобы получить следующий ['1a', '2a', '3a', '4a'].
4. Одной строкой удалите элемент  '2a' из прошлого списка и напечатайте его.
5. Скопируйте список и добавьте в него элемент '2a' так чтобы в исходном списке
этого элемента не было.
'''

lst_from1 = [(first_list + second_list) for first_list in ['a', 'b']
             for second_list in ['b', 'c', 'd']]
print(lst_from1)

print(lst_from1[::2])

lst_from3 = [digit + word for digit in ['1', '2', '3', '4'] for word in 'a']
print(lst_from3)

print(lst_from3.pop(1))

lst_from5 = lst_from3.copy()
lst_from5.insert(1, '2a')
print(lst_from5)
