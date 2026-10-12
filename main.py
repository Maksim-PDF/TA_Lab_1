#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""Верхнеуровневый модуль лабораторной работы.

Предоставляет консольное меню для запуска любого из 11 заданий.
Задания подключаются через importlib, поэтому при запуске меню
их код не выполняется автоматически - только по выбору пользователя.
"""

import importlib

# (имя модуля, краткое описание задания)
TASKS = [
    ('00_distance', 'Расстояния между городами (словари)'),
    ('01_circle', 'Площадь круга и точка в круге (числа)'),
    ('02_operations', 'Знаки операций между числами 1 2 3 4 5 (числа)'),
    ('03_favorite_movies', 'Выбор фильмов срезами строки (строки)'),
    ('04_my_family', 'Рост членов семьи (списки)'),
    ('05_zoo', 'Животные в зоопарке (списки)'),
    ('06_songs_list', 'Время звучания песен (списки и словари)'),
    ('07_secret', 'Расшифровка секретного сообщения (строки)'),
    ('08_garden', 'Цветы сада и луга (множества)'),
    ('09_shopping', 'Минимальные цены на сладости (словари)'),
    ('10_store', 'Товары на складе (словари)'),
]

EXIT_CHOICES = ('q', 'й', 'quit', 'exit', 'выход')


def print_menu():
    """Печатает меню со списком всех заданий."""
    print()
    print('=' * 64)
    print('  ЛАБОРАТОРНАЯ РАБОТА: базовые типы данных и конструкции Python')
    print('=' * 64)
    for number, (module_name, description) in enumerate(TASKS):
        print(f'  {number:>2}. {description}')
    print('=' * 64)
    print('   q - выход из программы')


def run_task(number):
    """Запускает задание с номером number (0..10).

    Возвращает True, если задание найдено и выполнено,
    иначе False (некорректный номер).
    """
    if not isinstance(number, int) or not 0 <= number < len(TASKS):
        return False
    module_name, description = TASKS[number]
    print()
    print(f'--- Задание {number}: {description} ---')
    module = importlib.import_module(module_name)
    module.main()
    return True


def main():
    """Основной цикл консольного меню."""
    while True:
        print_menu()
        try:
            choice = input('Введите номер задания (q - выход): ').strip().lower()
        except (KeyboardInterrupt, EOFError):
            print('\nВыход из программы. Пока!')
            break

        if choice in EXIT_CHOICES:
            print('Выход из программы. Пока!')
            break

        if not choice.isdigit() or not run_task(int(choice)):
            print(f'\nОшибка: введите число от 0 до {len(TASKS) - 1} или q для выхода.')


# Защита от автоматического выполнения при импорте модуля
if __name__ == "__main__":
    main()
