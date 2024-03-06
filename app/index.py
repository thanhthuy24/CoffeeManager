import math
from flask import render_template, request, redirect, jsonify, session
from app import app, dao, login
from flask_login import login_user, logout_user, login_required
import utils

@app.route('/')
def index():
    return render_template('index.html')


@app.route('/cake')
def product_page():
    kw = request.args.get('kw')
    # cate_id = request.args.get('cate_id')
    page = request.args.get('page')

    prods = dao.get_products(kw, 1, page)

    num = dao.count_product()

    return render_template('products.html', products=prods)
    # , pages=math.ceil(num / app.config['PAGE_SIZE'])



@app.route('/coffee')
def product_page_coffee():
    kw = request.args.get('kw')
    # cate_id = request.args.get('cate_id')
    page = request.args.get('page')

    prods = dao.get_products(kw, 2, page)

    num = dao.count_product()

    return render_template('coffee.html', products=prods)


@app.route('/dessert')
def product_page_dessert():
    kw = request.args.get('kw')
    # cate_id = request.args.get('cate_id')
    page = request.args.get('page')

    prods = dao.get_products(kw, 3, page)

    num = dao.count_product()

    return render_template('dessert.html', products=prods)


@app.route('/basket')
def basket():
    return render_template('basket.html')


@app.route("/login", methods=['get', 'post'])
def process_user_login():
    if request.method.__eq__('POST'):
        username = request.form.get('username')
        password = request.form.get('password')

        user = dao.auth_user(username=username, password=password)

        if user:
            login_user(user=user)

            return redirect('/')

    return render_template('login.html')


@app.route('/logout')
def process_user_logout():
    logout_user()
    return redirect('/')


@app.route('/api/basket', methods=['post'])
def add_to_basket():
    data = request.json

    basket = session.get('basket')
    if basket is None:
        basket = {}

    id = str(data.get("id"))
    if id in basket:  # sp co trong gio hang
        basket[id]['quantity'] += 1
    else:  # sp ko co trong gio hang
        basket[id] = {
            "id": id,
            "name": data.get("name"),
            "price": data.get("price"),
            "image": data.get("image"),
            "quantity": 1
        }

    session['basket'] = basket

    print(data)

    return jsonify(utils.count_basket(basket))


# tang / giam so luong product
@app.route('/api/basket/<product_id>', methods=['put'])
def update_basket(product_id):
    basket = session.get('basket')

    if basket and product_id in basket:
        quantity = request.json.get('quantity')
        basket[product_id]['quantity'] = int(quantity)
        # prods = basket[product_id]['quantity']
    session['basket'] = basket
    return jsonify(utils.count_basket(basket))


@app.route('/api/basket/<product_id>', methods=['delete'])
def delete_basket(product_id):
    basket = session.get('basket')

    if basket and product_id in basket:
        del basket[product_id]

    session['basket'] = basket
    return jsonify(utils.count_basket(basket))


# hien thi thanh header so luong product trong basket
@app.context_processor
def common_response():
    return {
        'basket': utils.count_basket(session.get('basket'))
    }


@app.route('/checkout')
def checkout_receipt():
    return render_template('checkout.html')


@app.route('/api/payCOD', methods=['post'])
def payment_cod():
    try:
        dao.add_receipt(session.get('basket'))
    except Exception as ex:
        return jsonify({'status': 500, "err_msg": str(ex)})
    else:
        del session['basket']
        return jsonify({'status': 200})


@login.user_loader
def get_user(user_id):
    return dao.get_user_by_id(user_id)


if __name__ == '__main__':
    app.run(debug=True)

