from src.base_product import BaseOrderCategory
from src.class_except import ZeroQuantityProduct


class Order(BaseOrderCategory):
    """Класс принимает ссылку на товар и выводит информацию о заказе: товар, количество и итоговую стоимость """

    order_count = 0

    def __init__(self, product):
        try:
            self.product = product
            if product.quantity == 0:
                raise ZeroQuantityProduct("Нельзя добавлять пробукт с нулевым количеством")
        except ZeroQuantityProduct as e:
            print(str(e))
        else:
            Order.order_count += 1
            print("Количество товара не равно нулю, можем добавлять в заказ")
        finally:
            print("Обработка данных продукта по количеству завершена")

    def __str__(self):
        sum_prod = self.product.price * self.product.quantity
        return (f"{self.product.name}, количество продуктов: {self.product.quantity} шт., итоговая стоимость:"
                f" {sum_prod} руб.")
