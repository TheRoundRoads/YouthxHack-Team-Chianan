from flask import Flask, request, redirect, render_template

app = Flask(__name__)

# A list to store information about the farms
farms = []

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/farms', methods=['GET', 'POST'])
def farms_route():
    if request.method == 'POST':
        # Add the new farm's information to the list
        farm = {
            'name': request.form['name'],
            'location': request.form['location'],
            'produce': request.form['produce'],
            'methods': request.form['methods'],
            'process': request.form['process']
        }
        farms.append(farm)
        return redirect('/farms')
    else:
        return render_template('farms.html', farms=farms)

if __name__ == '__main__':
    app.run()
