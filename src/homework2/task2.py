import string
our_string = input("Введите предложение: ")
list_punct = string.punctuation
our_string_clean = ""
for i in our_string:
    if i not in list_punct:
        our_string_clean = our_string_clean + i
list_of_words = our_string_clean.split()
len_of_list_of_words = len(list_of_words)
if len_of_list_of_words == 0:
    print("Вы ничего не ввели")
elif len_of_list_of_words == 1:
    print(list_of_words[0])
else:
    longest_word = ""
    len_of_longest_word=0
    for i in list_of_words:
        if len_of_longest_word < len(i):
            len_of_longest_word = len(i)
            longest_word = i
    print(longest_word)
