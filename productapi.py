from flask_restful import Resource
from flask_restful import fields, marshal_with, reqparse
from models import Product, db


#do I need to make a small search option? To look up Product ID?

class ProductAPI(Resource):

	def get(self, product_text):
		tab = product.query.filter_by(product_text.lower() in product_name.lower())
		




