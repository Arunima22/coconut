from models import db, User, Product, Category, Measure, Cart, Address #Supplier, Inventory, Manager, Order, OrderDetails, Address, Cart
from flask import Flask, render_template, url_for, redirect, request
from flask import current_app as app
from werkzeug.security import check_password_hash 
import sys
#------------------------SIGN UP SYSTEM---------------------------#

@app.route("/coconut")
def coconut():
	return render_template('home.html')

@app.route('/coconut/user_login', methods=["GET", "POST"])
def user_login():
	if request.method == "POST":
		email = request.form["email"]
		password = request.form["password"]
		guser = User.query.filter_by(user_email=email).first()
		if guser:
			if guser.user_password == password:
				return redirect(url_for('make_homepage', user_id = guser.user_id))
			else:
				return redirect('/coconut/error')
		else:
			return redirect('/coconut/error')
	return render_template('user_login.html')

@app.route('/coconut/admin_login')
def admin_login():
	return render_template('admin_login.html')

@app.route('/coconut/user_signup')
def user_signup():
	return render_template('user_signup.html')


#------------------------USER HOMEPAGE---------------------------#
#Displays only post logging in or signing up 

@app.route('/coconut/home/<user_id>', methods = ["GET", "POST"])
def make_homepage(user_id):
	all_cats = Category.query.all()
	top_products = Product.query.order_by(Product.product_launch.desc()).limit(3) #change the number later
	
	return render_template('user_homepage.html', user_id = user_id, top_products = top_products, all_cats = all_cats)

@app.route('/coconut/home/playing/<user_id>/<category_id>')
def cat_homepage(user_id, category_id):
	list_of_products = Product.query.filter_by(product_category = int(category_id))
	return render_template('user_homepage.html', user_id = user_id, top_products = list_of_products )

@app.route('/coconut/product/<user_id>/<product_id>', methods = ["GET", "POST"])
def product_page(user_id, product_id):
	cannot_delete = True
	if request.method == "POST":
		val = request.form["CartButton"]
		combination = Cart.query.filter_by(cuser_id = user_id, cproduct_id = product_id).first()
		if val == "Add":
			if combination:
				combination.cproduct_quantity = combination.cproduct_quantity + 1
			else: 
				cart_product = Cart(cuser_id = user_id, cproduct_id = product_id, cproduct_quantity = 1)
				db.session.add(cart_product)
		db.session.commit()
		if val == "Delete":
			if combination.cproduct_quantity == 1:
				db.session.delete(combination)
			else:
				combination.cproduct_quantity = combination.cproduct_quantity - 1
		db.session.commit()
	product = Product.query.filter_by(product_id = product_id).first()
	cart_products = Cart.query.filter_by(cuser_id = user_id)
	cart_product_ids = [each.cproduct_id for each in cart_products]
	if product.product_id in cart_product_ids:
		cannot_delete = False
	return render_template('product_page.html', user_id = user_id, product = product, cannot_delete = cannot_delete)
	# else: 
	# 	product = Product.query.filter_by(product_id = product_id).first()
	# 	cart_products = Cart.query.filter_by(cuser_id = user_id)
	# 	cart_product_ids = [each.cproduct_id for each in cart_products]
	# 	return render_template('product_page.html', user_id = user_id, product = product, cannot_delete = cannot_delete)

@app.route('/coconut/home/<user_id>/cart', methods = ["GET", "POST"])
def show_cart(user_id):
	if request.method == "POST":
		val = request.form["cart"]
		temp = list(val)
		product_id = int(temp[0])
		combination = Cart.query.filter_by(cuser_id = user_id, cproduct_id = product_id).first()
		if val == str(product_id) + "Add":
			combination.cproduct_quantity = combination.cproduct_quantity + 1
		db.session.commit()
		if val == str(product_id) + "Del":
			if combination.cproduct_quantity == 1:
				db.session.delete(combination)
			else:
				combination.cproduct_quantity = combination.cproduct_quantity - 1
		db.session.commit()
	cart_products = Cart.query.filter_by(cuser_id = user_id)
	return render_template('cart_page.html', user_id = user_id, cart_products = cart_products)

@app.route('/coconut/home/<user_id>/address', methods = ["GET", "POST"])
def choose_address(user_id):
	if request.method == "POST":
		address = request.form["addresses"]
		payment_method = request.form["payment_methods"]
		return redirect('/coconut/dummy')

	if request.method == "GET":
		user_addresses = Address.query.filter_by(user_id = user_id)
		addresses = [[each.user_address, each.address_nickname] for each in user_addresses]
		for each in addresses:
			print(each,file=sys.stderr)
		return render_template('choose_address.html', addresses = addresses, user_id = user_id)


#------------------------ADMIN PAGES---------------------------#



#------------------------DUMMY PAGES---------------------------#

@app.route('/coconut/dummy')
def dummy():
	return render_template('successful.html')

@app.route('/coconut/error')
def error():
	return render_template('error.html')















