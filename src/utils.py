import json
import os
from typing import Any, Dict, List

from src.category import Category
from src.product import Product


def read_json(path: str) -> List[Dict[str, Any]]:
    full_path = os.path.abspath(path)
    with open(full_path, 'r', encoding="UTF-8") as file:
        data: List[Dict[str, Any]] = json.load(file)
    return data


def create_objects_from_json(data: List[Dict[str, Any]]) -> List[Category]:
    categories = []
    for category in data:
        product_list = []
        for product in category["products"]:
            product_list.append(Product(**product))
        category["products"] = product_list
        categories.append(Category(**category))

    return categories


if __name__ == "__main__":
    raw_data = read_json("../data/products.json")
    categories_data = create_objects_from_json(raw_data)

    print(categories_data[0].name)
    print(categories_data[0].products)
