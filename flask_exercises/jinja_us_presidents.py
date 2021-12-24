from flask import Flask, render_template
import pandas as pd

app = Flask(__name__)

@app.route("/presidents")
def template_presidents():
    return render_template('presidents.html', my_string="US presidents", presidents=get_presidents()
)

def get_presidents():
    #Read
    df = pd.read_csv('US_Presidents_unordered.txt') 

    #Number
    df['Number'] = df["'Name'"].map(lambda x : int(x.replace("'", '').replace('.', '').split()[0])) 

    #Name
    df["'Name'"] = df["'Name'"].map(lambda x : ' '.join(x.replace("'", '').replace('.', '').split()[1:])) 

    #Term Start
    df["'Term Start'"] = df["'Term Start'"].map(lambda x : x.replace("'", ''))

    #Term End
    df["'Term End'"] = df["'Term End'"].map(lambda x : x.replace("'", ''))

    #Sort
    df = df.sort_values(by=['Number'])

    # drop
    df.drop(columns = ["Number"], inplace=True)
    # print(df.dtypes)
    solution = df
    return solution

# get_presidents()

# for key,value in get_presidents().iterrows():
#     print(key,type(key))
#     print(value,type(value))
if __name__ == '__main__':
    app.run(host='localhost',debug=True, port=8000)