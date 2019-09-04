
from flask import request, Response, make_response, jsonify
from flask_restplus import Resource,Namespace
from bson import json_util
import json
from .model import dto,save_post,get_posts, get_post

ns = Namespace('post', description='post related operations')
_post = dto(object,ns)


@ns.route('/')
class UserList(Resource):
    @ns.doc('list of post')
    #@ns.marshal_list_with(_post)
    def get(self):
        """List all registered users"""
        return get_posts(self)

    @ns.expect(_post, validate=True)
    @ns.response(201, 'User successfully created.')
    @ns.doc('create new post')
    def post(self):
        """Creates a new User """
        data = request.json
        return save_post(self,data=data)
