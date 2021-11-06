'''
6. Слова
Во входной строке записан текст.
Словом считается последовательность непробельных символов идущих подряд,
слова разделены одним или большим числом пробелов или символами конца строки.
Определите, сколько различных слов содержится в этом тексте.
'''


text_input = 'Enter some\n text:    text some '
text_input = text_input.replace('\n', ' ').split(' ')

set_words = set()
for word in text_input:
    if word != '':
        set_words.add(word)

print(len(set_words))
