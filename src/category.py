from typing import Iterator, List, Optional

from src.base_order_category import BaseOrderCategory
from src.order import ZeroQuantityError
from src.product import Product


class Category(BaseOrderCategory):
    name: str
    description: str
    products: List[Product]
    category_count: int = 0
    product_count: int = 0

    def __init__(self, name: str, description: str, products: Optional[List[Product]] = None) -> None:
        self.name = name
        self.description = description
        self.__products = products if products else []
        Category.category_count += 1
        Category.product_count += len(products) if products else 0

    @property
    def product_list(self) -> str:
        product_str = ""
        for product in self.__products:
            product_str += f"{product.name}, {product.price} руб. Остаток: {product.quantity} шт.\n"
        return product_str

    @property
    def products(self) -> List[Product]:
        return self.__products  # Позволяет получить доступ к списку продуктов

    def add_product(self, product: Product) -> None:
        try:
            if product.quantity <= 0:
                raise ZeroQuantityError("Товар с нулевым количеством не может быть добавлен.")
            self.__products.append(product)
            Category.product_count += 1
            print(f"Товар '{product.name}' успешно добавлен в категорию '{self.name}'.")
        except ZeroQuantityError as e:
            print(e)
        else:
            print(f"Обработка добавления товара '{product.name}' завершена успешно.")
        finally:
            print("Обработка добавления товара завершена.")

    def __iter__(self) -> Iterator[Product]:
        """Метод для поддержки итерации по продуктам в категории."""
        self._iter_index = 0  # Индекс для итерации
        return self

    def __next__(self) -> Product:
        """Метод для получения следующего продукта."""
        if self._iter_index < len(self.__products):
            product = self.__products[self._iter_index]
            self._iter_index += 1
            return product
        else:
            raise StopIteration  # Остановка итерации

    def get_info(self) -> str:
        return f"Категория: {self.name}, Описание: {self.description}, Количество продуктов: {len(self.__products)}"

    def middle_price(self) -> float:
        """Метод для подсчета среднего ценника всех товаров в категории."""
        try:
            total_price = sum(product.price for product in self.__products)
            middle = total_price / len(self.__products)
            return middle
        except ZeroDivisionError:
            return 0.0

    def __repr__(self) -> str:
        return f"Category(name={self.name}, description={self.description})"


if __name__ == "__main__":
    try:
        product_invalid = Product("Бракованный товар", "Неверное количество", 1000.0, 0)
    except ValueError:
        print(
            "Возникла ошибка ValueError прерывающая работу программы при попытке добавить продукт с нулевым "
            "количеством"
        )
    else:
        print("Не возникла ошибка ValueError при попытке добавить продукт с нулевым количеством")

    product1 = Product("Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5)
    product2 = Product("Iphone 15", "512GB, Gray space", 210000.0, 8)
    product3 = Product("Xiaomi Redmi Note 11", "1024GB, Синий", 31000.0, 14)

    category1 = Category("Смартфоны", "Категория смартфонов", [product1, product2, product3])

    print(category1.middle_price())

    category_empty = Category("Пустая категория", "Категория без продуктов", [])
    print(category_empty.middle_price())
