"""Тесты задания 05: животные в зоопарке."""

# Позволяет запускать файл напрямую: python tests/test_XX.py
# Корень проекта добавляется в sys.path независимо от pytest.ini
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))


import importlib

zoo_task = importlib.import_module('05_zoo')


def test_arrange_zoo_final_state():
    result = zoo_task.arrange_zoo(zoo_task.zoo, zoo_task.birds)
    assert result == [
        'lion', 'bear', 'kangaroo', 'monkey', 'rooster', 'ostrich', 'lark',
    ]


def test_arrange_zoo_does_not_mutate_input():
    original = list(zoo_task.zoo)
    zoo_task.arrange_zoo(zoo_task.zoo, zoo_task.birds)
    assert zoo_task.zoo == original


def test_cage_numbers_are_one_indexed():
    result = zoo_task.arrange_zoo(zoo_task.zoo, zoo_task.birds)
    assert zoo_task.get_cage_number(result, 'lion') == 1
    assert zoo_task.get_cage_number(result, 'lark') == 7


def test_main_prints_result(capsys):
    zoo_task.main()
    out = capsys.readouterr().out
    assert 'lion: 1' in out
    assert 'lark: 7' in out


# Прямой запуск: python tests/test_XX.py -> тесты выполняются через pytest
if __name__ == "__main__":
    import pytest
    pytest.main([__file__])
