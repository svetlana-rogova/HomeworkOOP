class ZeroQuantityProduct(Exception):
    """Класс для отработки исключений, когда в Категорию или Заказ добавляется товар с нулевым количеством"""

    def __init__(self, massege=None):
        super().__init__(massege)
