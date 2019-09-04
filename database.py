import pymongo
from flask import Flask
from bson import json_util, ObjectId
import json
from flask_restplus import fields, marshal


class DB(object):
    def __init__(self):
        pass
            
    @staticmethod
    def init(app):
        client = pymongo.MongoClient(app.config["MONGO_URI"])
        DB.DATABASE = client[app.config["DB_NAME"]]

    @staticmethod
    def insert(collection, data):

        #page_sanitized = json.loads(json_util.dumps(DB.DATABASE[collection].insert(data)))
        return str(DB.DATABASE[collection].insert(data))

    @staticmethod
    def find_one(collection, query):
        #page_sanitized = json.loads(json_util.dumps(DB.DATABASE[collection].find_one(query)))
        page_sanitized = json.loads(json_util.dumps(DB.DATABASE[collection].find_one(query)))
        return page_sanitized

    @staticmethod
    def find_all(collection):
        data=DB.DATABASE[collection].find()
        page_sanitized = json.loads(json_util.dumps(data))
        return page_sanitized
