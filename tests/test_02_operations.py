"""Тесты задания 02: знаки операций между числами 1 2 3 4 5."""

# Позволяет запускать файл напрямую: python tests/test_XX.py
# Корень проекта добавляется в sys.path независимо от pytest.ini
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))


import importlib

operations = importlib.import_module('02_operations')


def test_result_is_twenty_five():
    assert operations.compute_result() == 25


def test_main_prints_result(capsys):
    operations.main()
    out = capsys.readouterr().out
    assert '25' in out


# Прямой запуск: python tests/test_XX.py -> тесты выполняются через pytest
if __name__ == "__main__":
    import pytest
    pytest.main([__file__])
