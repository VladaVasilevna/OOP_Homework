from src.smartphone import Smartphone


def test_create_smartphone(smartphone: Smartphone) -> None:
    """Тест на создание смартфона"""
    assert smartphone.name == "Samsung Galaxy S23 Ultra"
    assert smartphone.memory == 256


def test_smartphone_str(smartphone: Smartphone) -> None:
    """Тест на строковое представление смартфона"""
    expected_str = (
        f"Samsung Galaxy S23 Ultra, {smartphone.price} руб. Остаток: "
        f"{smartphone.quantity} шт., Эффективность: {smartphone.efficiency}, "
        f"Модель: {smartphone.model}, Память: {smartphone.memory}GB, Цвет: {smartphone.color}"
    )
    assert str(smartphone) == expected_str
