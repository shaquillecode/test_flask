from flask import Flask
import os
from flask import render_template

os.chdir('/Users/shaq/Desktop/Django/test_flask/')

app = Flask(__name__) 

@app.route('/index')
def index():
    return render_template('index.html')

@app.route('/user/<name>')
def user(name):
    return render_template('user.html, name=name')

@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404

@app.errorhandler(500)
def internal_server_error(e):
    return render_template('500.html'), 500

if __name__ == '__main__':
    app.run(host='localhost',debug=True, port=8000)