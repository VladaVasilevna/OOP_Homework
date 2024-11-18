from src.product import Product


class LawnGrass(Product):
    def __init__(
        self,
        name: str,
        description: str,
        price: float,
        quantity: int,
        country: str,
        germination_period: str,
        color: str,
    ) -> None:
        super().__init__(name, description, price, quantity)
        self.country = country
        self.germination_period = germination_period
        self.color = color

    def __str__(self) -> str:
        return (
            f"{self.name}, {self.price} руб. Остаток: "
            f"{self.quantity} шт., Страна-производитель: {self.country}, "
            f"Срок прорастания: {self.germination_period}, Цвет: {self.color}"
        )
