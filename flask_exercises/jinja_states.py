from flask import Flask, render_template
app = Flask(__name__)


@app.route("/states")
def template_test():
    return render_template('jinja_states.html', my_string="US States", states=get_states()
)


# Code Here!
def get_states():
    states = []
    with open('US_states_codes.txt','r') as file:
        line = file.readline()
        # print(line)
        while line:
            line=line.strip().strip('\n')
            states.append(line)
            line = file.readline()
    return states


if __name__ == '__main__':
    app.run(host='localhost',debug=True, port=8000)