# # jinja_1.py
# from flask import Flask, render_template
# app = Flask(__name__)


# @app.route("/")
# def template_test():
#     return render_template('jinja_1.html', my_string="Fibonacci Sequence", fib=[1,1,2,3,5,8,13,21,34,55,89])

# def calcFibonacci(n=2,seed=[1,1]):
#     if not isinstance(seed,list):
#         return 'Cannot generate Fibonacci'
#     for i in range(n):
#         seed.append(seed[-2]+seed[-1])
#         yield seed    

# fib=[x for x in calcFibonacci(20,[1,1])][-1]


# if __name__ == '__main__':
#     app.run(host='localhost',debug=True, port=8000)

# def calcFibonacci(i,arr=[]):
#     while i < len(arr):
#         return i

# calcFibonacci(20,[1,1])



# print(fib)


import math

def isPrimeLC(num):
    return False if num < 2 or [False for i in range(2,int(math.sqrt(num))+1) if num % i == 0] else True

prime = [{i:isPrimeLC(i)} for i in range(2,24)]

print(prime,(type(prime)))

print(prime.items())