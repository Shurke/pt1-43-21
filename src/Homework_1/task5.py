# последовательность наичнается с 0!
fib = 0
fib_next = 1

for i in range(int(input('Enter № of num in Fibonachi  string: ')) - 1):
    fib, fib_next = fib_next, fib_next + fib
print(fib)
