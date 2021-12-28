"""Tests for task1.py."""

from task1 import School
from task1 import SchoolClass
import unittest


class TestSchoolMethods(unittest.TestCase):

    def setUp(self):
        self.school = School()

    def test_school_instances(self):
        """singleton check"""
        instance1 = self.school
        instance2 = School()
        self.assertIs(instance1, instance2)

    def test_school_address(self):
        """check for string"""
        school_address = self.school.get_school_address()
        self.assertIs(type(school_address), str)

    def test_director_name(self):
        """director's name in two words"""
        director_name = self.school.get_director()
        self.assertTrue(len(director_name.split()) == 2)

    def test_total_students(self):
        """test total_students and the existence of classes"""
        total_students = self.school.total_students
        classes = self.school.classes
        self.assertIs(type(total_students), int)
        if total_students > 0:
            self.assertTrue(len(classes) > 0)


class TestSchoolClassMethods(unittest.TestCase):

    def setUp(self):
        self.school_class = SchoolClass("Test class name")

    def test_school_class_instances(self):
        """School singleton check"""
        self.assertIs(self.school_class.school_instance, School())

    def test_class_in_school(self):
        """testing the availability of a class at school"""
        self.assertTrue(self.school_class.class_name in School().classes)

    def test_class_teacher(self):
        """test teacher"""
        class_name = "Test class name"
        if len(School().classes) > 0:
            class_name = School().classes[0]
        teacher = SchoolClass(class_name).get_teacher()
        self.assertIs(type(teacher), str)

    def test_class_students(self):
        """test class students"""
        class_name = "Test class name"
        if len(School().classes) > 0:
            class_name = School().classes[0]
        school_class = SchoolClass(class_name)
        if school_class.students_qty > 0:
            self.assertTrue(School().total_students > 0)


if __name__ == '__main__':
    unittest.main()
