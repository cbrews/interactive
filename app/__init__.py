from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from app.authentication import Auth
from app.autoload import Autoloader

web = Flask(__name__, template_folder="../templates")
web.config.from_object('config')
db = SQLAlchemy(web)
auth = Auth()

# Load all application controllers
Autoloader(__path__, __name__)

db.create_all()
