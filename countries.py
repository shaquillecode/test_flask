from flask import Flask,render_template
import os, sqlite3
import re
from pprint import pprint
import math

app = Flask(__name__)


# <h2>Exercise</h2>
# Open the file countries.txt and examine the file format<br>
# Task list<br>
# Open the file. <br>
# Create a database.  <br>
# Create a table called country_info<br>
# load the data<br>
# create an endpoint called '/getData/Currency' <br>
# - print "The currency of XX is YYYY"<br>
# - print "The country XX was not not found"<br>
# create an endpoint called '/getData/Capitals'<br>
# - print "The capital of XX is YY"<br>
# - print "The capital for XX was not found"<br>

print(os.getcwd()) 
os.chdir('/Users/shaq/Desktop/Django/test_flask/')
print(os.getcwd()) 

conn = sqlite3.connect('countries.db') 
curr = conn.cursor()

curr.execute("""DROP TABLE country_info""")
# Step 1 parse the text file
curr.execute("""CREATE TABLE IF NOT EXISTS country_info (
    country TEXT,
    capital TEXT,
    currency TEXT)
""")
conn.commit()  # <=== commit our table to the database
conn.close()


filename = '/Users/shaq/Desktop/Django/test_flask/'

# step 2 - open the countries.txt file

conn = sqlite3.connect('countries.db')
curr = conn.cursor()
curr.execute("""DELETE FROM country_info;""")
conn.commit()
with open(filename+'countries.txt') as fh:
    line = fh.readline()
    while line:
        country,capital,currency = line.split('|')
        country = country.strip("'")
        capital = capital.strip("'")
        if isinstance(currency,str):
            currency = currency.strip('"').strip("'").strip('\n').strip("'").strip()
        else:
            currency = ''.join([ x.strip("'").strip('\n').strip('"') for x in currency])
        print(country,capital,currency)
        curr.execute(f"""INSERT INTO country_info (country,capital,currency) 
        VALUES ('{country}','{capital}','{currency}');""")
        conn.commit()
        line = fh.readline()
conn.close()



@app.route('/getData/currency/<name>')
def get_currency(name):
    conn = sqlite3.connect('countries.db')
    curr = conn.cursor()

    curr.execute("SELECT * FROM country_info WHERE country = '{0}'".format(name))
    currency = curr.fetchone()[2]
    conn.commit()
    return f'<h1>***The currency of {name} is the {currency}***</h1>'

@app.route('/getData/capital/<name>')
def get_capital(name):
    conn = sqlite3.connect('countries.db')
    curr = conn.cursor()

    curr.execute("SELECT * FROM country_info WHERE country = '{0}'".format(name))
    capital = curr.fetchone()[1]
    conn.commit()
    return f'<h1>The capital of {name} is ==> {capital}</h1>'

@app.route('/getData/capitals/<name>')
def get_capital_currency(name):
    conn = sqlite3.connect('countries.db')
    curr = conn.cursor()

    curr.execute("SELECT * FROM country_info WHERE country = '{0}'".format(name))
    capital = curr.fetchone()[1]
    curr.execute("SELECT * FROM country_info WHERE country = '{0}'".format(name))
    currency = curr.fetchone()[2]
    conn.commit()
    return f"<h1>{name}'s capital city is {capital} and uses the {currency} currency</h1>"

@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404

@app.errorhandler(500)
def internal_server_error(e):
    return render_template('500.html'), 500

@app.route('/')
def index():
    return '<h1>Flask is so cool and fun</h1>'

if __name__ == "__main__":
    app.run(host='localhost',debug=True, port=4000)