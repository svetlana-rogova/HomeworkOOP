from abc import ABC, abstractmethod


class BaseProduct(ABC):
    """Абстрактный класс для выделения общей функциональности, которая должна быть у каждого продукта"""

    @classmethod
    @abstractmethod
    def new_product(cls, dict_product, category):
        pass

    @abstractmethod
    def __add__(self, other):
        pass


class BaseOrderCategory(ABC):
    """Абстрактный класс для выделения общей функциональности, которая должна быть у каждого заказа и категории"""

    @abstractmethod
    def __str__(self):
        pass
