from flask import Flask, render_template, request

app = Flask('project')


@app.route('/')
def hello_world():
    name = 'Luca Manfroi'
    products = [
        {'name': 'Dog Food', 'price': 199.99},
        {'name': 'Playstation', 'price': 1999.99}
    ]
    return render_template('hello.html', aProducts=products, n=name), 200

# New route
@app.route('/test')
@app.route('/test/<var>')
def funcao_teste(var=''):
    return f'Testing new route<br>Var: {var}', 200

# Form route
@app.route('/form')
def form():
    return render_template('form.html'), 200

# Form treatment route
@app.route('/receive_form', methods= ['GET', 'POST'])
def receive_form():
    if request.method == 'POST':
        name = request.form['name']
        return f'Name: {name}', 200
    else:
        return 'Cant call GET directly'

app.run()
