from flask import render_template, request
from app import app, dao

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/cake')
def product_page():
    cate_id = request.args.get('cate_id')

    prods = dao.get_products(cate_id)

    return render_template('products.html', products=prods)


if __name__ == '__main__':
    app.run(debug=True)