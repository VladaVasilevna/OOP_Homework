from src.category import Category
from src.product import Product


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


def test_get_info(category: Category) -> None:
    """Тест на метод get_info."""
    expected_info = (
        "Категория: Смартфоны, Описание: Смартфоны, как средство не только коммуникации, " "Количество продуктов: 3"
    )
    assert category.get_info() == expected_info


def test_empty_category() -> None:
    """Тест на создание пустой категории."""
    empty_category = Category("Пустая категория", "Описание пустой категории")

    assert empty_category.name == "Пустая категория"
    assert empty_category.description == "Описание пустой категории"
    assert len(empty_category.products) == 0
    assert empty_category.product_list == ""


def test_repr(category: Category) -> None:
    """Тест на метод __repr__."""
    expected_repr = "Category(name=Смартфоны, description=Смартфоны, как средство не только коммуникации)"
    assert repr(category) == expected_repr


def test_multiple_products_addition() -> None:
    """Тест на добавление нескольких продуктов в категорию."""
    category = Category("Электроника", "Различная электроника")

    products = [
        Product("Телевизор", "Умный телевизор", 50000.0, 10),
        Product("Ноутбук", "Игровой ноутбук", 120000.0, 5),
        Product("Смартфон", "Флагманский смартфон", 80000.0, 8),
    ]

    for product in products:
        category.add_product(product)

    assert len(category.products) == len(products)


def test_product_count_increment() -> None:
    """Тест на корректное увеличение счетчика продуктов при добавлении."""
    category = Category("Бытовая техника", "Различная бытовая техника")

    initial_count = Category.product_count
    new_product = Product("Холодильник", "Современный холодильник", 60000.0, 4)

    category.add_product(new_product)

    assert Category.product_count == initial_count + 1


def test_middle_price_no_products() -> None:
    """Тест на среднюю цену при отсутствии продуктов."""
    category = Category("Пустая категория", "Описание пустой категории")

    assert category.middle_price() == 0.0


def test_middle_price_with_products() -> None:
    """Тест на среднюю цену с несколькими продуктами."""
    product1 = Product("Samsung Galaxy S23 Ultra", "256GB, Серый цвет", 180000.0, 5)
    product2 = Product("Iphone 15", "512GB, Gray space", 210000.0, 8)

    category = Category("Смартфоны", "Описание смартфонов", [product1, product2])

    assert category.middle_price() == (180000.0 + 210000.0) / 2
