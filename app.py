from flask import Flask, render_template, redirect
from surveys import Question, Survey
app = Flask(__name__)
from flask_debugtoolbar import DebugToolbarExtension
# app.config['SECRET_KEY'] = "oh-so-secret"
debug = DebugToolbarExtension(app)

responses = []
@app.route("/")
def home_page():
    """Show instructions, survey name, and button to start survey"""
    return render_template("base.html")