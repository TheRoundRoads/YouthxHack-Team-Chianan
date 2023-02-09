import flask
from flask import render_template

app = flask.Flask(__name__)

@app.route('/')
def home():
    return render_template("home.html")

@app.route('/cucumber/')
def cucumber():
    return render_template("cucumber.html")

@app.route('/eggs/')
def eggs():
    return render_template("eggs.html")

@app.route('/chicken/')
def chicken():
    return render_template("chicken.html")

if __name__ == '__main__':
    app.run()