"""jinja_states.py"""
from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def template_test():
    '''template_test'''
    return render_template('states.html', my_string="US States", states=get_states()
)

def get_states():
    '''get_states'''
    states = []
    with open('states.txt','r') as file:
        line = file.readline()
        # print(line)
        while line:
            line=line.strip().strip('\n')
            states.append(line)
            line = file.readline()
    return states


if __name__ == '__main__':
    app.run(host='localhost',debug=True, port=8000)
