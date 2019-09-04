from flask import Flask,jsonify
from database import DB
from config import Config
import os, sys
from werkzeug.exceptions import HTTPException
from werkzeug.exceptions import default_exceptions



def create_app(object):
    app = Flask(__name__)   
    @app.errorhandler(Exception)
    def handle_error(e):
        code = 500
        if isinstance(e, HTTPException):
            code = e.code
        return jsonify(status=code,error=str(e),message="Something went wrong"), code

    for ex in default_exceptions:
        app.register_error_handler(ex, handle_error)


    print(f'ENV is set to: {app.config["ENV"]}')
   
    if app.config["ENV"] == "production":
        app.config.from_object("config.ProductionConfig")
        print(f'MONGO_URI: {app.config["MONGO_URI"]}') 
    else:
        app.config.from_object("config.DevelopmentConfig")
        print(f'MONGO_URI: {app.config["MONGO_URI"]}')      
       
    # initializa db
    DB.init(app)
    return app


