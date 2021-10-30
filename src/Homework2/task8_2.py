def persistence(n):
    # Write a function, persistence, that takes in a positive parameter num
    # and returns its multiplicative persistence, which
    # is the number of times you must multiply the digits
    # in num until you reach a single digit

    def get_digit(dgt):
        s = 1
        while dgt > 0:
            s *= dgt % 10
            dgt //= 10
        return s

    if n // 10 == 0:
        return 0
    else:
        nmb_times = 0
        while n // 10 > 0:
            n = get_digit(n)
            nmb_times += 1
        return nmb_times


k = int(input())
print(persistence(k))
