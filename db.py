from utils.singleton import Singleton
import pymongo
import os
from pizza import Pizza
from order import Order
from extra import Extra

"""
We create the DB class as an interface for the database,
the objective of this class is separate the logic of the DB implementation
this way later will be easier change the DB engine if needed,
because we only will have to modify this file
"""


class DB(metaclass=Singleton):
    def __init__(self):
        mongo_uri = os.environ.get('MONGODB_URI',  'mongodb://heroku_q32gfzdw:t7ee55bddhloqev0bh77aqlm12@ds047114.mlab.com:47114/heroku_q32gfzdw')
        self.db = pymongo.MongoClient(mongo_uri, retryWrites=False).get_database(os.environ.get('DB_NAME', 'heroku_q32gfzdw'))

    def __get_all_items(self, collection_name):
        return list(self.db[collection_name].find({}, {'_id': 0}))

    def get_pizzas(self):
        raw_pizzas = self.__get_all_items('pizzas')
        pizzas = [Pizza.load(p) for p in raw_pizzas]
        return pizzas

    def get_pizza(self, id):
        try:
            id = int(id)
        except ValueError:
            return None

        raw = self.db.pizzas.find_one({'id': int(id)}, {'_id': 0})
        if raw is None:
            return None
        pizza = Pizza.load(raw)

        return pizza

    def get_extras(self):
        raw_extras = self.__get_all_items('extras')
        extras = [Extra.load(e) for e in raw_extras]
        return extras

    def get_extra(self, name):
        raw = self.db.extras.find({'name': name}, {'_id': 0})
        extra = Extra.load(raw)
        return extra

    def get_orders(self):
        raw_orders = self.__get_all_items('orders')
        orders = [Order.load(raw_order) for raw_order in raw_orders]
        return orders

    def insert_order(self, order):
        raw_order = order.serialize()
        return self.db.orders.insert_one(raw_order.copy())

    # We should have methods for insert/update/delete in all but we are not going to use them in the POC


