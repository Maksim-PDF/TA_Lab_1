#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# В саду сорвали цветы
garden = ('ромашка', 'роза', 'одуванчик', 'ромашка', 'гладиолус', 'подсолнух', 'роза', )

# На лугу сорвали цветы
meadow = ('клевер', 'одуванчик', 'ромашка', 'клевер', 'мак', 'одуванчик', 'ромашка', )


def analyze_flowers(garden, meadow):
    """Возвращает словарь множеств цветов сада и луга.

    Ключи:
        all         - все виды цветов
        common      - растут и в саду, и на лугу
        garden_only - растут в саду, но не на лугу
        meadow_only - растут на лугу, но не в саду
    """
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
    # правка: у каждого вывода своя подпись (в исходнике все были "Все виды цветов")
    print(f"Все виды цветов: {result['all']}")
    print(f"Растут и в саду, и на лугу: {result['common']}")
    print(f"Растут в саду, но не растут на лугу: {result['garden_only']}")
    print(f"Растут на лугу, но не растут в саду: {result['meadow_only']}")
    return result


# Защита от автоматического выполнения при импорте модуля
if __name__ == "__main__":
    main()
