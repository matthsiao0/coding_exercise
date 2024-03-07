from flask import Flask, request, make_response

app = Flask(__name__)

good_picture = {'abc': 'def'}
goods_list = {}

@app.route('/goods')
def list_goods():
    response = make_response(goods_list)
    return response

@app.route('/launch', methods = ['POST'])
def launch_good():
    goods_list.update({
        f'{len(goods_list) + 1}' : {
            'goodsName': request.form['goodsName'],
            'price': request.form['price'],
            'reserve': request.form['price'],
            'promotion': request.form['promotion']
        }
    })
    return make_response(f'{len(goods_list)}')

@app.route('/discontinue', methods = ['DELETE'])
def discontinue_good():
    if request.form['goods_id'] not in goods_list:
        return make_response('', 403)
    goods_list.pop(request.form['goods_id'])
    return make_response('', 204)

@app.route('/<good_id>/update')
def update_reserve():
    pass

@app.route('/goods/<good_id>/picture')
def get_good_picture(good_id):
    if good_id not in good_picture:
        return make_response('', 404)
    response = make_response(good_picture[good_id])
    response.cache_control.max_age = 30
    return response

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
