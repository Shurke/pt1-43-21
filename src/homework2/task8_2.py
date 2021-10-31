'''
Task 2
A pangram is a sentence that contains every single letter of the alphabet at least once.
For example, the sentence "The quick brown fox jumps over the lazy dog" is a pangram, because it uses the letters A-Z at least once (case is irrelevant).
Given a string, detect whether or not it is a pangram. Return True if it is, False if not. Ignore numbers and punctuation.
pangram = "The quick, brown fox jumps over the lazy dog!"
test.assert_equals(is_pangram(pangram), True)
'''

import string
def is_pangram(s):
    letters = ''
    s = s.lower()
    for i in s:
        if i in string.ascii_letters:
            if i not in letters:
                letters = letters + i
            else:
                pass
        else:
            pass
    if len(letters) == 26:
        return True
    else:
        return False
print('Task2 result')
print(is_pangram('The quick, brown fox jumps over the lazy dog!'))
