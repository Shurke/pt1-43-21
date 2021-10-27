# codewars problem ---- Simple Pig Latin
# Move the first letter of each word to the end of it,
# then add "ay" to the end of the word. Leave punctuation marks untouched.
def main():
    s = input("Введите строку ")
    ans = ''
    f = False
    c = ''
    for i in s:
        if 'a' <= i <= 'z' or 'A' <= i <= 'Z':
            if not f:
                f = True
                c = i
                continue
            ans += i
        else:
            if f:
                ans += c
                c = ''
                ans += 'ay'
                f = False
            ans += i
    if c != '':
        ans += c
        ans += 'ay'
    print(ans)


main()
