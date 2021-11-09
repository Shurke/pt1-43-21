"""
Каждый из N школьников некоторой школы знает M языков.
Определите, какие языки знают все школьники и языки,
которые знает хотя бы один из школьников.
"""


print("Программа считает сколько языков знают все школьники "
      "и сколько языков знает хотя бы один")
number_of_students = int(input("Введите количество учеников, "
                               "с которым хотите работать: "))
i = 0
j = 0
list_of_languages = []
set_of_languages = set()
new_set_of_languages = set()
gen_set_of_languages = set()
while i < number_of_students:
    number_of_languages = int(input(f"Введите количество языков ученика №{i + 1}: "))
    new_set_of_languages = set()
    while j < number_of_languages:
        language = input(f"Язык №{j + 1}: ")
        set_of_languages.add(language)
        new_set_of_languages.add(language)
        j += 1
    if len(gen_set_of_languages) == 0:
        gen_set_of_languages = new_set_of_languages
    else:
        gen_set_of_languages = gen_set_of_languages & new_set_of_languages
    i += 1
    j = 0
print("\nЯзыки, которые знает хотя бы один студент:")
list_of_languages = list(set_of_languages)
list_of_languages.sort()
for language in list_of_languages:
    print(language)
print("\nЯзыки, которые знают все студенты:")
list_of_languages = list(gen_set_of_languages)
if len(list_of_languages) == 0:
    print("Общих для всех студентов языков нет!")
else:
    for language in list_of_languages:
        print(language)
