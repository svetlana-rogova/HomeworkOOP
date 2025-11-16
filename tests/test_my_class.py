from unittest.mock import patch

import pytest

from src.ctegory_iterator import CategoryIterator
from src.my_class import Category, Product


def test_Product(electronic_one, electronic_two, electronic_three):
    assert electronic_one.name == "Nokia"
    assert electronic_one.price == 50000.0
    assert electronic_two.name == "Hp"
    assert electronic_three.description == "65 дюймов"


def test_Category(cat_electronic_one, cat_electronic_two):
    assert cat_electronic_one.name == "Телефоны"
    assert len(cat_electronic_one.product_list) == 2
    assert len(cat_electronic_two.product_list) == 1
    assert Category.category_count == 2
    assert Category.product_count == 3


def test_new_product(dict_product, cat_electronic_two):
    answer = Product.new_product(dict_product, cat_electronic_two)
    assert answer.name == "Xiaomi"
    assert answer.quantity == 7
    assert answer.price == 190000.0


def test_price(electronic_two):
    electronic_two.price = 1500000.0
    assert electronic_two.price == 1500000.0
    electronic_two.price = 0
    assert electronic_two.price == 1500000.0


def test_price_two(electronic_two):
    with patch('builtins.input', return_value='y'):
        electronic_two.price = 1
        assert electronic_two.price == 1


def test_price_(electronic_two):
    with patch('builtins.input', return_value='n'):
        electronic_two.price = 1
        assert electronic_two.price == 150000.0


def test_products_property(cat_electronic_one):
    assert cat_electronic_one.products_str() == ('Hp, 150000.0 руб. Остаток: 7 шт.\nNokia, 50000.0 руб. '
                                                 'Остаток: 5 шт.\n')


def test_CategoryIterator(cat_electronic_one):
    list_answer = [str(el) for el in CategoryIterator(cat_electronic_one)]
    assert list_answer == [
        "Hp, 150000.0 руб. Остаток: 7 шт.",
        "Nokia, 50000.0 руб. Остаток: 5 шт."
    ]


def test_products_str(electronic_three):
    assert str(electronic_three) == "Xiaomi, 180000.0 руб. Остаток: 2 шт."


def test_category_str(cat_electronic_one):
    assert str(cat_electronic_one) == "Телефоны, количество продуктов: 12 шт."


def test_products_add(electronic_one, electronic_two):
    assert electronic_one + electronic_two == 1300000.0


def test_products_add_two(electronic_one, cat_electronic_one):
    with pytest.raises(TypeError) as exc_info:
        electronic_one + cat_electronic_one
    assert str(exc_info.value) == "Ожидался Product, а получен Category"


def test_add_product(cat_smartphon, product1):
    cat_smartphon.add_product(product1)
    assert len(cat_smartphon.products) == 2
    with pytest.raises(TypeError):
        cat_smartphon.add_product("Not a product")
