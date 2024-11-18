from typing import Any


class CreationLoggerMixin:
    def __init__(self, *args: Any, **kwargs: Any) -> None:
        class_name = self.__class__.__name__
        parameters = ", ".join(f"{arg}" for arg in args)
        print(f"Создан объект класса {class_name} с параметрами: {parameters}")
