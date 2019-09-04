'''
Refer below link for API metadata
https://flask-restplus.readthedocs.io/en/stable/api.html

'''

from flask_restplus import Api
from flask import Blueprint

from .user.route import api as ns1
from .todo.route import api as ns2
from .post.routes import ns as ns3


bp_api_v1 = Blueprint('api', __name__)

api = Api(
    bp_api_v1,
    title='My Title',
    version='1.0',
    description='A description',
    doc='/docs', #Path of documents,
    validate=True

     
    # All API metadatas
)

api.add_namespace(ns1)
api.add_namespace(ns2)
api.add_namespace(ns3)

#api.add_namespace(ns1, path='/api/v1/users')
#api.add_namespace(ns2, path='/api/v1/todos')


