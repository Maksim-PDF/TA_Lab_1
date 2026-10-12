"""Тесты задания 01: площадь круга и принадлежность точки кругу."""

import importlib

circle = importlib.import_module('01_circle')


def test_circle_area():
    assert circle.circle_area(42) == 5541.7693


def test_point_inside_circle():
    assert circle.is_point_inside_circle((23, 34), 42) is True


def test_point_outside_circle():
    assert circle.is_point_inside_circle((30, 30), 42) is False


def test_main_prints_results(capsys):
    circle.main()
    out = capsys.readouterr().out
    assert '5541.7693' in out
    assert 'True' in out
    assert 'False' in out
