def reverse_seq(n):
    # Build a function that returns an array of integers from n to 1 where n>0
    s = []
    i = n
    while i > 0:
        s.append(i)
        i -= 1
    return s


n_1 = int(input())
print(reverse_seq(n_1))
