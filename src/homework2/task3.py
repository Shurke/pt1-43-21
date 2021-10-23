my_string = input()
my_string = my_string.replace(" ", "")
new_string = ""
for i in my_string:
    if i not in new_string:
        new_string = new_string + i
print(new_string)
