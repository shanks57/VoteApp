from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_migrate import Migrate
# local imports
from config import app_config

# db variable initialization
db = SQLAlchemy()

#login_manager initialization
login_manager = LoginManager()


def create_app(config_name):
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_object(app_config[config_name])
    app.config.from_pyfile('config.py')
    db.init_app(app)

    login_manager.init_app(app)
    login_manager.login_message = "Kamu Harus Login Untuk Akses Halaman Ini"


    migrate = Migrate(app,db)

    from app import models

    #blueprint
    from .auth import auth as auth_blueprint
    app.register_blueprint(auth_blueprint, url_prefix='/auth')

    from .admin import admin as admin_blueprint
    app.register_blueprint(admin_blueprint)

    login_manager.blueprint_login_views = {

        'admin' : 'auth.admin_login'

    }

    return app
