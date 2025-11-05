from src.my_class import Category


def test_Product(electronic_one, electronic_two, electronic_three):
    assert electronic_one.name == "Nokia"
    assert electronic_one.price == 50000.0
    assert electronic_two.name == "Hp"
    assert electronic_three.description == "65 дюймов"


def test_Category(cat_electronic_one, cat_electronic_two):
    assert cat_electronic_one.name == "Телефоны"
    assert len(cat_electronic_one.products) == 2
    assert len(cat_electronic_two.products) == 1
    assert Category.category_count == 2
    assert Category.product_count == 3
