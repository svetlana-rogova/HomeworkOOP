import pytest

from src.my_class import Category, Product


@pytest.fixture
def electronic_one():
    return Product(
        name="Nokia",
        description="256GB",
        price=50000.0,
        quantity=5
    )


@pytest.fixture
def electronic_two():
    return Product(
        name="Hp",
        description="256GB",
        price=150000.0,
        quantity=7
    )


@pytest.fixture
def electronic_three():
    return Product(
        name="Xiaomi",
        description="65 дюймов",
        price=180000.0,
        quantity=2
    )


@pytest.fixture
def cat_electronic_one():
    return Category(
        name="Телефоны",
        description="Смартфоны большим количеством памяти",
        products=[Product(name="Hp", description="1024GB", price=150000.0, quantity=7),
                  Product(name="Nokia", description="1024GB", price=50000.0, quantity=5)]
    )


@pytest.fixture
def cat_electronic_two():
    return Category(
        name="Телевизоры",
        description="С большой диагональю",
        products=[Product(name="Xiaomi", description="65 дюймов", price=180000.0, quantity=2)]
    )


@pytest.fixture()
def dict_product():
    return {
        "name": "Xiaomi",
        "description": "65 дюймов",
        "price": 190000.0,
        "quantity": 5,
    }
