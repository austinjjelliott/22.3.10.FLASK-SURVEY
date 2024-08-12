from flask import Flask
app = Flask(__name__)
from flask_debugtoolbar import DebugToolbarExtension
# app.config['SECRET_KEY'] = "oh-so-secret"
debug = DebugToolbarExtension(app)