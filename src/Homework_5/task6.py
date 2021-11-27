"""
Во входной строке записан текст. Словом считается последовательность непробельных символов идущих
подряд, слова разделены одним или большим числом пробелов или символами конца строки. Определите,
сколько различных слов содержится в этом тексте.
"""


def task6(input_str=None):
    if input_str is None:
        input_str = 'Trump hit back, 11 repeated \n again hit false \n 11 claim that the election'
    for char in input_str:
        if not char.isalpha() and char != ' ':
            input_str = input_str.replace(char, "")
    input_str = set(input_str.lower().split())
    return f'The text contains {len(input_str)} different words'


print(task6())
