import pytest

from src.category import Category
from src.lawn_grass import LawnGrass
from src.product import Product
from src.smartphone import Smartphone


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


@pytest.fixture
def smartphone() -> Smartphone:
    """Фикстура для создания объекта Smartphone"""
    return Smartphone(
        name="Samsung Galaxy S23 Ultra",
        description="256GB, Серый цвет",
        price=180000.0,
        quantity=5,
        efficiency=90.0,
        model="S23 Ultra",
        memory=256,
        color="Gray",
    )


@pytest.fixture
def lawn_grass() -> LawnGrass:
    """Фикстура для создания объекта LawnGrass"""
    return LawnGrass(
        name="Газонная трава",
        description="Элитная трава для газона",
        price=500.0,
        quantity=20,
        country="Россия",
        germination_period="7 дней",
        color="Зеленый",
    )
