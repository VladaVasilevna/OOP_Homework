import pytest

from src.order import Order, ZeroQuantityError
from src.product import Product


def test_order_creation() -> None:
    """Тестирует создание объекта Order и правильность расчета итоговой стоимости."""
    product = Product("Samsung Galaxy S23 Ultra", "256GB, Серый цвет", 180000.0, 5)
    order = Order(product, 2)

    assert order.product.name == "Samsung Galaxy S23 Ultra"
    assert order.quantity == 2
    assert order.total_price == 360000.0  # Проверка итоговой стоимости


def test_order_invalid_quantity() -> None:
    """Тестирует обработку ошибки при создании заказа с отрицательным количеством."""
    product = Product("Samsung Galaxy S23 Ultra", "256GB, Серый цвет", 180000.0, 5)

    with pytest.raises(ZeroQuantityError) as excinfo:
        Order(product, -1)  # Проверка на отрицательное количество

    assert str(excinfo.value) == "Товар с нулевым количеством не может быть добавлен."
