from app import app, db
from sqlalchemy import Column, Integer, String, Float, ForeignKey, Enum, DateTime
from flask_login import UserMixin
import enum

class UserRoleEnum(enum.Enum):
    USER = 1
    ADMIN = 2

class User(db.Model, UserMixin):
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(50), nullable=False)
    username = Column(String(50), nullable=False, unique=True)
    password = Column(String(100), nullable=False)
    avatar = Column(String(100), default='static/images/img10.jpg')
    user_role = Column(Enum(UserRoleEnum), default=UserRoleEnum.USER)

    def __str__(self):
        return self.name


class Category(db.Model):
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(50), nullable=False, unique=True)

    def __str__(self):
        return self.name


class Product(db.Model):
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(50), nullable=False, unique=True)
    price = Column(Float, default=0)
    image = Column(String(100))
    category_id = Column(Integer, ForeignKey(Category.id), nullable=False)

    def __str__(self):
        return self.name


class BaseModel(db.Model):
    __abstract__ = True

    id = Column(Integer, primary_key=True, autoincrement=True)
    created_date = Column(DateTime, default=True)

class Receipt(BaseModel):
    user_id = Column(Integer, ForeignKey(User.id), nullable=False)
    pass


class Receipt():
    pass

if __name__ == '__main__':
    with app.app_context():
        db.create_all()

        import hashlib

        u1 = User(name='Abc', username='Abc01', password=str(hashlib.md5('12345'.encode('utf-8')).hexdigest()))
        db.session.add(u1)
        db.session.commit()

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
        # # #
        p1 = Product(name='Chocolate chip cookie', price=15000, category_id=3,
                     image="static/images/img7.jpg")
        p2 = Product(name='Donut', price=20000, category_id=3,
                     image="static/images/img8.jpg")
        p3 = Product(name='Blueberry tart', price=18000, category_id=3,
                     image="static/images/img9.jpg")
        p4 = Product(name='Heart jam cookie', price=15000, category_id=3,
                     image="static/images/img11.jpg")
        p5 = Product(name='Latte', price=20000, category_id=2,
                     image="static/images/img12.jpg")
        p6 = Product(name='Americano', price=18000, category_id=2,
                     image="static/images/img13.jpg")
        p7 = Product(name='Pink bows cake', price=15000, category_id=1,
                     image="static/images/img14.jpg")
        p8 = Product(name='Spring cake', price=20000, category_id=1,
                     image="static/images/img15.jpg")

        db.session.add_all([p1, p2, p3, p4, p5, p6, p7, p8])
        db.session.commit()
