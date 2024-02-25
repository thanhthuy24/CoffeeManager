import math

from flask import render_template, request
from app import app, dao


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/cake')
def product_page():
    kw = request.args.get('kw')
    cate_id = request.args.get('cate_id')
    page = request.args.get('page')

    prods = dao.get_products(kw, cate_id, page)

    num = dao.count_product()

    return render_template('products.html', products=prods, pages=math.ceil(num/app.config['PAGE_SIZE']))


@app.route('/login')
def login():
    return render_template('login.html')

@app.route('/basket')
def basket():
    return render_template('basket.html')

if __name__ == '__main__':
    app.run(debug=True)
