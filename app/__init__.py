#import extension and third-party

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_migrate import Migrate

#local import

from config import app_config



#deklarasi variabel

db = SQLAlchemy()
login_manager = LoginManager()



def create_app(config_name):

    app = Flask(__name__,instance_relative_config=True)
    app.config.from_object(app_config[config_name])
    app.config.from_pyfile('config.py')
    db.init_app(app)

    login_manager.init_app(app)
    login_manager.login_message = "You must be Logged into access this"
    login_manager.login_view = "auth.login"

    migrate = Migrate(app,db)


    from app import models

    #Blueprint

    from .admin import admin as admin_blueprint
    app.register_blueprint(admin_blueprint)

    return app
