import flask
from flask import render_template

app = flask.Flask(__name__)

@app.route('/')
def home():
    return render_template("home.html")

@app.route('/eggs/')
def eggs():
    return render_template("eggs.html")

@app.route('/mushroom/')
def mushroom():
    return render_template("mushroom.html")

@app.route('/barramundi/')
def barramundi():
    return render_template("barramundi.html")

if __name__ == '__main__':
    app.run()