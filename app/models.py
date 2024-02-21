from app import app, db
from sqlalchemy import Column, Integer, String, Float, ForeignKey

class Category(db.Model):
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(50), nullable=False, unique=True)

class Product(db.Model):
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(50), nullable=False, unique=True)
    price = Column(Float, default=0)
    image = Column(String(100))
    category_id = Column(Integer, ForeignKey(Category.id), nullable=False)

if __name__ == '__main__':
    with app.app_context():
        db.create_all()

        # import hashlib
        # u = User(name='Admin', username='admin',
        #          password=str(hashlib.md5('123456'.encode('utf-8')).hexdigest()),
        #          user_role=UserRoleEnum.ADMIN)
        # db.session.add(u)
        # db.session.commit()
        #
        c1 = Category(name='Cake')
        c2 = Category(name='Coffee')
        c3 = Category(name='Dessert')

        db.session.add(c1)
        db.session.add(c2)
        db.session.add(c3)
        db.session.commit()
        # #
        p1 = Product(name='Chocolate chip cookie', price=15000, category_id=1,
                     image="static/images/img7.jpg")
        p2 = Product(name='Donut', price=20000, category_id=1,
                     image="static/images/img8.jpg")
        p3 = Product(name='Blueberry tart', price=18000, category_id=1,
                     image="static/images/img9.jpg")
        # # p4 = Product(name='Galaxy Tab S9', price=28000000, category_id=2,
        # #              image="https://res.cloudinary.com/dxxwcby8l/image/upload/v1688179242/hclq65mc6so7vdrbp7hz.jpg")
        # # p5 = Product(name='Note 13', price=20000000, category_id=1,
        # #              image="https://res.cloudinary.com/dxxwcby8l/image/upload/v1688179242/hclq65mc6so7vdrbp7hz.jpg")
        # #
        db.session.add_all([p1, p2, p3])
        db.session.commit()