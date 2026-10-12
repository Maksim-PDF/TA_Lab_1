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

# Рассчитать на какую сумму лежит каждого товара на складе
# и вывести в формате
#   <товар> - <кол-во> шт, стоимость <сумма> руб

# Пример:
#   Лампа - 27 шт, стоимость 1134 руб
'''
for code, batches in store.items():
    if code == '12345':
        sum_qty = 0
        for good in batches:
            qty = good['quantity']
            price = good['price']
            sum_1 = sum_qty + qty
        result = sum_qty * price
        print(f"{12345} - {qty} шт, стоимость {result} руб")
    if code == '23456':
        sum_qty = 0
        for good in batches:
            qty = good['quantity']
            price = good['price']
            sum_qty = sum_qty + qty
        result = sum_qty * price
        print(f"{23456} - {qty} шт, стоимость {result} руб")                        
    if code == '34567':
        sum_qty = 0
        for good in batches:
            qty = good['quantity']
            price = good['price']
            sum_qty = sum_qty + qty
        result = sum_qty * price
        print(f"{34567} - {qty} шт, стоимость {result} руб")
    if code == '45678':
        sum_qty = 0
        for good in batches:
            qty = good['quantity']
            price = good['price']
            sum_qty = sum_qty + qty
        result = sum_qty * price
        print(f"{45678} - {qty} шт, стоимость {result} руб")   
'''

for name, code in goods.items():
    total_qty = 0
    total_cost = 0
    for batch in store[code]:
        total_qty += batch['quantity']
        total_cost += batch['quantity'] * batch['price']
    print(f"{name} - {total_qty} шт, стоимость {total_cost} руб")