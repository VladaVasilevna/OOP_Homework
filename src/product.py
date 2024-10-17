from typing import Dict, List


class Product:
    def __init__(self, name: str, description: str, price: float, quantity: int) -> None:
        if price < 0:
            raise ValueError("Цена не может быть отрицательной.")
        if quantity < 0:
            raise ValueError("Количество не может быть отрицательным.")

        self.name = name
        self.description = description
        self.__price = price  # Приватный атрибут цены
        self.quantity = quantity

    @property
    def price(self) -> float:
        return self.__price

    @price.setter
    def price(self, new_price: float) -> None:
        if new_price <= 0:
            print("Цена не должна быть нулевая или отрицательная.")
            return
        self.__price = new_price

    def merge_with_existing(self, products: List['Product']) -> None:
        for existing_product in products:
            if existing_product.name == self.name:
                existing_product.quantity += self.quantity

                # Обновление цены на более высокую
                if self.price > existing_product.price:
                    existing_product.price = self.price

                # Устанавливаем текущее количество в 0 после объединения
                self.quantity = 0
                return

        products.append(self)  # Если товара не существует в списке, добавляем его

    @classmethod
    def new_product(cls, product_data: Dict[str, str]) -> 'Product':
        name = product_data.get('name', "")
        description = product_data.get('description', "")

        # Преобразование значений из строк в нужные типы с проверкой на None
        price = float(product_data.get('price', 0)) if product_data.get('price') is not None else 0.0
        quantity = int(product_data.get('quantity', 0)) if product_data.get('quantity') is not None else 0

        return cls(name, description, price, quantity)  # Возвращаем новый объект


if __name__ == "__main__":
    new_product = Product.new_product(
        {"name": "Samsung Galaxy S23 Ultra",
         "description": "256GB, Серый цвет, 200MP камера",
         "price": "180000.0",
         "quantity": "5"}
    )

    print(new_product.name)
    print(new_product.description)
    print(new_product.price)
    print(new_product.quantity)

    new_product.price = 800
    print(new_product.price)

    new_product.price = -100  # Это вызовет сообщение об ошибке
    print(new_product.price)

    new_product.price = 0  # Это также вызовет сообщение об ошибке
    print(new_product.price)

    product_data1 = {
        'name': 'Xiaomi Redmi Note 11',
        'description': '1024GB, Синий',
        'price': '31000.0',
        'quantity': '1'
    }

    product1 = Product.new_product(product_data1)

    print(product1.name)
    print(product1.description)
    print(product1.price)
    print(product1.quantity)

    product_data2 = {
        'name': 'Xiaomi Redmi Note 11',
        'description': '1024GB, Черный',
        'price': '32000.0',
        'quantity': '5'
    }

    product2 = Product.new_product(product_data2)

    products_list = [product1]

    product2.merge_with_existing(products_list)  # Объединяем товары

    for product in products_list:
        print(product.name)
        print(product.description)
        print(product.price)
        print(product.quantity)
