import flask
from flask import render_template, request, redirect

app = flask.Flask(__name__)
farm_list = []

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/farms/', methods=['GET', 'POST'])
def farms():
    if request.method == 'POST':
        # Add the new farm's information to the list
        farm = {
            'name': request.form['name'],
            'location': request.form['location'],
            'produce': request.form['produce'],
            'methods': request.form['methods'],
            'process': request.form['process']
        }
        farm_list.append(farm)
        return redirect('/farms/')
    else:
        return render_template('farms.html', farms=farm_list)

@app.route('/home/')
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