import math,os
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
    return f"<h1>{name} is prime</h1>" if isPrimeLC(name) else f"<h4>{name} is NOT prime</h4>"

def isPrimeLC(num):
    num = int(num)
    return False if num < 2 or [False for x in range(2,int(math.sqrt(num))+1) if num % x == 0  ] else True

@app.route('/factors/<name>')    
def get_factors(name):
    name = int(name)
    return f"<h1>The factors of {name} are {[x for x in range(1,name+1) if name % x == 0  ]}</h1>"

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