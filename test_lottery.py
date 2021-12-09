from flask import Flask
from jinja2 import Template
import random
import os

os.chdir('/Users/shaq/Desktop/Django/test_flask/')
app = Flask(__name__) 

@app.route('/lottery')
def luck_numbers():
    lottery = gen_lucky_numbers()
    x = """
<p>Your Lucky Numbers Are</p>
<ul>
{% for i in my_list %}
<li>{{ i }}</li>
{% endfor %}
</ul>
"""
    template = Template(x)
    return template.render(my_list=lottery)

def gen_lucky_numbers():
    return [ random.randint(1,61) for x in range(6)]
    
if __name__ == '__main__':
    app.run(host='localhost',debug=True, port=8000)