from flask import Flask

app = Flask(__name__)

g = {}

@app.route('/goods')
def list_goods():
    return g

@app.route('/launch')
def launch_good():
    return g

@app.route('/discontinue')
def discontinue_good():
    pass

def update_reserve():
    pass

def purchase():
    pass

def generate_receipt():
    pass
