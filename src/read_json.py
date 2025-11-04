import json
import os
from src.my_class import Category, Product

file = os.path.join(os.path.dirname(__file__), "..", "data", "products.json")
def read_json(file):
    with open(file, "r", encoding="UTF-8") as f:
        data = json.load(f)
    return data

def create_object(data):
    new_category = []
    for category in data:
        new_products =[]
        for cat in category["products"]:
            new_products.append(Product(**cat))
        category["products"] = new_products
        new_category.append(Category(**category))
    return new_category

print(create_object(read_json(file))[0].products)



