"""Тесты задания 10: количество и стоимость товаров на складе."""

# Позволяет запускать файл напрямую: python tests/test_XX.py
# Корень проекта добавляется в sys.path независимо от pytest.ini
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))


import importlib

store_task = importlib.import_module('10_store')


def test_calculate_totals():
    expected = [
        ('Лампа', 27, 1134),
        ('Стол', 54, 27860),
        ('Диван', 3, 3550),
        ('Стул', 105, 10311),
    ]
    assert store_task.calculate_totals(store_task.goods, store_task.store) == expected


def test_main_prints_totals(capsys):
    store_task.main()
    out = capsys.readouterr().out
    assert 'Лампа - 27 шт, стоимость 1134 руб' in out
    assert 'Стол - 54 шт, стоимость 27860 руб' in out
    assert 'Диван - 3 шт, стоимость 3550 руб' in out
    assert 'Стул - 105 шт, стоимость 10311 руб' in out


# Прямой запуск: python tests/test_XX.py -> тесты выполняются через pytest
if __name__ == "__main__":
    import pytest
    pytest.main([__file__])
