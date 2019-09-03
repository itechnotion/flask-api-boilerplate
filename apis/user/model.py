from flask_restplus import Resource
USERS = [
    {'id': '1', 'name': 'iTechNotion'},
]

class User(Resource):
    def GetList(self):
        return USERS
