from src.base_product import BaseOrderCategory, BaseProduct
from src.class_except import ZeroQuantityProduct
from src.print_mixin import Mixin


class Product(BaseProduct, Mixin):
    """Класс для представления продуктов"""

    name: str
    description: str
    price: float
    quantity: int

    def __init__(self, name, description, price, quantity):
        self.name = name
        self.description = description
        self.__price = price
        if quantity == 0:
            raise ValueError("Товар с нулевым количеством не может быть добавлен")
        self.quantity = quantity
        super().__init__()

    def __str__(self):
        return f"{self.name}, {self.__price} руб. Остаток: {self.quantity} шт."

    def __add__(self, other):
        if type(other) is type(self):
            return self.price * self.quantity + other.price * other.quantity
        raise TypeError(f"Ожидался {type(self).__name__}, а получен {type(other).__name__}")

    @classmethod
    def new_product(cls, dict_product, category):
        for product in category._Category__products:
            if product.name == dict_product["name"]:
                product.quantity += dict_product["quantity"]
            if dict_product["price"] > product.price:
                product.price = dict_product["price"]
            return product

        return cls(
            name=dict_product["name"],
            description=dict_product["description"],
            price=dict_product["price"],
            quantity=dict_product["quantity"],
        )

    @property
    def price(self):
        return self.__price

    @price.setter
    def price(self, new_price):
        if new_price <= 0:
            print("Цена не должна быть нулевая или отрицательная")
            return
        elif self.__price > new_price:
            answer = input("Вы действительно хотите уменьшить цену товара?\nВведите 'y' если да.")
            if answer != "y":
                return
        self.__price = new_price


class Category(BaseOrderCategory):
    """Класс для представления категорий"""

    name: str
    description: str
    products: list

    category_count = 0
    product_count = 0

    def __init__(self, name, description, products):
        self.name = name
        self.description = description
        self.__products = products
        Category.category_count += 1
        Category.product_count += len(products) if products else 0

    def __str__(self):
        sum_prod = 0
        for prod in self.__products:
            sum_prod += prod.quantity
        return f"{self.name}, количество продуктов: {sum_prod} шт."

    @property
    def products(self):
        return self.__products

    def products_str(self):
        product_str = ""
        for el in self.__products:
            product_str += f"{str(el)}\n"
        return product_str

    def add_product(self, product: Product):
        if isinstance(product, Product):
            try:
                if product.quantity == 0:
                    raise ZeroQuantityProduct("Нельзя добавлять пробукт с нулевым количеством")
            except ZeroQuantityProduct as e:
                print(str(e))
            else:
                self.__products.append(product)
                Category.product_count += 1
                print("Продукт добавлен")
            finally:
                print("Обработка добавления продукта в категорию завершена")
        else:
            raise TypeError

    @property
    def product_list(self):
        return self.__products

    def middle_price(self):
        sum_price_prod = 0
        for prod in self.__products:
            sum_price_prod += prod.price
        try:
            average_price = sum_price_prod/len(self.__products)
        except ZeroDivisionError:
            return 0
        else:
            return average_price
        finally:
            print("Обработка расчета средней цены завершена")
