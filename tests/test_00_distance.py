"""Тесты задания 00: словарь словарей расстояний между городами."""

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
