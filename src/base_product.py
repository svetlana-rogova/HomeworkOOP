from abc import ABC, abstractmethod


class BaseProduct(ABC):

    @classmethod
    @abstractmethod
    def new_product(cls, dict_product, category):
        pass

    @abstractmethod
    def __add__(self, other):
        pass
