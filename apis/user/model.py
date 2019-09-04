from flask_restplus import Resource
from database import DB


USERS = [
    {'id': '1', 'name': 'iTechNotion'},
]

class User(Resource):
    def GetList(self):
        user_list = DB.find_one("users", {"name": 1})
        return user_list
