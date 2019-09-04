from flask_restplus import Namespace, fields
from flask import jsonify
from database import DB
from apis.utils.common import output_json


def dto(self,ns):

    Post = ns.model('Post', {
        '_id': fields.String(required=False, description='Post Title'),
        'title': fields.String(required=True, description='Post Title'),
        'content': fields.String(required=True, description='Post Content'),
        'author': fields.String(required=True, description='Post Author'),
        'is_published': fields.Boolean(required=True, description='Post Status')
    })
   
    
    return Post

def save_post(self,data):
    inserted_id=DB.insert("posts",data)
    status=True
    message="successfully loaded"
    if inserted_id=="":       
        status = False
        message="Not loaded"
    return output_json(inserted_id,message,status)

def get_post(self,title):
    return DB.find_one("posts",{"title": title})
def get_posts(self):
    message="successfully loaded"
    posts=DB.find_all("posts")

    return output_json(posts,message)
            
    #$return jsonify(message="user already exists",status="false")
        

   