#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Есть значение радиуса круга
radius = 42

# Пи возьмём равным 3.1415926, точность задаётся в функции round()
PI = 3.1415926


def circle_area(radius):
    """Возвращает площадь круга с точностью до 4-х знаков после запятой."""
    return round(PI * radius ** 2, 4)


def is_point_inside_circle(point, radius):
    """Определяет, лежит ли точка внутри круга с центром в (0, 0).

    Расстояние от точки до начала координат:
    (x ** 2 + y ** 2) ** 0.5
    """
    x, y = point
    d = (x ** 2 + y ** 2) ** 0.5
    return d <= radius


def main():
    print(circle_area(radius))
    print(is_point_inside_circle((23, 34), radius))
    print(is_point_inside_circle((30, 30), radius))


# Защита от автоматического выполнения при импорте модуля
if __name__ == "__main__":
    main()
