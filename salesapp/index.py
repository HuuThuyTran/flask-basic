from flask import render_template, request
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
    cate_id = request.args.get('category_id')
    keyword = request.args.get('keyword')
    from_price = request.args.get('from_price')
    to_price = request.args.get('to_price')
    products = utils.load_products(cate_id, keyword, from_price, to_price)

    category_name = None
    categories = utils.load_categories()
    if cate_id:
        for c in categories:
            if c['id'] == int(cate_id):
                category_name = c['name']
                break
    return render_template('products.html', products=products, category_name=category_name)

@app.route('/products/<int:product_id>')
def product_detail(product_id):
    product = utils.get_product_by_id(product_id)
    return render_template('product_detail.html', product=product)

# Chạy app
if __name__ == '__main__':
    app.run(debug=True)