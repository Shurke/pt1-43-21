num = input("Введите любое число: ")
num2 = num[::-1]
if num == num2:
    print("Является палиндромом")
else:
    print("Не является")