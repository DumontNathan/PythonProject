from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager

app = Flask( __name__ ) 
app.config['SECRET_KEY'] = 'eaad77e006e1146f85fcbf1e80778798'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///flaskr.db'  #Relative path to current flaskr.db file
db = SQLAlchemy(app)
bcrypt = Bcrypt(app)  #Password hasher
loginManager = LoginManager(app)

from app import routes