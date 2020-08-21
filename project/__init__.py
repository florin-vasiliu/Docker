# project/__init__.py

import os 
from flask import Flask, jsonify
from flask_restx import Resource, Api
from flask_sqlalchemy import SQLAlchemy

# instantiate the app
app = Flask(__name__)

api = Api(app)

# set environment config
app_settings = os.getenv('APP_SETTINGS') 
app.config.from_object(app_settings)

# # ensure that proper configuration was handled
# import sys
# print(app.config, file=sys.stderr)

class Ping(Resource):
    def get(self):
        return {
            'status':'success2',
            'message':'pong!'
        }

api.add_resource(Ping, '/ping')