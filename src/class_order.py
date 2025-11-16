from src.base_product import BaseOrderCategory


class Order(BaseOrderCategory):
    """Класс принимает ссылку на товар и выводит информацию о заказе: товар, количество и итоговую стоимость """

    order_count = 0

    def __init__(self, product):
        self.product = product
        Order.order_count += 1

    def __str__(self):
        sum_prod = self.product.price * self.product.quantity
        return (f"{self.product.name}, количество продуктов: {self.product.quantity} шт., итоговая стоимость:"
                f" {sum_prod} руб.")
