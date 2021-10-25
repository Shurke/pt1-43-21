our_string = input("Введите строку: ")
c_upper = 0
c_lower = 0
for i in our_string:
    if i.isalpha():
        if i.islower():
            c_lower = c_lower + 1
        else:
            c_upper = c_upper + 1
print("Больших букв: ", c_upper, ", ", "Маленьких букв: ", c_lower)
