from flask_sqlalchemy import SQLAlchemy

from RestAPI.app import app

db = SQLAlchemy()
db.init_app(app)


