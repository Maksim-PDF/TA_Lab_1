#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Есть словарь кодов товаров

goods = {
    'Лампа': '12345',
    'Стол': '23456',
    'Диван': '34567',
    'Стул': '45678',
}

# Есть словарь списков количества товаров на складе.
# Каждый товар может лежать в нескольких местах (партиях) с разной ценой.

store = {
    '12345': [
        {'quantity': 27, 'price': 42},
    ],
    '23456': [
        {'quantity': 22, 'price': 510},
        {'quantity': 32, 'price': 520},
    ],
    '34567': [
        {'quantity': 2, 'price': 1200},
        {'quantity': 1, 'price': 1150},
    ],
    '45678': [
        {'quantity': 50, 'price': 100},
        {'quantity': 12, 'price': 95},
        {'quantity': 43, 'price': 97},
    ],
}


def calculate_totals(goods, store):
    """Рассчитывает количество и стоимость каждого товара на складе.

    Возвращает список кортежей (товар, кол-во шт, стоимость руб).
    Стоимость складывается по всем партиям товара.
    """
    result = []
    for name, code in goods.items():
        total_qty = 0
        total_cost = 0
        for batch in store[code]:
            total_qty += batch['quantity']
            total_cost += batch['quantity'] * batch['price']
        result.append((name, total_qty, total_cost))
    return result


def main():
    for name, total_qty, total_cost in calculate_totals(goods, store):
        print(f"{name} - {total_qty} шт, стоимость {total_cost} руб")
    return calculate_totals(goods, store)


# Защита от автоматического выполнения при импорте модуля
if __name__ == "__main__":
    main()
