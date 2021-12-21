"""Tests for task1.py."""

import unittest
from task1 import School, SchoolClass


class TestSchoolMethods(unittest.TestCase):

    def test_school_instances(self):
        """singleton check"""
        instance1 = School()
        instance2 = School()
        self.assertIs(instance1, instance2)

    def test_school_address(self):
        """check for string"""
        school_address = School().get_school_address()
        self.assertTrue(isinstance(school_address, str))
        self.assertFalse(isinstance(school_address, int))

    def test_director_name(self):
        """director's name in two words"""
        director_name = School().get_director()
        self.assertTrue(len(director_name.split()) == 2)
        self.assertFalse(len(director_name.split()) != 2)

    def test_total_students(self):
        """test total_students"""
        total_students = School().total_students
        classes = School().classes
        self.assertTrue(isinstance(total_students, int))
        if total_students > 0:
            self.assertTrue(len(classes) > 0)


class TestSchoolClassMethods(unittest.TestCase):

    def test_school_class_instances(self):
        """School singleton check"""
        self.assertIs(SchoolClass("Test class name").school_instance, School())

    def test_class_in_school(self):
        """test class name"""
        self.assertTrue(SchoolClass("Test class name").class_name in School().classes)

    def test_class_teacher(self):
        """test teacher"""
        class_name = "Test class name"
        if len(School().classes) > 0:
            class_name = School().classes[0]
        teacher = SchoolClass(class_name).get_teacher()
        self.assertTrue(isinstance(teacher, str))

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
