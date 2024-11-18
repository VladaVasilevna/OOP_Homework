from src.base_order_category import BaseOrderCategory
from src.product import Product


class ZeroQuantityError(Exception):
    """Исключение, вызываемое при попытке создать заказ с нулевым количеством."""

    def __init__(self, message: str) -> None:
        super().__init__(message)


class Order(BaseOrderCategory):
    def __init__(self, product: Product, quantity: int) -> None:
        if quantity <= 0:
            raise ZeroQuantityError("Товар с нулевым количеством не может быть добавлен.")

        self.product = product
        self.quantity = quantity
        self.total_price = self.calculate_total_price()
        print(f"Заказ на '{self.product.name}' успешно создан.")

    def calculate_total_price(self) -> float:
        return self.product.price * self.quantity

    def get_info(self) -> str:
        return (
            f"Заказ: {self.product.name}, "
            f"Количество: {self.quantity}, "
            f"Итоговая стоимость: {self.total_price:.2f} руб."
        )

    def __repr__(self) -> str:
        return f"Order(product={self.product.name}, quantity={self.quantity}, total_price={self.total_price})"
