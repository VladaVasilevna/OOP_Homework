from src.product import Product


class Smartphone(Product):
    def __init__(
        self,
        name: str,
        description: str,
        price: float,
        quantity: int,
        efficiency: float,
        model: str,
        memory: int,
        color: str,
    ) -> None:
        super().__init__(name, description, price, quantity)
        self.efficiency = efficiency
        self.model = model
        self.memory = memory
        self.color = color

    def __str__(self) -> str:
        return (
            super().__str__() + f", Эффективность: {self.efficiency}, Модель: {self.model}, "
            f"Память: {self.memory}GB, Цвет: {self.color}"
        )
