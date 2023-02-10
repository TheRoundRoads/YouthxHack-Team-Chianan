from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def alternatives():
    alternatives_dict = {
        "eggs": ["tofu", "chickpea flour", "flax seeds"],
        "mushrooms": ["portobello mushrooms", "oyster mushrooms", "shiitake mushrooms"],
        "fish": ["red grouper", "sardine", "salmon"]
    }
    return render_template("alternatives.html", alternatives=alternatives_dict)

if __name__ == "__main__":
    app.run()
