from flask import Flask, request, redirect, Response, abort
import json
import os


app = Flask(__name__)


@app.route("/")
def index():
    return Response(json.dumps({}), status=200)


@app.route("/api/v1/pizza/")
def pizzas():
    return Response(json.dumps([]), status=200)


@app.route("/api/v1/pizza/<id>")
def pizza(id):
    return Response(json.dumps({
                                  "id": id,
                                  "name": "Cheese & Tomato",
                                  "price": 11.90,
                                  "ingredients": ["tomato", "cheese"],
                                  "img": "cheesetomato.jpg"
                                }), status=200)


@app.route("/api/v1/extra/")
def extras():
    return Response(json.dumps([]), status=200)


@app.route("/api/v1/extra/<name>")
def extra(name):
    return Response(json.dumps({"name": name, "price": 1.2}), status=200)


@app.route("/api/v1/order", methods=['POST'])
def register_order():
    pizza = request.json.get('pizza')
    extras = request.json.get('extras')
    price = pizza.get('price') + sum([extra['price'] for extra in extras])

    return Response(json.dumps({'pizza': pizza, 'extras': extras, "price": price}), status=200, mimetype='application/json')


@app.route("/api/v1/order_price", methods=['POST'])
def order_price():
    pizza = request.json.get('pizza')
    extras = request.json.get('extras')
    price = pizza.get('price') + sum([extra['price'] for extra in extras])

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
