from flask import Flask
from config import config_options
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_bcrypt import Bcrypt
#creating app configuration

login_manager= LoginManager()
login_manager.login_view= 'signIn'
db = SQLAlchemy()
bcrypt = Bcrypt()


def create_app(config_name):
    app = Flask(__name__)
    app.config.from_object(config_options[config_name])

    # Initializing flask extensions
    db.init_app(app)
    login_manager.init_app(app)
    
    #registering the blueprint
    from .auth import auth as blue_print
    app.register_blueprint(blue_print)
    
    #registering the blueprint
    from .main import main as blue_print
    app.register_blueprint(blue_print)

    #Setting up configuration
    from .request import configure_request
    configure_request(app)


    return app