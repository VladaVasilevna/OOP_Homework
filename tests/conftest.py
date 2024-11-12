import pytest

from src.category import Category
from src.product import Product


@pytest.fixture(autouse=True)
def reset_category_counts() -> None:
    """Сбросить счётчики категорий перед каждым тестом."""
    Category.category_count = 0
    Category.product_count = 0


@pytest.fixture
def products() -> list[Product]:
    """Создание продуктов."""
    return [
        Product("Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5),
        Product("Iphone 15", "512GB, Gray space", 210000.0, 8),
        Product("Xiaomi Redmi Note 11", "1024GB, Синий", 31000.0, 14),
    ]


@pytest.fixture
def category(products: list[Product]) -> Category:
    """Создание категории с продуктами."""
    return Category("Смартфоны", "Смартфоны, как средство не только коммуникации", products)


@pytest.fixture
def product() -> Product:
    """Создание нового продукта."""
    return Product("Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5)
