from abc import ABC, abstractmethod


class BaseOrderCategory(ABC):
    @abstractmethod
    def get_info(self) -> str:
        """Метод для получения информации о заказе или категории."""
        pass
