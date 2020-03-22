from pizza import Pizza
from extra import Extra


class Order:
    def __init__(self, order):
        self.pizza = Pizza(order['pizza'])
        self.extras = Extra(order['extras'])

    def to_dict(self):
        return {
                    'pizza': self.pizza.to_dict(),
                    'extras': [e.to_dict() for e in self.extras],
                }