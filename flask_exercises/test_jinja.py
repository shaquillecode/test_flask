'''test_jinja.py'''
import math
import random
from flask import Flask
from jinja2 import Template

app = Flask(__name__)

@app.route('/')
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

@app.route('/ftoc/<temp>')
def f_to_c(temp):
    x = """
<p>{{func(t,conv_type='F')}}</p>
"""
    template = Template(x)
    return template.render(func=get_temp_convert, t = temp)

@app.route('/ctof/<temp>')
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
        return int(t)*(9/5) + 32
    else:
        return 'No converter'

@app.route('/prime/<number>')
def prime_number(number):
    return f"<h1>{number} is prime</h1>" if isPrimeLC(number) else f"<h1>{number} is NOT prime</h1>"

def isPrimeLC(num):
    num = int(num)
    return False if num < 2 or [False for x in range(2,int(math.sqrt(num))+1) if num % x == 0  ] else True

@app.route('/factors/<number>')
def get_factors(number):
    number = int(number)
    return f"<h1>The factors of {number} are {[x for x in range(1,number+1) if number % x == 0  ]}</h1>"

@app.route('/oddoreven/<number>')
def oddOrEven(number):
    number = int(number)
    if number == 0:
        return "<h1>Neither Odd nor Even</h1>"
    return "<h1>Odd</h1>" if number % 2 == 1 else "<h1>Even</h1>"

@app.route('/squared/<number>')
def squareNumber(number):
    number = int(number)
    if number == 0:
        return "<h1>This is 0 not a square</h1>"
    return f"<h1>{number} is not a square </h1>" if abs(math.sqrt(number) - int(math.sqrt(number))) > 0 else f"<h1>{number} is a square </h1>"

@app.route('/fibonacci/<number>')
def isFibonacciNumber(number):
    """
    Function will find out if parameter is a Fibonacci number
    """
    number = int(number)
    fibonacci = False
    if number >= 0:
        seq = [0,1]
        while seq[-1] <= number:
            seq.append(seq[-2] + seq[-1])
        fibonacci = f"<h1>{number} is a Fibonacci number</h1>" if number in seq else f"<h1>{number} is NOT a Fibonacci number </h1>"
    return fibonacci

@app.route('/sequence/<num_length>')
def calc_fibo(num_length):
    """
    Function will show a Fibonacci sequence with the length of the parameter
    """
    num_length= int(num_length)
    fibon = [0,1]
    num = 2
    while len(fibon) < num_length:
        if isFibonacciNumber(num):
            # print(f'{num} is a Fibonacci number')
            fibon.append(num)
        num += 1
    return f"<h1><strong>{fibon}<strong></h1>"

def isFibonacciNumber(num):
    fibonacci = False
    if num >= 0:
        seq = [0,1]
        while seq[-1] <= num:
            seq.append(seq[-2] + seq[-1])
        fibonacci = True if num in seq else False
    return fibonacci

LYRICS = {'do': 'Doe, a deer a female deer',
         're': 'Ray, A drop of golden sun',
         'me': 'Me, a name I call myself',
         'fa': 'Far, a long long way to run',
         'so': 'Sew, a needle pulling thread',
         'la': 'La, a note to follow so',
         'ti': 'Tea, a drink with jam and bread'}

@app.route('/song/<name>') # <----- New endpoint
def sound_of_music(name):
    res = LYRICS.get(name) if LYRICS.get(name) else f"The note {name} is not part of the song!"
    return f"<h1>{res}</h1>"

if __name__ == '__main__':
    app.run(host='localhost',debug=True, port=8000)
