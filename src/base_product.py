from abc import ABC, abstractmethod


class BaseProduct(ABC):
    @abstractmethod
    def get_info(self) -> str:
        """Метод для получения информации о продукте."""
        pass

    @abstractmethod
    def calculate_discounted_price(self, discount: float) -> float:
        """Метод для расчета цены со скидкой."""
        pass
