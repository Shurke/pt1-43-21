# Write a function that takes in a string of one or more words,
# and returns the same string, but with all five or more letter
# words reversed (like the name of this kata).

# Strings passed in will consist of only letters and spaces.
# Spaces will be included only when more than one word is present.

sentence = input('Enter some string: ')


def spin_words(sentence):
    sentence = sentence.split(' ')
    a = ''
    for i in sentence:
        if len(i) >= 5:
            a = a + i[::-1] + ' '
        else:
            a = a + i + ' '
    a = a.strip(' ')
    return a


print(spin_words(sentence))
