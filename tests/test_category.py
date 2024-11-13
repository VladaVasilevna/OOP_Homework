import pytest

from src.category import Category
from src.lawn_grass import LawnGrass
from src.product import Product
from src.smartphone import Smartphone


def test_category_creation(category: Category) -> None:
    """Тест на создание категории."""
    assert category.name == "Смартфоны"
    assert category.description == "Смартфоны, как средство не только коммуникации"
    assert len(category.product_list.splitlines()) == 3  # Проверяем количество продуктов в списке


def test_add_product(category: Category) -> None:
    """Тест на добавление продукта в категорию."""
    new_product: Product = Product('55" QLED 4K', "Фоновая подсветка", 123000.0, 7)
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
    assert Category.product_count == len(category.products)  # Проверяем количество продуктов


def test_category_iteration(category: Category) -> None:
    """Тест на итерацию по продуктам в категории."""
    products = [product for product in category]  # Используем итератор

    assert len(products) == len(category.products)  # Должно быть столько же продуктов


def test_add_product_to_category(category: Category, smartphone: Smartphone) -> None:
    """Тест на добавление продукта в категорию"""
    category.add_product(smartphone)
    assert smartphone in category.products


def test_add_invalid_product_to_category(category: Category) -> None:
    """Тест на добавление некорректного объекта в категорию"""
    with pytest.raises(TypeError):
        category.add_product("Not a product")


def test_category_creation_with_products() -> None:
    """Тест на создание категории с продуктами."""
    products = [
        Smartphone("Samsung Galaxy S23 Ultra", "256GB, Серый цвет", 180000.0, 5, 90.0, "S23 Ultra", 256, "Gray"),
        Smartphone("Iphone 15", "512GB, Gray space", 210000.0, 8, 95.0, "Iphone 15", 512, "Gray"),
    ]
    category = Category("Смартфоны", "Смартфоны, как средство не только коммуникации", products)

    assert len(category.products) == len(products)  # Проверяем количество продуктов
    assert category.product_count == len(products)  # Проверяем количество продуктов в категории


def test_add_multiple_products(category: Category) -> None:
    """Тест на добавление нескольких продуктов в категорию."""
    new_product1 = Product('55" QLED 4K', "Фоновая подсветка", 123000.0, 7)
    new_product2 = Product("Sony WH-1000XM4", "Наушники с шумоподавлением", 30000.0, 10)

    category.add_product(new_product1)
    category.add_product(new_product2)

    assert len(category.products) == 5


def test_add_lawn_grass_to_category(category: Category) -> None:
    """Тест на добавление LawnGrass в категорию."""
    lawn_grass = LawnGrass("Газонная трава", "Элитная трава для газона", 500.0, 20, "Россия", "7 дней", "Зеленый")

    category.add_lawn_grass(lawn_grass)

    assert lawn_grass in category.products


def test_category_and_product_count_increment() -> None:
    """Тест на увеличение счетчиков категорий и продуктов."""
    initial_category_count = Category.category_count
    initial_product_count = Category.product_count

    new_category = Category("Наушники", "Категория наушников")

    new_product = Product("Sony WH-1000XM4", "Наушники с шумоподавлением", 30000.0, 10)
    new_category.add_product(new_product)

    assert Category.category_count == initial_category_count + 1
    assert Category.product_count == initial_product_count + 1


def test_category_iteration_correctness(category: Category) -> None:
    """Тест на правильность итерации по продуктам в категории."""
    products = [product for product in category]
    assert len(products) == len(category.products)


def test_category_creation_empty() -> None:
    """Тест на создание пустой категории."""
    category = Category("Пустая категория", "Описание пустой категории")
    assert category.name == "Пустая категория"
    assert category.description == "Описание пустой категории"
    assert len(category.products) == 0  # Должно быть 0 продуктов
