import pytest

from src.product import Product


def test_product_init(product: Product) -> None:
    assert product.name == "55\" QLED 4K"
    assert product.description == "Фоновая подсветка"
    assert product.price == 123000.0
    assert product.quantity == 7


def test_product_negative_price() -> None:
    with pytest.raises(ValueError):
        Product("Iphone 15", "512GB, Gray space", -210000.0, 8)


def test_product_negative_quantity() -> None:
    with pytest.raises(ValueError):
        Product("Iphone 15", "512GB, Gray space", 210000.0, -8)


def test_update_product_price() -> None:
    product: Product = Product("Iphone 15", "512GB, Gray space", 210000.0, 8)
    product.price = 120000.0
    assert product.price == 120000.0


def test_update_product_quantity() -> None:
    product: Product = Product("Iphone 15", "512GB, Gray space", 210000.0, 8)
    product.quantity = 15
    assert product.quantity == 15


def test_product_main_output(capsys: pytest.CaptureFixture) -> None:
    # Выполняем код из блока main
    product1: Product = Product("Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5)
    product2: Product = Product("Iphone 15", "512GB, Gray space", 210000.0, 8)
    product3: Product = Product("Xiaomi Redmi Note 11", "1024GB, Синий", 31000.0, 14)

    print(product1.name)
    print(product1.description)
    print(product1.price)
    print(product1.quantity)

    print(product2.name)
    print(product2.description)
    print(product2.price)
    print(product2.quantity)

    print(product3.name)
    print(product3.description)
    print(product3.price)
    print(product3.quantity)

    # Захватываем вывод
    captured = capsys.readouterr()

    # Ожидаемый вывод
    expected_output: str = (
        "Samsung Galaxy S23 Ultra\n"
        "256GB, Серый цвет, 200MP камера\n"
        "180000.0\n"
        "5\n"
        "Iphone 15\n"
        "512GB, Gray space\n"
        "210000.0\n"
        "8\n"
        "Xiaomi Redmi Note 11\n"
        "1024GB, Синий\n"
        "31000.0\n"
        "14\n"
    )

    # Проверяем, что вывод соответствует ожидаемым значениям
    assert captured.out == expected_output
