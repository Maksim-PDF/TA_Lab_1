#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Есть список песен группы Depeche Mode со временем звучания с точностью до долей минут

violator_songs_list = [
    ['World in My Eyes', 4.86],
    ['Sweetest Perfection', 4.43],
    ['Personal Jesus', 4.56],
    ['Halo', 4.9],
    ['Waiting for the Night', 6.07],
    ['Enjoy the Silence', 4.20],
    ['Policy of Truth', 4.76],
    ['Blue Dress', 4.29],
    ['Clean', 5.83],
]

# Есть словарь песен группы Depeche Mode
violator_songs_dict = {
    'World in My Eyes': 4.76,
    'Sweetest Perfection': 4.43,
    'Personal Jesus': 4.56,
    'Halo': 4.30,
    'Waiting for the Night': 6.07,
    'Enjoy the Silence': 4.6,
    'Policy of Truth': 4.88,
    'Blue Dress': 4.18,
    'Clean': 5.68,
}


def get_total_duration(songs, titles):
    """Возвращает суммарное время звучания песен из titles.

    songs - список пар [название, время] или словарь {название: время}.
    Суммирование чисел с плавающей точкой может давать погрешность,
    поэтому результат округляется до 3 знаков после запятой.
    """
    total_time = 0
    if isinstance(songs, dict):
        items = songs.items()
    else:
        items = songs
    for name, time in items:
        if name in titles:
            total_time += time
    return round(total_time, 3)


def main():
    total_time = get_total_duration(
        violator_songs_list, ('Halo', 'Enjoy the Silence', 'Clean'))
    print(f"Три песни звучат {total_time} минут")

    # правка: вторая часть задания считается по словарю violator_songs_dict,
    # а не по списку, и выводится фраза "А другие три песни звучат ..."
    other_total_time = get_total_duration(
        violator_songs_dict, ('Sweetest Perfection', 'Policy of Truth', 'Blue Dress'))
    print(f"А другие три песни звучат {other_total_time} минут")


# Защита от автоматического выполнения при импорте модуля
if __name__ == "__main__":
    main()
