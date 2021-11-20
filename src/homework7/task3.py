"""
Реализовать функцию get_ranges которая получает на вход
непустой список неповторяющихся целых чисел,
отсортированных по возрастанию, которая этот список “сворачивает”
get_ranges([0, 1, 2, 3, 4, 7, 8, 10]) // "0-4,7-8,10"
get_ranges([4,7,10]) // "4,7,10"
 get_ranges([2, 3, 8, 9]) // "2-3,8-9"
"""


def get_ranges(some_list):
    my_list = some_list.split()
    i = 0
    my_string = f"{my_list[0]}"
    loc_string = ""
    while i < len(my_list) - 1:
        if int(my_list[i + 1]) - int(my_list[i]) == 1:
            while i < len(my_list) - 1 and int(my_list[i + 1]) - int(my_list[i]) == 1:
                loc_string = f"-{my_list[i + 1]}"
                i += 1
            my_string = my_string + loc_string
            loc_string = ""
        elif int(my_list[i + 1]) - int(my_list[i]) != 1:
            my_string = my_string + f", {my_list[i + 1]}"
            i += 1
        else:
            my_string = my_string + ", "
            i += 1
    print(f"Не свернутый список: {some_list}")
    print(f"Cвернутый список: {my_string}")


test = input("Введите не повторяющиеся числа в порядке возрастания через пробел:\n")
get_ranges(test)
