import pytest


def test_Smartphone(smartphone1):
    assert smartphone1.name == "Xiaomi Redmi Note 11"
    assert smartphone1.model == "Note 11"


def test_smartphone_add(smartphone1, smartphone2, lawn_grass1):
    assert smartphone1 + smartphone2 == 1334000
    with pytest.raises(TypeError) as exc_info:
        smartphone1 + lawn_grass1
    assert str(exc_info.value) == "Ожидался Smartphone, а получен LawnGrass"


def test_LawnGrass(lawn_grass1):
    assert lawn_grass1.color == "Темно-зеленый"
    assert lawn_grass1.germination_period == "5 дней"


def test_lawnGrass_add(lawn_grass1, lawn_grass2, smartphone2):
    assert lawn_grass1 + lawn_grass2 == 8250.0
    with pytest.raises(TypeError) as exc_info:
        lawn_grass2 + smartphone2
    assert str(exc_info.value) == "Ожидался LawnGrass, а получен Smartphone"
