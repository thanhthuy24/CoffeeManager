from flask import render_template, request
from app import app, dao

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/cake')
def product_page():
    kw = request.args.get('kw')
    cate_id = request.args.get('cate_id')

    prods = dao.get_products(kw, cate_id)

    return render_template('products.html', products=prods)


@app.route('/login')
def login():
    return render_template('login.html')

if __name__ == '__main__':
    app.run(debug=True)