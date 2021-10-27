# codewars problem ---- Vowel Count
# Return the number (count) of vowels in the given string.
def main():
    s = input("Введите строку ")
    ans = 0
    ans += s.count('a')
    ans += s.count('e')
    ans += s.count('i')
    ans += s.count('o')
    ans += s.count('u')
    print(ans)


main()
