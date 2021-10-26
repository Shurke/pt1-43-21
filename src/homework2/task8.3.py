# You are asked to ensure that the first and last names of people begin with a capital letter
# in their passports.
# For example, alison heck should be capitalised correctly as Alison Heck.
print("Задача приводит ФИО к правильному регистру")
name = input("Введите имя и фамилию: ")
fin_name = name.split()
new_name = ""
for i in fin_name:
    new_name = new_name + " " + i.capitalize()
new_name = new_name.strip()
print(new_name)
