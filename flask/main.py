import flask, sqlite3
from flask import render_template, request, redirect

app = flask.Flask(__name__)
farm_list = []
items = [{"name": "EGO Swiss roll", "path": "swissroll.jpg", "reason": "exceeding levels of sorbic acid"},
         {"name": "Prego Carbonara Mushroom Pasta Sauce", "path": "sauce.png", "reason": "Product spoilage"},
         {"name": "Mie Sedaap", "path": "noodle.png", "reason": "presence of ethylene oxide"}]
alternatives_dict = {
        "eggs": ["Tofu", "Chickpea Flour", "Flax seeds"],
        "mushrooms": ["Portobello Mushrooms", "Oyster Mushrooms", "Shiitake Mushrooms"],
        "fish": ["Red Grouper", "Sardine", "Salmon"]
    }


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
    return render_template("eggs.html", alternatives=alternatives_dict["eggs"])

@app.route('/mushroom/')
def mushroom():
    return render_template("mushroom.html", alternatives=alternatives_dict["mushrooms"])

@app.route('/barramundi/')
def barramundi():
    return render_template("barramundi.html", alternatives=alternatives_dict["fish"])

@app.route('/recall/')
def recall():
    db = sqlite3.connect("recalls.db")
    return render_template("recall.html", items=items)

if __name__ == '__main__':
    app.run()