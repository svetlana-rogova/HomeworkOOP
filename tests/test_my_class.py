from unittest.mock import patch

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
    assert cat_electronic_one.products == 'Hp, 150000.0 руб. Остаток: 7 шт.\nNokia, 50000.0 руб. Остаток: 5 шт.\n'
