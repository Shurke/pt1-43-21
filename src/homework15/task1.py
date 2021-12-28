"""
Создайте  модель из жизни. Это может быть бронирование комнаты в отеле,
покупка билета в транспортной компании, или простая РПГ.
Создайте несколько объектов классов, которые описывают ситуацию.
Объекты должны содержать как атрибуты так и метода класса для симуляции
различных действий.
Программа должна инстанцировать объекты и эмулировать какую-либо ситуацию -
вызывать методы, взаимодействие объектов и т.д.

Создание модели школы, содержащей классы.
Хранение данных, используя атрибуты родительского singleton-класса школы.
"""

from pprint import pprint


class School:

    instance = None
    school_name = ""
    school_address = ""
    director_name = ""
    director_surname = ""
    classes = []
    total_students = 0

    def __new__(cls, *args, **kwargs):
        if not cls.instance:
            cls.instance = super(School, cls).__new__(cls, *args, **kwargs)
        return cls.instance

    def set_school_name(self, school_name: str):
        self.school_name = school_name

    def set_school_address(self, address: str):
        self.school_address = address

    def get_school_address(self) -> str:
        return self.school_address

    def set_director(self, name: str, surname: str):
        self.director_name = name
        self.director_surname = surname

    def get_director(self) -> str:
        return self.director_name + " " + self.director_surname

    def get_school_info(self) -> dict:
        school_info = {
            'school_name': self.school_name,
            'school_address': self.get_school_address(),
            'director': self.get_director(),
            'classes': self.classes,
            'total_students': self.total_students
        }
        return school_info

    def print_school_info(self):
        school_info = self.get_school_info()
        print("\nИнформация о школе :")
        pprint(school_info)


class SchoolClass:

    school_instance = None
    class_name = ""
    teacher_name = ""
    teacher_surname = ""
    students_qty = 0
    students = None

    def __init__(self, class_name: str):
        self.class_name = class_name
        self.students = []
        self.school_instance = School()
        self.school_instance.classes.append(class_name)

    def set_teacher(self, name: str, surname: str):
        self.teacher_name = name
        self.teacher_surname = surname

    def get_teacher(self) -> str:
        return self.teacher_name + " " + self.teacher_surname

    def set_student(self, student_name: str, student_surname: str, student_age: int):
        student_info = {
            "student_name": student_name,
            "student_surname": student_surname,
            "student_age": student_age
        }
        self.students.append(student_info)
        self.students_qty += 1
        self.school_instance.total_students += 1

    def get_class_info(self) -> dict:
        class_info = {
            "school_name": self.school_instance.school_name,
            "school_address": self.school_instance.get_school_address(),
            "director": self.school_instance.get_director(),
            "class_name": self.class_name,
            "teacher": self.get_teacher(),
            "students_qty": self.students_qty,
            "students": self.students
        }
        return class_info

    def print_class_info(self):
        class_info = self.get_class_info()
        print("\nИнформация о классе", self.class_name, ":")
        pprint(class_info)


school = School()
school.set_school_name("Школа чародейства и волшебства Хогвартс")
school.set_school_address("Шотландия")
school.set_director("Альбус", "Дамблдор")

class_a = SchoolClass("Гриффиндор")
class_a.set_teacher("Минерва", "Макгонагалл")
class_a.set_student("Гарри", "Поттер", 17)
class_a.set_student("Рональд", "Уизли", 18)
class_a.set_student("Гермиона", "Грейнджер", 17)

class_b = SchoolClass("Слизерин")
class_b.set_teacher("Северус", "Снегг")
class_b.set_student("Драко", "Малфой", 18)
class_b.set_student("Маркус", "Флинт", 17)
class_b.set_student("Винсент", "Крэбб", 17)

school.print_school_info()
class_a.print_class_info()
class_b.print_class_info()
