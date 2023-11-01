from flask import Flask,jsonify,make_response, request, session
from flask_migrate import Migrate
from flask_cors import CORS
from models import db ,User, Review,Product
from flask_restful import Resource, Api
from passlib.hash import sha256_crypt


app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"]='sqlite:///app.db'
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

api=Api(app)

CORS(app)
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
        name = request.form.get('name')
        email = request.form.get('email')
        password = request.form.get('password')

        if name and email and password:
            hashed_pass = sha256_crypt.hash(password)
            new_user = User(name=name, email=email, password=hashed_pass)
            db.session.add(new_user)
            db.session.commit()
            
            return new_user.to_dict(),201
       
    
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

class ReviewProduct(Resource):
    def get(self, id):
        review = Review.query.filter_by(id=id).first()
        response_dict = review.to_dict()
        response = make_response(jsonify(response_dict), 200)
        response.headers["Content-Type"]= "application/json"
        return response
        
        
    def post(self):
        new_review = Review(
            review = request.form["review"],
            product_id= request.form["product_id"],
            user_id= request.form["user_id"]
        )
        db.session.add(new_review)
        db.session.commit()

        response_dict = new_review.to_dict()
        response = make_response(
            jsonify(response_dict), 201
        )
        return response
    
    def patch(self,id):
        updated_review = Review.query.filter_by(id=id).first()
        for attr in request.form:
            setattr(updated_review, attr, request.form.get(attr))
        db.session.add(updated_review)
        db.session.commit()

        review_dict = updated_review.to_dict()
        response = make_response(
            jsonify(review_dict), 200
        )
        return response

    
    def delete(self,id):
        delete_review = Review.query.filter_by(id=id).first()
        db.session.delete(delete_review)
        db.session.commit()

        response_dict = {"message":"Review deleted successfully"}
        response = make_response(jsonify(response_dict), 200)
        return response
    

        

       

api.add_resource(ReviewProduct,'/reviews/<int:id>')


if __name__ =='__main__':
    app.run(port=5555, debug=True)