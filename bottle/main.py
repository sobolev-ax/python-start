from bottle import Bottle, run, template

app = Bottle()

@app.route('/')
@app.route('/hello/<name>')
def home(name='World'):
    return template('<h1>Hello, {{name}}!</h1>', name=name)

run(app, host='localhost', port=8080)
