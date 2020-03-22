

class Extra:
    def __init__(self, name=None, price=None):
        self.name = name
        self.price = price

    @classmethod
    def load(cls, obj):
        extra = Extra(name=obj['name'], price=obj['price'])
        return extra

    def serialize(self):
        return {
            'name': self.name,
            'price': self.price
        }
