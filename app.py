import datetime

from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def index():
    now = datetime.datetime.now()
    new_year = now.month == 1 and now.day == 1
    headline = "Hello, world!"
    return render_template("index.html", headline=headline, new_year=new_year)

@app.route("/<string:name>")
def hello(name):
    name = name.capitalize()
    return f"Hello, {name}"