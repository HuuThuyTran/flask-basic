import json, os
from salesapp import app

# Hàm đọc json
def read_json(path):
    with open(path, 'r', encoding='utf-8') as f:
        return json.load(f)

# Hàm load categories
def load_categories():
    return read_json(os.path.join(app.root_path, 'data/categories.json'))

# Hàm load products
def load_products():
    return read_json(os.path.join(app.root_path, 'data/products.json'))