from flask_restplus import Namespace, Resource, fields
from .model import User

# This is swagger document title and discription
api = Namespace('Users', description='Users related operations')

# Model for cat json data - it will help for validation
user = api.model('User', {
    'id': fields.Integer(required=True, description='The user identifier'),
    'name': fields.String(required=True, description='The user name'),
})


USERS = [
    {'id': '1', 'name': 'Avkash'},
]

USERSP = [
    {'id': '1', 'name': 'post avkash'},
]


@api.route('/')
class UserList(Resource):
    @api.doc('list_users')
    @api.marshal_list_with(user)
    def get(self):
        '''List all users'''
        return User.GetList

    @api.doc('list_users')
    @api.marshal_list_with(user)
    def post(self):
        '''List all users'''
        return USERSP
    

@api.route('/<id>')
@api.param('id', 'The user identifier')
@api.response(404, 'User not found')
class Cat(Resource):
    @api.doc('get_user')
    @api.marshal_with(user)
    def get(self, id):
        '''Fetch a cat given its identifier'''
        for user in USERS:
            if user['id'] == id:
                return user
        api.abort(404)