import pytest

from src.my_class import Category, Product
from src.new_class_Product import LawnGrass, Smartphone


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


@pytest.fixture
def cat_smartphon():
    return Category(
        "Смартфоны",
        "Смартфоны, как средство не только коммуникации, но и получения дополнительных функций для удобства жизни",
        [Product("Iphone 15", "512GB, Gray space", 210000.0, 8)]
    )


@pytest.fixture
def product1():
    return Product("Xiaomi Redmi Note 11", "1024GB, Синий", 31000.0, 14)


@pytest.fixture
def dict_product():
    return {
        "name": "Xiaomi",
        "description": "65 дюймов",
        "price": 190000.0,
        "quantity": 5,
    }


@pytest.fixture
def lawn_grass1():
    return LawnGrass("Газонная трава 2", "Выносливая трава", 450.0, 15, "США", "5 дней", "Темно-зеленый")


@pytest.fixture
def lawn_grass2():
    return LawnGrass("Газонная трава", "Выносливая трава", 150.0, 10, "Германия", "15 дней", "Зеленый")


@pytest.fixture
def smartphone1():
    return Smartphone("Xiaomi Redmi Note 11", "1024GB, Синий", 31000.0, 14, 90.3, "Note 11", 1024, "Синий")


@pytest.fixture
def smartphone2():
    return Smartphone("Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5,
                      95.5, "S23 Ultra", 256, "Серый"
                      )
