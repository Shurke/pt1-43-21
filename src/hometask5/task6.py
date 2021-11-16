"""
Слова
Во входной строке записан текст. Словом считается последовательность
непробельных символов идущих подряд,
слова разделены одним или большим числом пробелов или символами конца строки.
Определите, сколько различных слов содержится в этом тексте.
"""


def main():
    input_text = input('Введите ваш текст ')
    answer_set = set(input_text.split())
    print('Количество различных слов в тексте -', len(answer_set))


main()
