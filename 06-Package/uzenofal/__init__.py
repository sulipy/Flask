from flask import Flask
from flask_sqlalchemy import SQLAlchemy


db = SQLAlchemy()
app = Flask(__name__)
app.config.from_object('config')
db.init_app(app)

from uzenofal import routes