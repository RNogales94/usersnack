from utils.singleton import Singleton
import pymongo
import os


class DB(metaclass=Singleton):
    def __init__(self):
        mongo_uri = os.environ.get('MONGODB_URI')
        self.db = pymongo.MongoClient(mongo_uri)

