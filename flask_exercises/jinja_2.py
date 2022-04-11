"""jinja_2.py"""
import math
from flask import Flask, render_template


app = Flask(__name__)

@app.route("/")
def template_test():
    return render_template('fibonacci.html', my_string="Fibonacci Sequence",
                           fib=[x for x in calcFibonacci(20,[1,1])][-1])

def calcFibonacci(n=2,seed=[1,1]):
    if not isinstance(seed,list):
        return 'Cannot generate Fibonacci'
    for i in range(n):
        seed.append(seed[-2]+seed[-1])
        yield seed

@app.route("/numbers")
def template_number():
    return render_template('numbers_table.html', my_string="Numbers and Squares", numbers=[x for x in range(2,20)])

@app.route("/prime")
def template_prime():
    return render_template('prime.html', my_string="Prime Finder", prime = [f"The number {i} is {'prime' if isPrimeLC(i) else 'not prime'}" for i in range(2,24)])

def isPrimeLC(num):
    '''Prime Finder'''
    return False if num < 2 or [False for i in range(2,int(math.sqrt(num))+1) if num % i == 0] else True




if __name__ == '__main__':
    app.run(host='localhost',debug=True, port=8000)
