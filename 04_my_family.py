#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Создайте списки:

# моя семья (минимум 3 элемента, есть еще дедушки и бабушки, если что)
my_family = ["Мать", "Отец", "Брат"]

# список списков приблизительного роста членов вашей семьи
my_family_height = [
    ['Мать', 155],
    ['Отец', 180],
    ['Брат', 182]
]


def get_height_of_member(heights, member):
    for name, height in heights:
        if name == member:
            return height
    return None


def get_total_family_height(heights):
    total_height = 0
    for name, height in heights:
        total_height += height
    return total_height


def main():
    # Выведите на консоль рост отца в формате
    #   Рост отца - ХХ см
    print(f"Рост отца - {get_height_of_member(my_family_height, 'Отец')} см")

    # Выведите на консоль общий рост вашей семьи как сумму ростов всех членов
    #   Общий рост моей семьи - ХХ см
    print(f"Общий рост моей семьи - {get_total_family_height(my_family_height)} см")


if __name__ == "__main__":
    main()
