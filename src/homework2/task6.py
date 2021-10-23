num = int(input("Введите число для проверки на палиндром: "))
n = num
new = 0
dig = 0
while n > 0:
    dig = n % 10
    new = new * 10 + dig
    n = n // 10
if num == new:
    print(f"{num} - палиндром")
else:
    print(f"{num} - НЕ палиндром")