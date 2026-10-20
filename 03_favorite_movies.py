#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Есть строка с перечислением фильмов

my_favorite_movies = 'Терминатор, Пятый элемент, Аватар, Чужие, Назад в будущее'

# Выведите на консоль с помощью индексации строки, последовательно:
#   первый фильм
#   последний
#   второй
#   второй с конца

# Запятая не должна выводиться. Переопределять my_favorite_movies нельзя.
# Использовать .split() или .find() или другие методы строки нельзя - пользуйтесь только срезами,
# как указано в задании!


def get_selected_movies(movies):
    return (
        movies[:10],
        movies[42:],
        movies[12:25],
        movies[35:40],
    )


def main():
    for movie in get_selected_movies(my_favorite_movies):
        print(movie)


if __name__ == "__main__":
    main()
