"""Тесты задания 06: суммарное время звучания песен."""

# Позволяет запускать файл напрямую: python tests/test_XX.py
# Корень проекта добавляется в sys.path независимо от pytest.ini
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))


import importlib

songs_task = importlib.import_module('06_songs_list')


def test_total_duration_by_list():
    total = songs_task.get_total_duration(
        songs_task.violator_songs_list, ('Halo', 'Enjoy the Silence', 'Clean'))
    assert total == 14.93


def test_total_duration_by_dict():
    total = songs_task.get_total_duration(
        songs_task.violator_songs_dict,
        ('Sweetest Perfection', 'Policy of Truth', 'Blue Dress'))
    assert total == 13.49


def test_main_prints_both_totals(capsys):
    songs_task.main()
    out = capsys.readouterr().out
    assert 'Три песни звучат 14.93 минут' in out
    assert 'А другие три песни звучат 13.49 минут' in out


# Прямой запуск: python tests/test_XX.py -> тесты выполняются через pytest
if __name__ == "__main__":
    import pytest
    pytest.main([__file__])
