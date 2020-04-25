import datetime

from flask import Flask, render_template, request

app = Flask(__name__)

notes = []

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

@app.route("/loopinjinja")
def loopinjinja():
    names = ["Alice", "Bob", "Charlie"]
    return render_template("loop.html", names=names)

@app.route("/hello", methods=["POST"])
def helloFromForm():
    name = request.form.get("name")
    return render_template("hello.html", name=name)

@app.route("/form")
def getForm():
    return render_template("form.html")

@app.route("/note", methods=["POST", "GET"])
def note():
    if request.method == "POST":
        note = request.form.get("note")
        notes.append(note)

    return render_template("note.html", notes=notes)
