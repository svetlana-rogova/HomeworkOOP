class Product:
    """Класс для представления продуктов"""

    name: str
    description: str
    price: float
    quantity: int

    def __init__(self, name, description, price, quantity):
        self.name = name
        self.description = description
        self.__price = price
        self.quantity = quantity

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


class Category:
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

    @property
    def products(self):
        product_list = ""
        for el in self.__products:
            product_list += f"{el.name}, {el.price} руб. Остаток: {el.quantity} шт.\n"
        return product_list

    def add_product(self, products: Product):
        self.__products.append(products)
        Category.product_count += 1
