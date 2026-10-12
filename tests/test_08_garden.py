"""Тесты задания 08: множества цветов сада и луга."""

# Позволяет запускать файл напрямую: python tests/test_XX.py
# Корень проекта добавляется в sys.path независимо от pytest.ini
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))


import importlib

garden_task = importlib.import_module('08_garden')


def test_all_flowers():
    result = garden_task.analyze_flowers(garden_task.garden, garden_task.meadow)
    assert result['all'] == {
        'ромашка', 'роза', 'одуванчик', 'гладиолус', 'подсолнух', 'клевер', 'мак',
    }


def test_common_flowers():
    result = garden_task.analyze_flowers(garden_task.garden, garden_task.meadow)
    assert result['common'] == {'ромашка', 'одуванчик'}


def test_garden_only_flowers():
    result = garden_task.analyze_flowers(garden_task.garden, garden_task.meadow)
    assert result['garden_only'] == {'роза', 'гладиолус', 'подсолнух'}


def test_meadow_only_flowers():
    result = garden_task.analyze_flowers(garden_task.garden, garden_task.meadow)
    assert result['meadow_only'] == {'клевер', 'мак'}


def test_main_prints_four_sections(capsys):
    garden_task.main()
    out = capsys.readouterr().out
    assert 'Все виды цветов' in out
    assert 'и в саду, и на лугу' in out
    assert 'в саду, но не растут на лугу' in out
    assert 'на лугу, но не растут в саду' in out


# Прямой запуск: python tests/test_XX.py -> тесты выполняются через pytest
if __name__ == "__main__":
    import pytest
    pytest.main([__file__])
