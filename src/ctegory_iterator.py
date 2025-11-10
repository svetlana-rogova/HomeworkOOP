class CategoryIterator:
    """Класс для перебора товаров одной категории"""
    def __init__(self, category_obj):
        self.category = category_obj

    def __iter__(self):
        self.index = 0
        return self

    def __next__(self):
        if self.index < len(self.category.products):
            product = self.category.products[self.index]
            self.index += 1
        else:
            raise StopIteration
        return product
