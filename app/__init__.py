
from flask import Flask

""" call config options"""
from app.config import config_options  # dict

""" call db object from models file """
from app.models import db

# 1- create app
def create_app(config_name='dev'):

    app = Flask(__name__)

    current_config = config_options[config_name]  # Class of config
    # configure app with db. ,
    app.config['SQLALCHEMY_DATABASE_URI'] = current_config.SQLALCHEMY_DATABASE_URI
    # another way
    app.config.from_object(current_config)  # read need config. for app from the given class

    # Connect db object with app
    db.init_app(app)

    # register url
    from app.students.views import  index
    app.add_url_rule("/students", view_func=index , endpoint='students.index')




    return app