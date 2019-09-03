from flask_restplus import Namespace, Resource, fields
from .model import User
from .validators import Validator

# This is swagger document title and discription
api = Namespace('Users', description='Users related operations')

# Model for cat json data - it will help for validation



USERS = [
    {'id': '1', 'name': 'Avkash'},
]

USERSP = [
    {'id': '1', 'name': 'post avkash'},
]


@api.route('/')
class UserList(Resource):
    @api.doc('list_users')
    @api.marshal_list_with(Validator.User(Resource,api))
    def get(self):
        '''List all users'''
        return User.GetList(self)

    @api.doc('list_users')
    @api.marshal_list_with(Validator.User(Resource,api))
    def post(self):
        '''List all users'''
        return USERSP
    

@api.route('/<id>')
@api.param('id', 'The user identifier')
@api.response(404, 'User not found')
class Cat(Resource):
    @api.doc('get_user')
    @api.marshal_with(Validator.User(Resource,api))
    def get(self, id):
        '''Fetch a cat given its identifier'''
        for user in USERS:
            if user['id'] == id:
                return user
        api.abort(404)