from random import choice as rc
from faker import Faker
from app import app
from models import db, User,Product,Review
from passlib.hash import sha256_crypt

fake = Faker()
with app.app_context():
    User.query.delete()
    Product.query.delete()
    Review.query.delete()

    users=[]
    for n in range(10):
        email = fake.email()
        password = fake.password(length=10, special_chars=True)
        hashed_pass = sha256_crypt.hash(password)

        user = User(name=fake.name(),email=email, password=hashed_pass)
        users.append(user)
    db.session.add_all(users)
  

    products=[]
    product_data = [
        ('Shoes','Black high-heeled shoes','https://www.pexels.com/@craytive/','1500'),
        ('Perfume','D&G','https://images.pexels.com/photos/965990/pexels-photo-965990.jpeg?auto=compress&cs=tinysrgb&w=300','4500'),
        ('Flower','Roses','https://images.pexels.com/photos/74512/pexels-photo-74512.jpeg?auto=compress&cs=tinysrgb&w=300','3500'),
        ('Lipstick','Vicrose pink','https://images.pexels.com/photos/2533266/pexels-photo-2533266.jpeg?auto=compress&cs=tinysrgb&w=300','10000'),
        ('Lipgloss','Anzalyellow glow','https://images.pexels.com/photos/3373722/pexels-photo-3373722.jpeg?auto=compress&cs=tinysrgb&w=300','7500'),
        ('Mascara','Venusneriko black','https://images.pexels.com/photos/6167864/pexels-photo-6167864.jpeg?auto=compress&cs=tinysrgb&w=300','1000'),
        ('Beauty cream','Masibolies white','https://images.pexels.com/photos/2587175/pexels-photo-2587175.jpeg?auto=compress&cs=tinysrgb&w=300','8500'),
        ('Nail polish','nailstar','https://images.pexels.com/photos/791157/pexels-photo-791157.jpeg?auto=compress&cs=tinysrgb&w=300','1500'),
        ('Lipbum','Mucsinrose brown','https://images.pexels.com/photos/6167864/pexels-photo-6167864.jpeg?auto=compress&cs=tinysrgb&w=300','7500'),
        ('Lipbum','Mucsinrose brown','https://images.pexels.com/photos/6167864/pexels-photo-6167864.jpeg?auto=compress&cs=tinysrgb&w=300','7500'),
        ('Lipbum','Mucsinrose brown','https://images.pexels.com/photos/6167864/pexels-photo-6167864.jpeg?auto=compress&cs=tinysrgb&w=300','7500'),
        ('Lipbum','Mucsinrose brown','https://images.pexels.com/photos/6167864/pexels-photo-6167864.jpeg?auto=compress&cs=tinysrgb&w=300','7500')
    ]
    for product_name ,description, image,price in product_data:
        product= Product(product_name=product_name,description=description,image=image, price=price)
        products.append(product)
    db.session.add_all(products)

    for product in products:
        num_reviews = rc(range(5,10))
        for _ in range(num_reviews):
            review_text = fake.paragraph()
            user = rc(users)
            review = Review(review=review_text,user=user,product=product)
            db.session.add(review)
    db.session.commit()

    
        