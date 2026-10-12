"""Тесты задания 09: два магазина с минимальными ценами на сладости."""

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
