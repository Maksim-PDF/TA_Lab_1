"""Тесты задания 03: выбор фильмов срезами строки."""

import importlib

movies_task = importlib.import_module('03_favorite_movies')


def test_selected_movies():
    assert movies_task.get_selected_movies(movies_task.my_favorite_movies) == (
        'Терминатор',
        'Назад в будущее',
        'Пятый элемент',
        'Чужие',
    )


def test_no_commas_in_output(capsys):
    movies_task.main()
    out = capsys.readouterr().out
    lines = out.strip().splitlines()
    assert len(lines) == 4
    for line in lines:
        assert ',' not in line
