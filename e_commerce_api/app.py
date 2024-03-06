from flask import Flask

app = Flask(__name__)

g = {}

@app.route('/goods')
def list_goods():
    return g

@app.route('/launch')
def launch_good():
    pass

@app.route('/discontinue')
def discontinue_good():
    pass

@app.route('/<good_id>/update')
def update_reserve():
    pass

@app.route('/<user_id>/cart')
def add_good_to_cart():
    pass

@app.route('/<user_id>/cart/<good_id>')
def remove_good_from_cart():
    pass

@app.route('/<user_id>/cart')
def list_cart():
    pass

@app.route('/<user_id>/cart/checkout')
def checkout():
    return {'receipt_id': ''}

@app.route('/<user_id>/orders')
def list_orders():
    pass
