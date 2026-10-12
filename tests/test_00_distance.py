"""Тесты задания 00: словарь словарей расстояний между городами."""

# Позволяет запускать файл напрямую: python tests/test_XX.py
# Корень проекта добавляется в sys.path независимо от pytest.ini
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))


import importlib
import math

import pytest

distance = importlib.import_module('00_distance')


def test_distances_between_known_cities():
    distances = distance.compute_distances(distance.sites)
    assert distances['Moscow']['London'] == pytest.approx(math.sqrt(21200))
    assert distances['Moscow']['Paris'] == pytest.approx(math.sqrt(17000))
    assert distances['London']['Paris'] == pytest.approx(math.sqrt(1800))


def test_distances_symmetric_and_no_self_distance():
    distances = distance.compute_distances(distance.sites)
    for city1 in distance.sites:
        assert city1 not in distances[city1]
        for city2 in distance.sites:
            if city1 != city2:
                assert distances[city1][city2] == pytest.approx(distances[city2][city1])


def test_main_prints_distances(capsys):
    distance.main()
    out = capsys.readouterr().out
    assert 'Moscow' in out and 'London' in out and 'Paris' in out


# Прямой запуск: python tests/test_XX.py -> тесты выполняются через pytest
if __name__ == "__main__":
    import pytest
    pytest.main([__file__])
