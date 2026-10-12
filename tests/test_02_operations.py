"""Тесты задания 02: знаки операций между числами 1 2 3 4 5."""

import importlib

operations = importlib.import_module('02_operations')


def test_result_is_twenty_five():
    assert operations.compute_result() == 25


def test_main_prints_result(capsys):
    operations.main()
    out = capsys.readouterr().out
    assert '25' in out
