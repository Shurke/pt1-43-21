# codewars problem ---- Sum of a Beach
# Beaches are filled with sand, water, fish, and sun. Given a string,
# calculate how many times the words "Sand", "Water",
# "Fish", and "Sun" appear without overlapping (regardless of the case).
def main():
    beach = input("Введите строку ")
    beach = beach.lower()
    ans = 0
    for i in range(len(beach)):
        if beach[i] == 'w':
            f = 0
            if i + 1 < len(beach) and beach[i + 1] == 'a':
                f += 1
            if i + 2 < len(beach) and beach[i + 2] == 't':
                f += 1
            if i + 3 < len(beach) and beach[i + 3] == 'e':
                f += 1
            if i + 4 < len(beach) and beach[i + 4] == 'r':
                f += 1
            if f == 4:
                ans += 1
        if beach[i] == 's':
            f = 0
            if i + 1 < len(beach) and beach[i + 1] == 'u':
                f += 1
            if i + 2 < len(beach) and beach[i + 2] == 'n':
                f += 1
            if f == 2:
                ans += 1
        if beach[i] == 's':
            f = 0
            if i + 1 < len(beach) and beach[i + 1] == 'a':
                f += 1
            if i + 2 < len(beach) and beach[i + 2] == 'n':
                f += 1
            if i + 3 < len(beach) and beach[i + 3] == 'd':
                f += 1
            if f == 3:
                ans += 1
        if beach[i] == 'f':
            f = 0
            if i + 1 < len(beach) and beach[i + 1] == 'i':
                f += 1
            if i + 2 < len(beach) and beach[i + 2] == 's':
                f += 1
            if i + 3 < len(beach) and beach[i + 3] == 'h':
                f += 1
            if f == 3:
                ans += 1
    print(ans)


main()
