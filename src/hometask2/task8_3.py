"""
  codewars problem ---- Sum of a Beach
  Beaches are filled with sand, water, fish, and sun. Given a string,
  calculate how many times the words "Sand", "Water",
  "Fish", and "Sun" appear without overlapping (regardless of the case).
"""


def main():
    beach = input("Введите строку ")
    beach = beach.lower()
    ans = 0
    beach = beach.lower()
    words = ["sand", "water", "fish", "sun"]
    for i in words:
        ans += beach.count(i)
    print('Количество искомых слов', ans)


main()
