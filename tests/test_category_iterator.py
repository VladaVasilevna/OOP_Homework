from src.category import Category


def test_category_iterator(category: Category) -> None:
    """Тест на работу итератора категории."""
    iterator = iter(category)

    products = list(iterator)

    assert len(products) == len(category.products)  # Должно совпадать количество продуктов
    assert products[0].name == category.products[0].name  # Проверка первого элемента


def test_empty_category_iteration() -> None:
    """Тест на итерацию по пустой категории."""
    empty_category = Category("Empty Category", "No products here")

    iterator = iter(empty_category)

    assert list(iterator) == []  # Итерация должна вернуть пустой список
