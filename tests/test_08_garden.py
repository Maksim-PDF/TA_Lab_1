"""Тесты задания 08: множества цветов сада и луга."""

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
