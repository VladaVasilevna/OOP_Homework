from src.lawn_grass import LawnGrass


def test_create_lawn_grass(lawn_grass: LawnGrass) -> None:
    """Тест на создание LawnGrass"""
    assert lawn_grass.name == "Газонная трава"
    assert lawn_grass.country == "Россия"


def test_lawn_grass_str(lawn_grass: LawnGrass) -> None:
    """Тест на строковое представление LawnGrass"""
    expected_str = (
        f"{lawn_grass.name}, {lawn_grass.price} руб. Остаток: "
        f"{lawn_grass.quantity} шт., Страна-производитель: {lawn_grass.country}, "
        f"Срок прорастания: {lawn_grass.germination_period}, Цвет: {lawn_grass.color}"
    )
    assert str(lawn_grass) == expected_str
