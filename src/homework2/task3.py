our_string = input("Введите строку: ")
our_string = our_string.replace(" ", "")
result_string = ""
for i in our_string:
    if i not in result_string:
        result_string = result_string + i
print(result_string)
