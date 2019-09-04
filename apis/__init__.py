from flask_restplus import Api

from .user.route import api as ns1
from .todo.route import api as ns2


api = Api(
    title='My Title',
    version='1.0',
    description='A description',
    # All API metadatas
)
api.add_namespace(ns1, path='/api/v1/users')
api.add_namespace(ns2, path='/api/v1/todos')


