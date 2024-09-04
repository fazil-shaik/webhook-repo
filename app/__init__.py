from flask import Flask
from .database import initialize_db

app = Flask(__name__)
app.config.from_object('config.Config')

initialize_db(app)

from app import routes
