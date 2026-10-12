#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# В саду сорвали цветы
garden = ('ромашка', 'роза', 'одуванчик', 'ромашка', 'гладиолус', 'подсолнух', 'роза', )

# На лугу сорвали цветы
meadow = ('клевер', 'одуванчик', 'ромашка', 'клевер', 'мак', 'одуванчик', 'ромашка', )

# Создайте множество цветов, произрастающих в саду и на лугу
# garden_set =
# meadow_set =


def analyze_flowers(garden, meadow):
    garden_set = set(garden)
    meadow_set = set(meadow)
    return {
        'all': garden_set | meadow_set,
        'common': garden_set & meadow_set,
        'garden_only': garden_set - meadow_set,
        'meadow_only': meadow_set - garden_set,
    }


def main():
    result = analyze_flowers(garden, meadow)

    # Выведите на консоль все виды цветов
    print(f"Все виды цветов: {result['all']}")

    # Выведите на консоль те, которые растут и там и там
    print(f"Растут и в саду, и на лугу: {result['common']}")

    # Выведите на консоль те, которые растут в саду, но не растут на лугу
    print(f"Растут в саду, но не растут на лугу: {result['garden_only']}")

    # Выведите на консоль те, которые растут на лугу, но не растут в саду
    print(f"Растут на лугу, но не растут в саду: {result['meadow_only']}")

    return result


if __name__ == "__main__":
    main()
