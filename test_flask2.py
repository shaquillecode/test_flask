from flask import Flask

app = Flask(__name__)


@app.route('/')
def hello():
    return "<h2>Hello World!</h2>"

@app.route('/user/<name>')     # <---- THE NEW ENDPOINT - The variable has to be <name>
def hello_name(name):
    return f"<h1>-- Hola me llamo {name} --</h1>"

if __name__ == '__main__':
    app.run(host='localhost',debug=True, port=2000)