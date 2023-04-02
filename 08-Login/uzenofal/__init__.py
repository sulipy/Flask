from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager


db = SQLAlchemy()
app = Flask(__name__)
app.config.from_object('config')
db.init_app(app)
bcrypt = Bcrypt()
login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_message = 'Ennek az oldalnak az elérése belépéshez kötött!'
login_manager.login_message_category = 'danger'
login_manager.login_view = 'login'

from uzenofal import routes