from flask import Flask
from apis import api
from database import DB
from config import Config
import os, sys


def create_app(self):
    app = Flask(__name__)
   
   
    print(f'ENV is set to: {app.config["ENV"]}')
   
    if app.config["ENV"] == "production":
        app.config.from_object("config.ProductionConfig")
        print(f'MONGO_URI: {app.config["MONGO_URI"]}') 
    else:
        app.config.from_object("config.DevelopmentConfig")
        print(f'MONGO_URI: {app.config["MONGO_URI"]}')      
       
    # initializa db
    #db=DB(app)
    DB.init(app,app.config["MONGO_URI"])

    # initializa app
    api.init_app(app)

    return app


