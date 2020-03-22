

class Pizza:
    def __init__(self, dict):
        self.id = dict['id']
        self.name = dict['name']
        self.price = dict['price']
        self.ingredients = dict['ingredients']
        self.img = dict['img']

    def to_dict(self):
        return {
                    'id': self.id,
                    'name': self.name,
                    'price': self.price,
                    'ingredients': self.ingredients,
                    'img': self.img,
                }
