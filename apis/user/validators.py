from flask_restplus import Namespace, Resource, fields

class Validator(Resource):
    def User(self,api):
        user = api.model('User', {
                    'id': fields.Integer(required=True, description='The user identifier'),
                    'name': fields.String(required=True, description='The user name'),
                })
        return user
  