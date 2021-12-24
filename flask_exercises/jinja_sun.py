from flask import Flask, render_template
import os

# Display the contents of sun.csv in table format
# Display only the first 20 dates of trade date, closing price ,
# and volume

app = Flask(__name__)

os.chdir("/Users/shaq/Desktop/Django/")

x = "SUN1.CSV"

@app.route("/csv")
def template_csv():
    return render_template('sun.html', my_string= "Stock Information", csv = csvReader(x)) 

def csvReader(x):   
    cnt = 0
    with open(f"{x}", "r") as data:
        sun = []
        row = data.readline().strip("\n").split(",")
        # print(row)
        while len(row) > cnt:
            sun.append(row)
            row = data.readline().strip("\n").split(",")            
            cnt += 1
        # print(sun)
    return sun


# [symbol=row[0], date=row[1], open=row[2], high=row[3], low=row[4], close=row[5], adj_close=row[6], volume=row[7]]

if __name__ == '__main__':
    app.run(host='localhost',debug=True, port=4000)