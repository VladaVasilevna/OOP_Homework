from src.category import Category
from src.product import Product


def test_category_creation(category: Category) -> None:
    """Тест на создание категории."""
    assert category.name == "Смартфоны"
    assert category.description == "Смартфоны, как средство не только коммуникации"
    assert len(category.product_list.splitlines()) == 3  # Проверяем количество продуктов в списке


def test_add_product(category: Category) -> None:
    """Тест на добавление продукта в категорию."""
    new_product: Product = Product("55\" QLED 4K", "Фоновая подсветка", 123000.0, 7)
    category.add_product(new_product)

    # Проверяем, что новый продукт добавлен
    assert len(category.product_list.splitlines()) == 4  # Теперь должно быть 4 продукта


def test_product_list_output(category: Category) -> None:
    """Тест на правильный вывод списка продуктов."""
    expected_output: str = (
        "Samsung Galaxy S23 Ultra, 180000.0 руб. Остаток: 5 шт.\n"
        "Iphone 15, 210000.0 руб. Остаток: 8 шт.\n"
        "Xiaomi Redmi Note 11, 31000.0 руб. Остаток: 14 шт.\n"
    )

    assert category.product_list == expected_output


def test_category_and_product_count(category: Category) -> None:
    """Тест на подсчет категорий и продуктов."""
    assert Category.category_count == 1  # Проверяем количество категорий
    assert Category.product_count == len(category.get_products)  # Проверяем количество продуктов
