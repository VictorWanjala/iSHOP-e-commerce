from flask import Flask,jsonify,make_response
from flask_migrate import Migrate
from models import db ,User, Review,Product
from flask_restful import Resource, Api

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



if __name__ =='__main__':
    app.run(port=5555, debug=True)