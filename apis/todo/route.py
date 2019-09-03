from flask_restplus import Namespace, Resource, fields

# This is swagger document title and discription
api = Namespace('To Do', description='To DO list')

# Model for cat json data - it will help for validation
todo = api.model('Todo', {
    'id': fields.Integer(required=True, description='The todo identifier'),
    'name': fields.String(required=True, description='The todo name'),
    'description': fields.String(required=True, description='The todo description'),
})

TODOS = [
    {'id': '1', 'name': 'Python project','description':'Detail to do information'},
]

@api.route('/')
class TodoLIst(Resource):
    @api.doc('list_todo')
    @api.marshal_list_with(todo)
    def get(self):
        '''List all todos'''
        return TODOS

@api.route('/<id>')
@api.param('id', 'The todo identifier')
@api.response(404, 'Todo not found')
class Todo(Resource):
    @api.doc('get_todo')
    @api.marshal_with(todo)
    def get(self, id):
        '''Fetch a todo given its identifier'''
        for todo in TODOS:
            if todo['id'] == id:
                return todo
        api.abort(404)