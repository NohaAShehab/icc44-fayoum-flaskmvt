
from flask import Flask

""" call config options"""
from app.config import config_options  # dict

""" call db object from models file """
from app.models import db

""" use migrate """
from flask_migrate import Migrate

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


    "add migrate to the project "
    migrate = Migrate(app, db)

    """ next I need to initialize migration directory
        then generate migration files
        
        go terminal
        cd app 
        export FLASK_APP=flasky
        flask db init  # generate migration directory
        # to generate migration files
        flask db migrate  -m 'create students table'
        
    """

    # register url
    # from app.students.views import  index
    # app.add_url_rule("/students", view_func=index , endpoint='students.index')

    # I need to ask app to use ?? blueprint
    from app.students import student_blueprint
    app.register_blueprint(student_blueprint)




    return app