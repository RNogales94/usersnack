from db import DB
from order import Order
from extra import Extra
from pizza import Pizza


def test_get_pizzas():
    assert isinstance(DB().get_pizzas(), list)
    assert isinstance(DB().get_pizzas()[0], Pizza)


def test_get_pizza():
    assert isinstance(DB().get_pizza(id=4), Pizza)


def test_get_orders():
    assert isinstance(DB().get_orders(), list)
    assert isinstance(DB().get_orders()[0], Order)


def test_insert_orders():
    pizza = Pizza({
                  "id": 5,
                  "name": "Cheese & Tomato",
                  "price": 11.90,
                  "ingredients": ["tomato", "cheese"],
                  "img": "cheesetomato.jpg"
                })
    peppers = Extra({"name": "green peppers", "price": 1.2})
    mushrooms = Extra({"name": "mushrooms", "price": 1.2})
    onion = Extra({"name": "onion", "price": 1})

    order = Order(pizza=pizza, extras=[peppers, mushrooms, onion])

    assert DB().insert_order(order)
