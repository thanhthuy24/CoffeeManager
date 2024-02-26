import math

from flask import render_template, request, redirect
from app import app, dao, login
from flask_login import login_user, logout_user, login_required


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

    return render_template('products.html', products=prods, pages=math.ceil(num / app.config['PAGE_SIZE']))


# @app.route('/login')
# def login():
#     return render_template('login.html')

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

            # request.args.get('next')
            return redirect('/')

    return render_template('login.html')


@login.user_loader
def get_user(user_id):
    return dao.get_user_by_id(user_id)


@app.route('/logout')
def process_user_logout():
    logout_user()
    return redirect('/')

if __name__ == '__main__':
    app.run(debug=True)
