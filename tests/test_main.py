"""Тесты верхнеуровневого модуля main.py: консольное меню."""

# Позволяет запускать файл напрямую: python tests/test_XX.py
# Корень проекта добавляется в sys.path независимо от pytest.ini
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))


import main as main_module


def test_tasks_list_contains_11_tasks():
    assert len(main_module.TASKS) == 11


def test_print_menu_lists_all_tasks(capsys):
    main_module.print_menu()
    out = capsys.readouterr().out
    for number in range(11):
        assert f'{number:>2}. ' in out
    assert 'q' in out


def test_run_task_executes_chosen_module(capsys):
    assert main_module.run_task(0) is True
    out = capsys.readouterr().out
    assert 'Задание 0' in out
    assert 'Moscow' in out


def test_run_task_invalid_number():
    assert main_module.run_task(11) is False
    assert main_module.run_task(-1) is False


def test_menu_quit(monkeypatch, capsys):
    monkeypatch.setattr('builtins.input', lambda prompt='': 'q')
    main_module.main()
    out = capsys.readouterr().out
    assert 'Выход из программы' in out


def test_menu_invalid_input_then_quit(monkeypatch, capsys):
    answers = iter(['99', 'abc', 'q'])
    monkeypatch.setattr('builtins.input', lambda prompt='': next(answers))
    main_module.main()
    out = capsys.readouterr().out
    assert out.count('Ошибка') == 2


def test_menu_runs_task_then_quits(monkeypatch, capsys):
    answers = iter(['2', 'q'])
    monkeypatch.setattr('builtins.input', lambda prompt='': next(answers))
    main_module.main()
    out = capsys.readouterr().out
    assert 'Задание 2' in out
    assert '25' in out


# Прямой запуск: python tests/test_XX.py -> тесты выполняются через pytest
if __name__ == "__main__":
    import pytest
    pytest.main([__file__])
