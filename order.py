from pizza import Pizza
from extra import Extra


class Order:
    def __init__(self, pizza=None, extras=[], name=None, address=None):
        self.pizza = pizza
        self.extras = extras
        self.name = name
        self.address = address

    @classmethod
    def load(cls, obj):
        order = Order(
                    pizza=Pizza.load(obj['pizza']),
                    extras=[Extra.load(e) for e in obj['extras']],
                    name=obj['name'],
                    address=obj['address']
                    )
        return order

    def serialize(self):
        print(self.pizza)
        print(self.extras)
        obj = {
                    'pizza': self.pizza.serialize(),
                    'extras': [e.serialize() for e in self.extras],
                    'name': self.name,
                    'address': self.address
                }
        return obj

    def get_total_price(self):
        price = self.pizza.price + sum([extra.price for extra in self.extras])
        return price
