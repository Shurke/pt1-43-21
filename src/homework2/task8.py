'''
Task 1
Write a function that accepts an array of 10 integers (between 0 and 9),
that returns a string of those numbers in the form of a phone number.
Example
create_phone_number([1, 2, 3, 4, 5, 6, 7, 8, 9, 0]) # => returns "(123) 456-7890"
test.assert_equals(create_phone_number([1, 2, 3, 4, 5, 6, 7, 8, 9, 0]), "(123) 456-7890")
test.assert_equals(create_phone_number([1, 1, 1, 1, 1, 1, 1, 1, 1, 1]), "(111) 111-1111")
test.assert_equals(create_phone_number([1, 2, 3, 4, 5, 6, 7, 8, 9, 0]), "(123) 456-7890")
test.assert_equals(create_phone_number([0, 2, 3, 0, 5, 6, 0, 8, 9, 0]), "(023) 056-0890")
test.assert_equals(create_phone_number([0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), "(000) 000-0000")
'''

def create_phone_number(n):
    res_str = '('
    for i in range(10):
        if i <= 2 or (i > 3 and i <= 5) or i > 6:
            res_str = res_str + str(n[i])
        elif i == 3:
            res_str = res_str + ') ' + str(n[i])
        elif i == 6:
            res_str = res_str + '-' + str(n[i])
    return res_str
print('Task1 result')
print(create_phone_number([1, 2, 3, 4, 5, 6, 7, 8, 9, 0]))
print(create_phone_number([1, 1, 1, 1, 1, 1, 1, 1, 1, 1]))
print(create_phone_number([1, 2, 3, 4, 5, 6, 7, 8, 9, 0]))
print(create_phone_number([0, 2, 3, 0, 5, 6, 0, 8, 9, 0]))
print(create_phone_number([0, 0, 0, 0, 0, 0, 0, 0, 0, 0]))


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


'''
Task 3
A square of squares
Task
Given an integral number, determine if it's a square number:
In mathematics, a square number or perfect square is an integer that is the square of an integer; 
in other words, it is the product of some integer with itself.
The tests will always use some integral number, so don't worry about that in dynamic typed languages.
test.assert_equals(is_square(-1), False, "-1: Negative numbers cannot be square numbers")
test.assert_equals(is_square( 0), True, "0 is a square number (0 * 0)")
test.assert_equals(is_square( 3), False, "3 is not a square number")
test.assert_equals(is_square( 4), True, "4 is a square number (2 * 2)")
test.assert_equals(is_square(25), True, "25 is a square number (5 * 5)")
test.assert_equals(is_square(26), False, "26 is not a square number")
'''

def is_square(n):
    if n >= 0:
       if n ** 0.5 % 1 == 0:
            return True
        else:
            return False
    else:
        return False

print('Task3 result')
print(is_square(3))
print(is_square(26))
print(is_square(25))