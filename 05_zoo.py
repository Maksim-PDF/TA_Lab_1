#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Есть список животных в зоопарке
zoo = ['lion', 'kangaroo', 'elephant', 'monkey']

# Птицы для заселения в последние клетки зоопарка
birds = ['rooster', 'ostrich', 'lark']


def arrange_zoo(zoo, birds):
    """Выполняет все операции задания и возвращает итоговый список.

    1. Медведь (bear) садится между львом и кенгуру.
    2. Птицы добавляются в последние клетки зоопарка.
    3. Слон (elephant) убирается из зоопарка.
    """
    result = list(zoo)
    result.insert(1, 'bear')
    result.extend(birds)
    result.remove('elephant')
    return result


def get_cage_number(animals, animal):
    """Возвращает 1-индексированный номер клетки животного."""
    return animals.index(animal) + 1


def main():
    result = arrange_zoo(zoo, birds)
    print(result)
    print(f"lion: {get_cage_number(result, 'lion')}, "
          f"lark: {get_cage_number(result, 'lark')}")


# Защита от автоматического выполнения при импорте модуля
if __name__ == "__main__":
    main()
