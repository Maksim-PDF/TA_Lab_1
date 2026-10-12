#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Есть список животных в зоопарке
zoo = ['lion', 'kangaroo', 'elephant', 'monkey']

birds = ['rooster', 'ostrich', 'lark']


def arrange_zoo(zoo, birds):
    result = list(zoo)

    # Посадите медведя (bear) между львом и кенгуру
    result.insert(1, 'bear')

    # Добавьте птиц из списка birds в последние клетки зоопарка
    result.extend(birds)

    # Уберите слона (elephant) из зоопарка
    result.remove('elephant')

    return result


def get_cage_number(animals, animal):
    return animals.index(animal) + 1


def main():
    result = arrange_zoo(zoo, birds)
    print(result)

    # Выведите на консоль в какой клетке сидит лев (lion) и жаворонок (lark).
    # Номера при выводе должны быть 1-индексированными (первая клетка - номер 1).
    print(f"lion: {get_cage_number(result, 'lion')}, "
          f"lark: {get_cage_number(result, 'lark')}")


if __name__ == "__main__":
    main()
