from app .models import Product, Category
import hashlib
from app import app, db

def get_categories():
    return Category.query.all()

def get_products (cate_id):
    products = Product.query

    if cate_id:
        products = products.filter(Product.category_id.__eq__(cate_id))

    return products.all()
