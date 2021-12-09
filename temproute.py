from flask import Flask
from jinja2 import Template
import os

os.chdir('/Users/shaq/Desktop/Django/test_flask/')

app = Flask(__name__)

# /FtoC<br>
# /CtoF<br>

@app.route('/FtoC/<temp>')
def f_to_c(temp):
    x = """
<p>{{func(t,conv_type='F')}}</p>
"""
    template = Template(x)
    return template.render(func=get_temp_convert, t = temp)

@app.route('/CtoF/<temp>')
def c_to_f(temp):
    x = """
<p>{{func(t,conv_type='C')}}</b></p>
"""
    template = Template(x)
    return template.render(func=get_temp_convert, t = temp)

def get_temp_convert(t,**kwargs):
    # temp = 212
    temp_type = kwargs['conv_type']
    if temp_type == 'F':
        return (int(t) - 32)*(5/9)
    elif temp_type == 'C':
        return (int(t)*(9/5) + 32)
    else:
        return 'No converter'

if __name__ == '__main__':
    app.run(host='localhost',debug=True, port=4000)