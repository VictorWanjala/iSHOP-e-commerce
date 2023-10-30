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
    serialize_rules = ('-reviews.user')

    id = db.Column(db.Integer,primary_key=True)
    name = db.Column(db.String)
    email = db.Column(db.String, unique= True)
    password = db.Column(db.String)

    reviews = db.relationship('Review', backref ='user')


class Product(db.Model,SerializerMixin):
    __tablename__ = 'products'
    serialize_rules = ('-reviews.product')

    id = db.Column(db.Integer, primary_key=True)
    product_name = db.Column(db.String)
    description = db.Column(db.String)
    price = db.Column(db.Integer)
    image = db.Column(db.String)

    reviews = db.relationship('Review',backref='product')
    

class Review(db.Model,SerializerMixin):
    __tablename__ = 'reviews'
    serialize_rules = ('-user.reviews','-product.reviews')

    id = db.Column(db.Integer, primary_key=True)
    review = db.Column(db.String)
    

    product_id= db.Column(db.Integer, db.ForeignKey('products.id'))
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))

    

