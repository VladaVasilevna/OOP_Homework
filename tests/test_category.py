from src.category import Category
from src.product import Product


def test_category_init(first_category: Category, second_category: Category) -> None:
    assert first_category.name == "Смартфоны"
    assert first_category.description == ("Смартфоны, как средство не только коммуникации, "
                                          "но и получения дополнительных функций для удобства жизни")
    assert len(first_category.products) == 3

    assert Category.category_count == 2

    assert first_category.product_count == 3
    assert second_category.product_count == 1


def test_product_count_in_category(first_category: Category) -> None:
    """Проверка количества продуктов в категории."""
    assert len(first_category.products) == 3
    assert first_category.product_count == 3


def test_empty_products_in_category() -> None:
    """Проверка инициализации категории без продуктов."""
    empty_category: Category = Category("Без продуктов", "Категория без продуктов")
    assert len(empty_category.products) == 0
    assert empty_category.product_count == 0


def test_add_products_to_existing_category(first_category: Category) -> None:
    """Проверка добавления продуктов в существующую категорию."""
    new_product: Product = Product("Xiaomi Mi Band 6", "Фитнес-браслет", 3000.0, 20)
    first_category.add_product(new_product)

    assert len(first_category.products) == 4
    assert first_category.product_count == 4
