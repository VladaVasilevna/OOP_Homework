from unittest.mock import patch

import pytest

from src.lawn_grass import LawnGrass
from src.product import Product


def test_product_creation(product: Product) -> None:
    """Тест на создание продукта."""
    assert product.name == "Samsung Galaxy S23 Ultra"
    assert product.description == "256GB, Серый цвет, 200MP камера"
    assert product.price == 180000.0
    assert product.quantity == 5


def test_set_negative_price(product: Product) -> None:
    """Тест на установку отрицательной цены."""
    with patch("builtins.print") as mock_print:
        product.price = -100
        mock_print.assert_called_once_with("Цена не должна быть нулевая или отрицательная.")
        assert product.price == 180000.0  # Цена не должна измениться


def test_set_zero_price(product: Product) -> None:
    """Тест на установку нулевой цены."""
    with patch("builtins.print") as mock_print:
        product.price = 0
        mock_print.assert_called_once_with("Цена не должна быть нулевая или отрицательная.")
        assert product.price == 180000.0  # Цена не должна измениться


@patch("builtins.input", return_value="y")  # Эмулируем ввод 'y'
def test_set_valid_price(mock_input: str, product: Product) -> None:
    """Тест на успешное изменение цены."""
    product.price = 150000.0
    assert product.price == 150000.0


@patch("builtins.input", side_effect=["n"])  # Пользователь отвечает 'n'
def test_confirm_price_decrease(mock_input: str, product: Product) -> None:
    """Тест на отказ понижения цены."""
    with patch("builtins.print") as mock_print:
        product.price = 170000.0  # Понижаем цену
        mock_print.assert_called_once_with("Изменение цены отменено.")
        assert product.price == 180000.0  # Цена не должна измениться


@patch("builtins.input", side_effect=["y"])  # Пользователь отвечает 'y'
def test_confirm_price_decrease_accept(mock_input: str, product: Product) -> None:
    """Тест на подтверждение понижения цены."""
    product.price = 170000.0  # Понижаем цену
    assert product.price == 170000.0


def test_merge_with_existing(product: Product) -> None:
    """Тест на объединение продуктов."""
    existing_product = Product("Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера", 200000.0, 3)
    products_list = [existing_product]

    product.merge_with_existing(products_list)

    assert existing_product.quantity == 8  # Объединение количеств
    assert existing_product.price == 200000.0  # Цена не должна измениться, так как она выше у существующего продукта
    assert product.quantity == 0  # Количество нового продукта должно стать нулевым


def test_new_product() -> None:
    """Тест на создание нового продукта из словаря."""
    product_data: dict[str, str] = {
        "name": "Xiaomi Redmi Note 11",
        "description": "1024GB, Синий",
        "price": "31000.0",
        "quantity": "1",
    }

    new_product = Product.new_product(product_data)

    assert new_product.name == "Xiaomi Redmi Note 11"
    assert new_product.description == "1024GB, Синий"
    assert new_product.price == 31000.0
    assert new_product.quantity == 1


def test_addition_of_products() -> None:
    """Тест на сложение двух продуктов."""
    product1 = Product("Product A", "Description A", 100.0, 2)
    product2 = Product("Product B", "Description B", 200.0, 3)

    total_cost = product1 + product2
    assert total_cost == (100.0 * 2 + 200.0 * 3)  # Ожидаемая стоимость


def test_create_lawn_grass(lawn_grass: LawnGrass) -> None:
    """Тест на создание LawnGrass"""
    assert lawn_grass.name == "Газонная трава"
    assert lawn_grass.country == "Россия"


def test_lawn_grass_str(lawn_grass: LawnGrass) -> None:
    """Тест на строковое представление LawnGrass"""
    expected_str = (
        f"Газонная трава, {lawn_grass.price} руб. Остаток: "
        f"{lawn_grass.quantity} шт., Страна-производитель: {lawn_grass.country}, "
        f"Срок прорастания: {lawn_grass.germination_period}, Цвет: {lawn_grass.color}"
    )
    assert str(lawn_grass) == expected_str


def test_create_product_with_negative_quantity() -> None:
    """Тест на создание продукта с отрицательным количеством."""
    with pytest.raises(ValueError, match="Количество не может быть отрицательным."):
        Product("Товар", "Описание товара", 100.0, -1)


def test_merge_with_existing_updates_price() -> None:
    """Тест на объединение продуктов с обновлением цены."""
    existing_product = Product("Samsung Galaxy S23 Ultra", "256GB, Серый цвет", 200000.0, 3)
    products_list = [existing_product]

    new_product = Product("Samsung Galaxy S23 Ultra", "256GB, Серый цвет", 250000.0, 5)
    new_product.merge_with_existing(products_list)

    assert existing_product.price == 250000.0


def test_new_product_with_invalid_data() -> None:
    """Тест на создание нового продукта из словаря с некорректными данными."""
    product_data = {
        "name": "Xiaomi Redmi Note 11",
        "description": "1024GB, Синий",
        "price": "-31000.0",
        "quantity": "1",
    }

    with pytest.raises(ValueError, match="Цена не может быть отрицательной."):
        Product.new_product(product_data)
