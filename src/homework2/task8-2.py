'''
You are given a string and your task is to swap cases. In other words, convert all lowercase
letters to uppercase letters and vice versa. For Example:Www.HackerRank.com → wWW.hACKERrANK.COM
Pythonist 2 → pYTHONIST 2
'''


def main():
    text = 'HackerRank.com presents "Pythonist 2".'
    text2 = text.swapcase()
    print(text2)


if __name__ == "__main__":
    main()
