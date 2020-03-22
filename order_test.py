from order import Order
from pizza import Pizza
from extra import Extra

import pytest


@pytest.fixture
def complete_order():
    pizza = Pizza(
                id=5,
                name="Cheese & Tomato",
                price=11.90,
                ingredients=["tomato", "cheese"],
                img="cheesetomato.jpg"
             )
    peppers = Extra(name="green peppers", price=1.2)
    mushrooms = Extra(name="mushrooms", price=1.2)
    onion = Extra(name="onion", price=1)

    order = Order(pizza=pizza, extras=[peppers, mushrooms, onion])
    return order


@pytest.fixture
def no_extras_order():
    pizza = Pizza(
                   id=5,
                   name="Cheese & Tomato",
                   price=11.90,
                   ingredients=["tomato", "cheese"],
                   img="cheesetomato.jpg"
                )

    order = Order(pizza=pizza)
    return order


def test_class_attributes(complete_order):
   assert isinstance(complete_order.pizza, Pizza)
   assert isinstance(complete_order.extras, list)
   assert isinstance(complete_order.extras[0], Extra)


def test_class_attributes_2(no_extras_order):
   assert isinstance(no_extras_order.pizza, Pizza)
   assert isinstance(no_extras_order.extras, list)


def test_sum_total_price(complete_order):
   assert complete_order.get_total_price() == 15.3


def test_sum_total_price_2(no_extras_order):
   assert no_extras_order.get_total_price() == 11.9


def test_serialize(complete_order):
   assert isinstance(complete_order.serialize(), dict)
   assert isinstance(complete_order.serialize()['pizza'], dict)
   assert isinstance(complete_order.serialize()['extras'], list)
   assert isinstance(complete_order.serialize()['extras'][0], dict)

