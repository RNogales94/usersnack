

class Extra:
    def __init__(self, dict):
        self.name = dict['name']
        self.price = dict['price']

    def to_dict(self):
        return {
            'name': self.name,
            'price': self.price
        }
