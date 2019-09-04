import pymongo
from flask import Flask
from bson import json_util, ObjectId
import json


class DB(object):
    def __init__(self):
        pass
            
    @staticmethod
    def init(self,URI):
        client = pymongo.MongoClient(URI)
        DB.DATABASE = client['test']

    @staticmethod
    def insert(collection, data):
        DB.DATABASE[collection].insert(data)

    @staticmethod
    def find_one(collection, query):
        page_sanitized = json.loads(json_util.dumps(DB.DATABASE[collection].find_one(query)))
        return page_sanitized
