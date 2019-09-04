'''
Refer below link for API metadata
https://flask-restplus.readthedocs.io/en/stable/api.html

'''

from flask_restplus import Api
from flask import Blueprint

from .post.routes import ns as NSpost


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

api.add_namespace(NSpost)

#api.add_namespace(ns1, path='/api/v1/users')
#api.add_namespace(ns2, path='/api/v1/todos')


