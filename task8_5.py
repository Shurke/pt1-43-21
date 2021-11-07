def max_digit(number: int) -> int:
    n = number % 10
    number = number // 10

    while number > 0:
        if number % 10 > n:
            n = number % 10
        number = number // 10

    return n
