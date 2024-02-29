# Main configurations for the application

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS

# Initialize application
app = Flask(__name__)
# Wrap app in CORS, allowing communication
CORS(app)

# specifying the location of the sqlite database (local)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///contactlistdatabase.db'
# Not going to track changes to the db
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# create instance of the db (allow access)
db = SQLAlchemy(app)
