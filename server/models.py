# Defining User model
# - Models:
#   - User
#   - Product
#   - Review

from flask_sqlalchemy import SQLAlchemy
from sqlalchemy_serializer import SerializerMixin

db = SQLAlchemy()

class User(db.Model,SerializerMixin):
    __tablename__ = 'users'
    serialize_rules = ('products')

    id = db.Column(db.Integer,primary_key=True)
    name = db.Column(db.String)
    email = db.Column(db.String, unique= True)
    password = db.Column(db.String)

    products = db.relationship('Product', backref ='user')


class Product(db.Model,SerializerMixin):
    __tablename__ = 'products'
    serialize_rules = ('users, carts')

    id = db.Column(db.Integer, primary_key=True)
    product_name = db.Column(db.String)
    description = db.Column(db.String)
    price = db.Column(db.Integer)
    image = db.Column(db.String)

    carts = db.relationship('Cart', backref ='product')
    

class Cart(db.Model,SerializerMixin):
    __tablename__ = 'carts'
    serialize_rules = ('product')

    id = db.Column(db.Integer, primary_key=True)
    product_name = db.Column(db.String)
    price = db.Column(db.Integer)

    product_id = db.Column(db.Integer,db.ForeignKey('products.id'))
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))

    

