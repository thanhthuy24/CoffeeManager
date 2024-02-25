from flask import Flask
from urllib.parse import quote
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.secret_key = '*(^(*^897987(*^&*^&*%YUFUF&^^&$^&%&*^&*^*(^^%'
app.config["SQLALCHEMY_DATABASE_URI"] ="mysql+pymysql://root:%s@localhost/coffeemanage?charset=utf8mb4" % quote('Admin123@')
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = True
app.config["PAGE_SIZE"] = 2

db = SQLAlchemy(app=app)