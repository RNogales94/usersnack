

class Pizza:
    def __init__(self, id=None, name=None, price=None, ingredients=None, img=None):
        self.id = id
        self.name = name
        self.price = price
        self.ingredients = ingredients
        self.img = img

    @classmethod
    def load(cls, obj):
        pizza = Pizza(id=obj['id'],
                      name=obj['name'],
                      price=obj['price'],
                      ingredients=obj['ingredients'],
                      img=obj['img']
                      )
        return pizza

    def to_dict(self):
        return {
                    'id': self.id,
                    'name': self.name,
                    'price': self.price,
                    'ingredients': self.ingredients,
                    'img': self.img,
                }

