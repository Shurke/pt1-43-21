def main():
    '''
    3. Вводится строка.
    Требуется удалить из нее повторяющиеся символы и все пробелы.
    Например, если было введено "abc cde def", то должно быть выведено "abcdef".
    '''
    print('Введите произвольную строку')
    msg = (input().replace(' ', ''))
    result = ''
    for i in msg:
        if i not in result:
            result = result + i
        else:
            pass
    print('Результат:', result)

main()

