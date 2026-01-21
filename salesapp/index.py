from flask import render_template
from salesapp import app
# from utils import load_categories, load_products # => C1
import utils # => C2

# Định nghĩa các route
@app.route('/')
def home():
    categories = utils.load_categories()
    return render_template('index.html', categories=categories)

@app.route('/products')
def product_list():
    products = utils.load_products()
    return render_template('products.html', products=products)

# Chạy app
if __name__ == '__main__':
    app.run(debug=True)