"""
Тесты задачи task_1
"""

import pytest
import task1


def test_executive_right_dimensions_tree():
    """Тест dimensions_tree.

    Тест функции dimensions_tree класса NewYearPlace на правильность
    передачи данных.

    """
    t_class = task1.NewYearTreePlace(2.1, 1.3)
    assert t_class.height == 2.1 and t_class.width == 1.3


def test_executive_fault_dimensions_tree():
    """Тест dimensions_tree.

     Тест  dimensions_tree класса NewYearPlace на правильность передачи
     данных (негативный).

     """
    t_class = task1.NewYearTreePlace(2.1, 1.3)
    assert t_class.height != 2.1 or t_class.width != 1.5


def test_pass_argument_newyeartree():
    """Проверка передачи аргументов.

    Проверка передачи аргументов в класс NewYearTree при наследовании
    класса NewYearPlace.

    """
    t_class_place = task1.NewYearTreePlace(2.1, 1.3)
    t_class_tree = task1.NewYearTree(t_class_place.height, t_class_place.width)
    assert t_class_tree.height == 2.1 and t_class_tree.width == 1.3


def test_one_get_choice():
    """Тестирование функции get_choice.

    Тестирование функции get_choice класса RandomChoose при выборе одного
    элемента из списка.

    """
    t_list = [1, 2, 3]
    t_choice = task1.RandomChoose(t_list, 1)
    assert t_choice.get_choice() in t_list


def test_multiple_get_choice():
    """
    Тестирование get_choice.

    Тестирование функции get_choice класса RandomChoose при выборе нескольких
    элементов из списка.

    """
    t_list = [1, 2, 36, 7, 9, 4]
    t_choice = task1.RandomChoose(t_list, 3)
    t_choice_multiply = t_choice.get_choice()
    for item in t_choice_multiply:
        assert item in t_list


def test_multiple_get_choice_type():
    """
    Тестирование get_choice.

    Тестирование типа результата функции get_choice класса RandomChoose
    при выборе нескольких элементов из списка.

    """
    t_list = [1, 2, 36, 7, 9, 4]
    t_choice = task1.RandomChoose(t_list, 3)
    assert isinstance(t_choice.get_choice(), list)


def test_wrong_input_1_get_choice():
    """
    Проверка на ошибку №1 get_choice.

    Проверка возникновения ошибки при передаче в функцию get_choice
    класса RandomChoose неправильного типа данных.

    """
    t_wrong_input = 1
    t_choice = task1.RandomChoose(t_wrong_input, 1)
    with pytest.raises(TypeError):
        t_choice.get_choice()


def test_wrong_input_2_get_choice():
    """
    Проверка на ошибку №2 get_choice.

    Проверка возникновения ошибки при передаче в функцию get_choice
    класса RandomChoose длины выборки, которая больше длины набора,
    из которого делается выборка.

    """
    t_list = [1, 2, 36, 7, 9, 4]
    t_wrong_input = 7
    t_choice = task1.RandomChoose(t_list, t_wrong_input)
    with pytest.raises(ValueError):
        t_choice.get_choice()


def test_right_choose_type_tree():
    """Проверка, что тип елки в функции choose_type_tree выбран корректно."""
    t_class_tree = task1.NewYearTree(2.1, 1.3)
    t_class_tree.choose_type_tree()
    t_type_tree = t_class_tree.type_tree
    assert t_type_tree.find('Жив') != -1 or t_type_tree.find('Искус') != -1


def test_right_move_tree():
    """Проверка, в функции move_tree get_tree_place и my_vehicle выбраны корректно"""
    t_class_tree = task1.NewYearTree(2.1, 1.3)
    t_class_tree.choose_type_tree()
    t_vehicle = t_class_tree.move_tree()
    assert t_class_tree.get_tree_place == 'Гараж' or t_class_tree.get_tree_place == 'Базар'
    assert t_vehicle.vehicle in ['такси', 'своей машине']


def test_right_get_tree(monkeypatch):
    """Проверка, в функции get_tree view_tree выбран корректно"""
    monkeypatch.setattr('builtins.input', lambda temp: 'да')
    t_class_tree = task1.NewYearTree(2.1, 1.3)
    t_view_tree = t_class_tree.get_tree()
    assert t_view_tree in ['облезлая', 'редкая', 'пышная']


def test_right_put_gifts():
    """Тестирование функции put_gifts на работоспособность."""
    t_desires_list = ['наушники', 'краски с кистью', 'плюшевый мишка', 'часы',
                      'кукла', 'духи', 'коньки']
    t_vehicle_list = ['такси', 'своей машине', 'общественном транспорте']
    t_class_tree = task1.NewYearTree(2.1, 1.3)
    t_out_list = t_class_tree.put_gifts()
    assert t_out_list[0] in t_vehicle_list
    assert set(t_out_list[1]) < set(t_desires_list)


def test_wrong_put_gifts():
    """Негативное тестирование работоспособности функции put_gifts."""
    t_desires_list = ['дырокол', 'большая ваза', 'транспарант', 'часы', 'кукла',
                      'духи', 'коньки']
    t_vehicle_list = ['велосипед', 'трактор', 'самолет']
    t_class_tree = task1.NewYearTree(2.1, 1.3)
    t_out_list = t_class_tree.put_gifts()
    assert t_out_list[0] not in t_vehicle_list
    assert not (set(t_out_list[1]) < set(t_desires_list))
