import math, os
from flask import Flask

os.chdir('/Users/shaq/Desktop/Django/test_flask/')
app = Flask(__name__)

@app.route('/')
def index():
    return "<h1>Flask is so cool and fun</h1>"

@app.route('/user/<name>')
def hello(name):
    return "Hello {}!".format(name)

@app.route('/number/<name>')
def prime_number(name):
    return f"<h1>{name} is prime</h1>" if isPrimeLC(name) else f"<h1>{name} is NOT prime</h1>"

def isPrimeLC(num):
    num = int(num)
    return False if num < 2 or [False for x in range(2,int(math.sqrt(num))+1) if num % x == 0  ] else True

@app.route('/factors/<name>')    
def get_factors(name):
    name = int(name)
    return f"<h1>The factors of {name} are {[x for x in range(1,name+1) if name % x == 0  ]}</h1>"

@app.route('/oddoreven/<name>') 
def oddOrEven(name):
    name = int(name)
    if name == 0:
        return "<h1>Neither Odd nor Even</h1>"
    return "<h1>Odd</h1>" if name % 2 == 1 else "<h1>Even</h1>"

@app.route('/squared/<name>')
def squareNumber(name):
    name = int(name)
    return f"<h1>{name} is not a square </h1>" if abs(math.sqrt(name) - int(math.sqrt(name))) > 0 else f"<h1>{name} is a square </h1>"

@app.route('/fibonacci/<name>')
def isFibonacciNumber(name):
    """
    Function will find out if parameter is a Fibonacci number
    """
    name = int(name)
    fibonacci = False
    if name >= 0:
        seq = [0,1]
        while seq[-1] <= name:
            seq.append(seq[-2] + seq[-1])
        fibonacci = f"<h1>{name} is a Fibonacci number</h1>" if name in seq else f"<h1>{name} is NOT a Fibonacci number </h1>" 
    return fibonacci

@app.route('/sequence/<name>')
def calc_fibo(name):
    """
    Function will show if  a Fibonacci sequence with the length of the parameter
    """
    name = int(name)
    fibon = [0,1]
    num = 2
    while len(fibon) < name:
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