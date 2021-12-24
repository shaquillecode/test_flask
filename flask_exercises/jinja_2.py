# jinja_2.py
from flask import Flask, render_template
import math

app = Flask(__name__)

@app.route("/")
def template_test():
    return render_template('jinja_1.html', my_string="Fibonacci Sequence", 
                           fib=[x for x in calcFibonacci(20,[1,1])][-1])


@app.route("/numbers")
def template_number():
    return render_template('numbers_table.html', my_string="Numbers and squares", numbers=[x for x in range(2,20)])                         


@app.route("/prime")
def template_prime():
    return render_template('prime.html', my_string="Prime Finder", prime = [{i:isPrimeLC(i)} for i in range(2,24)])   

def isPrimeLC(num):
    return False if num < 2 or [False for i in range(2,int(math.sqrt(num))+1) if num % i == 0] else True


def calcFibonacci(n=2,seed=[1,1]):
    if not isinstance(seed,list):
        return 'Cannot generate Fibonacci'
    for i in range(n):
        seed.append(seed[-2]+seed[-1])
        yield seed 


if __name__ == '__main__':
    app.run(host='localhost',debug=True, port=8000)