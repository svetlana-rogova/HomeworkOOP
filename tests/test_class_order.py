from src.class_order import Order


def test_Order(product1, lawn_grass1):
    answer = Order(product1)
    assert str(answer) == "Xiaomi Redmi Note 11, количество продуктов: 14 шт., итоговая стоимость: 434000.0 руб."
    assert answer.order_count == 1
    answer2 = Order(lawn_grass1)
    assert str(answer2) == "Газонная трава 2, количество продуктов: 15 шт., итоговая стоимость: 6750.0 руб."
    assert answer2.order_count == 2
