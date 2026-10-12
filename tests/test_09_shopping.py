"""Тесты задания 09: два магазина с минимальными ценами на сладости."""

# Позволяет запускать файл напрямую: python tests/test_XX.py
# Корень проекта добавляется в sys.path независимо от pytest.ini
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))


import importlib

import pytest

shopping = importlib.import_module('09_shopping')


def _two_cheapest_offers(shops, product):
    """Вычисляет по данным shops два магазина с минимальными ценами."""
    offers = []
    for shop_name, items in shops.items():
        for item in items:
            if item['name'] == product:
                offers.append({'shop': shop_name, 'price': item['price']})
    offers.sort(key=lambda offer: offer['price'])
    return offers[:2]


@pytest.mark.parametrize('product', ['печенье', 'конфеты', 'карамель', 'пирожное'])
def test_sweets_match_two_cheapest_shops(product):
    assert shopping.sweets[product] == _two_cheapest_offers(shopping.shops, product)


def test_sweets_structure_uniform():
    for offers in shopping.sweets.values():
        assert len(offers) == 2
        for offer in offers:
            assert set(offer) == {'shop', 'price'}


def test_main_prints_sweets(capsys):
    shopping.main()
    out = capsys.readouterr().out
    for product in ('печенье', 'конфеты', 'карамель', 'пирожное'):
        assert product in out


# Прямой запуск: python tests/test_XX.py -> тесты выполняются через pytest
if __name__ == "__main__":
    import pytest
    pytest.main([__file__])
