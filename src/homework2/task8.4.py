'''
Write a function that takes in a string of one or more words,
and returns the same string, but with all five or more letter
words reversed (like the name of this kata).

Strings passed in will consist of only letters and spaces.
Spaces will be included only when more than one word is present.
'''

sentence = input('Enter some string: ')


def spin_words(sentence):
    sentence = sentence.split(' ')
    string_result = ''

    for word in sentence:
        if len(word) >= 5:
            string_result = string_result + word[::-1] + ' '
        else:
            string_result = string_result + word + ' '

    string_result = string_result.strip(' ')
    return string_result


print(spin_words(sentence))
