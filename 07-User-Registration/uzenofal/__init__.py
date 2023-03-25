from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt


db = SQLAlchemy()
app = Flask(__name__)
app.config.from_object('config')
db.init_app(app)
bcrypt = Bcrypt()

from uzenofal import routes