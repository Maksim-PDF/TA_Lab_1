#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Создайте списки:

# моя семья (минимум 3 элемента, есть еще дедушки и бабушки, если что)
my_family = ["Мать", "Отец", "Брат"]

# список списков приблизительного роста членов вашей семьи
my_family_height = [
    ['Мать', 155],
    ['Отец', 180],
    ['Брат', 182],
]


def get_height_of_member(heights, member):
    """Возвращает рост члена семьи по имени."""
    for name, height in heights:
        if name == member:
            return height
    return None


def get_total_family_height(heights):
    """Возвращает общий рост семьи как сумму ростов всех членов."""
    total_height = 0
    for name, height in heights:
        total_height += height
    return total_height


def main():
    print(f"Рост отца - {get_height_of_member(my_family_height, 'Отец')} см")
    print(f"Общий рост моей семьи - {get_total_family_height(my_family_height)} см")


# Защита от автоматического выполнения при импорте модуля
if __name__ == "__main__":
    main()
