'''jinja_nato.py'''
from flask import Flask, render_template


app = Flask(__name__)

@app.route("/")
def template_nato():
    '''template_nato'''
    return render_template('nato.html', my_string= "Year Countries join NATO", nato = get_nato())


def get_nato():
    '''get_nato'''
    with open('nato.txt','r') as line:
        countries = []
        country = line.readline().strip("\n").split(",")
        # print(line)
        while len(country) > 1:
            countries.append(country)
            country = line.readline().strip("\n").split(",")
    return countries

if __name__ == '__main__':
    app.run(host='localhost',debug=True, port=4000)
