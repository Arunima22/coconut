from sqlalchemy import DateTime
from datetime import datetime
from sqlalchemy.sql import func
from flask_sqlalchemy import SQLAlchemy
db = SQLAlchemy()

class User(db.Model):
	no_of_users = 0
	__tablename__ = "User"
	user_id = db.Column(db.Integer, autoincrement = True, primary_key = True)
	user_email = db.Column(db.String(150), unique = True, nullable = False)
	user_password = db.Column(db.String(100), nullable = False)
	user_first_name = db.Column(db.String(50), nullable = False)
	user_last_name = db.Column(db.String(50))

class Category(db.Model):

	num_of_categories = 0  #how do we do this? 

	#database stuff
	__tablename__ = "Category"
	category_id = db.Column(db.Integer, autoincrement = True, primary_key = True)
	category_name = db.Column(db.String, unique = True, nullable = False)
	category_description = db.Column(db.String)
	total_products = db.Column(db.Integer, default = 0)
	category_launch_date = db.Column(db.DateTime(timezone=True),
                           server_default=func.now())
	products = db.relationship('Product', backref='Categories', lazy = True)



class Product(db.Model):

	#database stuff
	__tablename__ = "Product"
	product_id = db.Column(db.Integer, autoincrement = True, primary_key = True)
	product_name = db.Column(db.String, unique = True)
	product_description = db.Column(db.Text)
	product_measure = db.Column(db.String, db.ForeignKey("Measure.measure_name"))
	product_quantity = db.Column(db.Integer)
	product_category = db.Column(db.String, db.ForeignKey("Category.category_id"), nullable= False, primary_key = False)
	product_sell_price = db.Column(db.Integer)
	product_launch = db.Column(db.DateTime(timezone=True),
                           server_default=func.now())


# class Inventory(db.Model):

# 	__tablename__ = "Inventory"
# 	product_id = db.Column(db.Integer, db.ForeignKey("Product.product_id"), nullable = False, primary_key = True)
# 	supplier_id = db.Column(db.Integer, db.ForeignKey("Supplier.supplier_id"), nullable= False, primary_key = True)
# 	product_launch_date = db.Column(db.DateTime, db.ForeignKey("Product.product_launch_date"), nullable=False)
# 	product_end_date = db.Column(db.DateTime, nullable = True)
# 	product_cost_price = db.Column(db.Integer)
# 	product_sell_price = db.Column(db.Integer)
# 	product_sold_num = db.Column(db.Integer) #Number of unites sold till date
# 	product_bought_num = db.Column(db.Integer) #Number of units bought till date
# 	product_current_stock = db.Column(db.Integer)
# 	product_status = db.Column(db.String(100), nullable=True, default= "IN STOCK")

class Measure(db.Model):

	no_of_measures = 0
	__tablename__ = "Measure"
	measure_name = db.Column(db.String(10), primary_key = True)
	measure_desc = db.Column(db.String(50))

class Cart(db.Model):
	__tablename__ = "Cart"
	cuser_id = db.Column(db.Integer, db.ForeignKey("User.user_id"), nullable = False, primary_key = True)
	cproduct_id = db.Column(db.Integer, db.ForeignKey("Product.product_id"), nullable = False, primary_key = True)
	cproduct_quantity = db.Column(db.Integer, default = 0)

class Address(db.Model):

	__tablename__ = "Address"
	user_id = db.Column(db.Integer, db.ForeignKey("User.user_id"), nullable = False, primary_key = True)
	user_address = db.Column(db.String(500), primary_key = True, default = "ABC")
	address_nickname = db.Column(db.String(50), default = "Home Address", primary_key = True)
