from typing import Iterator

from src.category import Category
from src.product import Product


class CategoryIterator(Iterator[Product]):
    def __init__(self, category: "Category") -> None:
        self._category = category
        self._index = 0  # Начальный индекс для итерации

    def __iter__(self) -> "CategoryIterator":
        return self  # Возвращаем сам объект итератора

    def __next__(self) -> Product:
        if self._index < len(self._category.products):
            product = self._category.products[self._index]
            self._index += 1
            return product
        else:
            raise StopIteration  # Завершаем итерацию, если достигнут конец списка
