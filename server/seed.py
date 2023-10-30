from random import choice as rc
from faker import Faker
from app import app
from models import db, User,Product,Review

fake = Faker()
with app.app_context():
    User.query.delete()
    Product.query.delete()
    Review.query.delete()

    users=[]
    for n in range(10):
        user = User(name=fake.name())
        users.append(user)
    db.session.add_all(users)
    # db.session.commit()

    products=[]
    product_data = [
        ('Shoes','Black high-heeled shoes','https://www.pexels.com/@craytive/','1500'),
        ('Shoes','Black high-heeled shoes','https://www.pexels.com/@craytive/','1500'),
        ('Shoes','Black high-heeled shoes','https://www.pexels.com/@craytive/','1500'),
        ('Shoes','Black high-heeled shoes','https://www.pexels.com/@craytive/','1500'),
        ('Shoes','Black high-heeled shoes','https://www.pexels.com/@craytive/','1500')
    ]
    for product_name ,description, image,price in product_data:
        product= Product(product_name=product_name,description=description,image=image, price=price)
        products.append(product)
    db.session.add_all(products)
    db.session.commit()

    
        