from flask import Flask, render_template

app = Flask(__name__) 

@app.route('/')
def index():
    return render_template('demo_index.html')

@app.route('/user/<name>') # <---- THE NEW ENDPOINT - The variable has to be <name>
def user(name):
    return render_template('user.html', name=name)

@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404

@app.errorhandler(500)
def internal_server_error(e):
    return render_template('500.html'), 500

if __name__ == '__main__':
    app.run(host='localhost',debug=True, port=4000)