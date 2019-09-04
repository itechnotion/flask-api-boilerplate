from flask_restplus import Namespace, Resource, fields

class Validator(Resource):
    def User(self,api):
        user = api.model('User', {
                    '_id': fields.Integer(required=True, description='The user identifier'),
                    'name': fields.String(required=True, description='The user name'),
                    'surname': fields.String(required=True, description='The user name'),
                    'gender': fields.String(required=True, description='The user name'),
                })
        return user
    def Jobs(self,api):
        user = api.model('Jobs', {
                    '_id': fields.String(required=False, description='The user identifier'),
                    'name': fields.String(required=True, description='The user name'),
                    'created_date': fields.String(required=True, description='The user name')
                })
        return user
  