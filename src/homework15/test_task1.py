'''
Tests for homework15 task1
'''

import pytest
import task1


def test_npc_choice_positive():
    '''Test random npc choice in range'''

    test_class = task1.Npc
    assert test_class.choice() in range(1, 4)


def test_npc_choice_negative():
    '''Test random npc choice in range'''

    test_class = task1.Npc
    assert test_class.choice() in range(-1, 0)


def test_npc_name_positive():
    '''Test npc name in list'''

    test_list = ['Шелдон', 'Пенни', 'Говард']
    test_class = task1.Npc
    assert test_class.name() in test_list


def test_npc_name_negative():
    '''Test npc name in list'''

    test_list = ['A', 'B', 'C']
    test_class = task1.Npc
    assert test_class.name() in test_list


def test_session_init_positive():
    '''Test  positive init session class'''

    test_class = task1.Session(1, 3)
    assert test_class.win1 == 1 and test_class.win2 == 3


def test_session_init_negative():
    '''Test negative init session class'''

    test_class = task1.Session(1, 3)
    assert test_class.win1 != 1 or test_class.win2 != 2


def test_session_get_score_positive():
    '''Test session.getscore'''

    test_class = task1.Session(1, 3)
    assert test_class.get_score() == (1, 3)


def test_session_get_score_negative():
    '''Test session.getscore'''

    test_class = task1.Session(1, 3)
    assert test_class.get_score() != (1, 5)
