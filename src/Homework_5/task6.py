"""
Во входной строке записан текст. Словом считается последовательность непробельных символов идущих
подряд, слова разделены одним или большим числом пробелов или символами конца строки. Определите,
сколько различных слов содержится в этом тексте.
"""


def task6(str_):
    for char in str_:
        if (not char.isalpha()) and char != ' ':
            str_ = str_.replace(char, "")
    str_ = set(str_.lower().split())
    return f'The text contains {len(str_)} different words'


if __name__ == "__main__":
    print(task6(
        str_='Trump hit back, 11 repeated \n    '
             'again hit 222    false \n 11 claim that the \n election was stolen'))
