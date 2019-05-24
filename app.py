from flask import Flask
from users import users

app = Flask(__name__)

app.register_blueprint(users)