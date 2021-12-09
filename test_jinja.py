from flask import Flask
from jinja2 import Template
import random
import os

os.chdir('/Users/shaq/Desktop/Django/test_flask/')

app = Flask(__name__) 

@app.route('/Scrooge')
def christmas_carol():
    x = """
<h1>Uncle Scrooge nephews</h1>
<ul>
{% for i in my_list %}
<li><strong>{{ i }}</strong></li>
{% endfor %}
</ul>
"""
    template = Template(x)
    return template.render(my_list=['Huey', 'Dewey', 'Louie'])

if __name__ == '__main__':
    app.run(host='localhost',debug=True, port=8000)