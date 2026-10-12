"""Тесты задания 04: рост членов семьи."""

# Позволяет запускать файл напрямую: python tests/test_XX.py
# Корень проекта добавляется в sys.path независимо от pytest.ini
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))


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


# Прямой запуск: python tests/test_XX.py -> тесты выполняются через pytest
if __name__ == "__main__":
    import pytest
    pytest.main([__file__])
