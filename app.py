from flask import Flask, render_template

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
@app.route("/test/<var>")
def funcao_teste(var = ""):
    return "Testing new route<br>Var: {}".format(var), 200

app.run()
