from flask import Flask, request, redirect, Response, abort
import json
import os

from pizza import Pizza
from order import Order
from extra import Extra

from db import DB

app = Flask(__name__)
db = DB()


@app.route("/")
def index():
    return Response(json.dumps({}), status=200)


@app.route("/api/v1/pizzas/")
def pizzas():
    pizzas = db.get_pizzas()
    response = json.dumps([pizza.serialize() for pizza in pizzas])
    return Response(response, status=200, mimetype='application/json')


@app.route("/api/v1/pizza/<id>")
def pizza(id):
    pizza = db.get_pizza(id)
    if pizza is None:
        return Response(json.dumps({'error': f'pizza id={id} not found'}), status=404, mimetype='application/json')

    return Response(json.dumps(pizza.serialize()), status=200, mimetype='application/json')


@app.route("/api/v1/extras/")
def extras():
    return Response(json.dumps([]), status=200)


@app.route("/api/v1/extra/<name>")
def extra(name):
    return Response(json.dumps({"name": name, "price": 1.2}), status=200)


@app.route("/api/v1/orders")
def get_orders():

    orders = db.get_orders()
    response = json.dumps([o.serialize() for o in orders])

    return Response(response=response, status=200, mimetype='application/json')


@app.route("/api/v1/order", methods=['POST'])
def register_order():
    raw_pizza = request.json.get('pizza')
    raw_extras = request.json.get('extras')

    pizza = Pizza.load(raw_pizza)
    extras = [Extra.load(e) for e in raw_extras]

    order = Order(pizza=pizza, extras=extras)
    db.insert_order(order)

    return Response(json.dumps(order.serialize()), status=200, mimetype='application/json')


@app.route("/api/v1/get-order-price", methods=['POST'])
def order_price():
    raw_pizza = request.json.get('pizza')
    raw_extras = request.json.get('extras')

    pizza = Pizza.load(raw_pizza)
    extras = [Extra.load(e) for e in raw_extras]

    order = Order(pizza=pizza, extras=extras)
    price = order.get_total_price()

    return Response(json.dumps({"price": price}), status=200, mimetype='application/json')


if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    env = os.environ.get('ENVIRONMENT', 'DEV')
    if env == 'PRD':
        debug = False
        host = '0.0.0.0'
    else:
        debug = True
        host = '127.0.0.1'

    app.run(host=host, port=port, debug=debug)
