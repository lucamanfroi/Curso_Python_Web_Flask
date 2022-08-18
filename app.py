from flask import Flask, render_template, request, session, redirect, url_for

app = Flask('project')
# Creating a secret key
app.secret_key = 'secret'

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

# Login form route
@app.route('/login')
def login():
    return render_template('login.html'), 200

# Login treatment route
@app.route('/login_validation', methods=['POST'])
def login_validation():
    if request.form['user'] == 'manfroi' and request.form['password'] == '12345':
        session['user'] = request.form['user']
        session['code'] = 1
        return redirect(url_for('restricted_access'))
    else:
        return 'User/password wrong, try again.', 200

# Restricted area route
@app.route('/restricted')
def restricted_access():
    if session['code'] == 1:
        return f'Welcome to the restricted area!<br>User: {session["user"]}<br>Código: {session["code"]}', 200
    else:
        return 'Invalid access', 200

app.run()
