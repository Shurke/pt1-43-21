"""
 codewars problem ---- Simple Pig Latin
 Move the first letter of each word to the end of it,
 then add "ay" to the end of the word. Leave punctuation marks untouched.
 pigIt('Pig latin is cool'); // igPay atinlay siay oolcay
 pigIt('Hello world !');     // elloHay orldway !
"""

import string


def main():
    s = input("Введите строку ")
    ans = []
    for i in s.split():
        if i in string.ascii_letters:
            ans.append(i[1:] + i[0] + 'ay')
        else:
            ans.append(i)
    print(' '.join(ans))


main()
