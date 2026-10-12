"""Тесты задания 04: рост членов семьи."""

import importlib

family = importlib.import_module('04_my_family')


def test_father_height():
    assert family.get_height_of_member(family.my_family_height, 'Отец') == 180


def test_total_family_height():
    assert family.get_total_family_height(family.my_family_height) == 517


def test_main_prints_heights(capsys):
    family.main()
    out = capsys.readouterr().out
    assert 'Рост отца - 180 см' in out
    assert 'Общий рост моей семьи - 517 см' in out
