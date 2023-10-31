from flask import Flask,jsonify,make_response, request
from flask_migrate import Migrate
from models import db ,User, Review,Product
from flask_restful import Resource, Api
from passlib.hash import sha256_crypt


app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"]='sqlite:///app.db'
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

api=Api(app)

migrate = Migrate(app, db)
db.init_app(app)

class Products(Resource):
    def get(self):
        my_product=[n.to_dict()for n in Product.query.all()]
        response=make_response(jsonify(my_product),200)

        return response
api.add_resource(Products,"/products")

class UserRegister(Resource):
    def post(self):
        data = request.get_json()
        name = data.get('name')
        email = data.get('email')
        password = data.get('password')

        if not name or not email or not password:
            return jsonify({'message': 'Missing required fields'}), 400
        
        hashed_pass = sha256_crypt.hash(password)

        new_user = User(name=name, email=email, password=hashed_pass)
        db.session.add(new_user)
        db.session.commit()

        return jsonify({'message': 'User registered successfully'}), 201
api.add_resource(UserRegister, '/users')


class UserLogin(Resource):
    def post(self):
        data = request.get_json()
        email = data.get("email")
        password = data.get("password")

        if not email or not password:
            return jsonify({"message": "Missing email or password"}), 400

        user = User.query.filter_by(email=email).first()

        if user and sha256_crypt.verify(password, user.password):
            return jsonify({"message": "Login successful"}), 200
        else:
            return jsonify({"message": "Invalid email or password or user not found"}), 401



if __name__ =='__main__':
    app.run(port=5555, debug=True)