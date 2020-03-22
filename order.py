from pizza import Pizza
from extra import Extra


class Order:
    def __init__(self, pizza=None, extras=[]):
        self.pizza = pizza
        self.extras = extras

    @classmethod
    def load(cls, obj):
        order = Order()
        pizza = Pizza(obj['pizza'])
        extras = Extra(obj['extras'])
        order.pizza = pizza
        order.extras = extras
        return order

    def serialize(self):
        return {
                    'pizza': self.pizza.serialize(),
                    'extras': [e.serialize() for e in self.extras],
                }
