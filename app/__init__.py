from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from .config import Config

app = Flask(__name__)
db = SQLAlchemy(app)
app.config['SECRET_KEY'] = 'some$3cretKey'
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:passwordyoucreatedearlier@localhost/db_app'

app.config.from_object(Config)
from app import views,models