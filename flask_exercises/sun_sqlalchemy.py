from sqlalchemy import Column, ForeignKey, Integer, VARCHAR, Float
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
'''
<h2>Exercise</h2>
Create code that will take the file SUN.csv<br>
1 - Create SQLite database named CI_trades<br>
2 - Create a table called security_master<br>

table structure:<br>
id<br>
symbol<br>
trade_date<br>
close_price<br>
volume<br>

3 - Read the data in from the text file and using SQLAlchemy store the data<br>
4 - Create a function called get_price which uses the symbol to<br>
retreive the symbol, date, closing price and volume using SQLAlchemy <br>
returned in json format<br>'''

Base = declarative_base()   # All clases inherit from here

class StockData(Base):
    __tablename__ = 'security_master'     # REQUIRED !!!!!!!!
    id = Column(Integer, primary_key=True)      # Every table must have a primary key
    symbol = Column(VARCHAR(10), nullable=False)
    date = Column(VARCHAR(11), nullable=False)
    open = Column(Float(20), nullable=False)
    high = Column(Float(20), nullable=False)
    low = Column(Float(20), nullable=False)
    close = Column(Float(20), nullable=False)
    adj_close = Column(Float(20), nullable=False)
    volume = Column(Integer, nullable=False)

engine = create_engine('sqlite:///CI_trades.db')
Base.metadata.create_all(engine)
Base.metadata.bind = engine
DBSession = sessionmaker(bind=engine)
session = DBSession()

# tables = engine.table_names()   # Which tables exist in the database
# for table in tables:
#     print(table)

def docWriter(x, y):
    with open(f"{x}.csv", "w") as file:
        for n in range(len(y)):
            file.write(y[n])
            file.write("\n")


def csvReader(x):
    engine = create_engine('sqlite:///CI_trades.db')
    DBSession = sessionmaker(bind=engine)
    session = DBSession()
    cnt = 0
    with open(f"{x}", "r") as data:
        row = data.readline().strip("\n").split(",")
        while row[0] != "":
            if cnt > 0:
                session.add_all([StockData(symbol=row[0], date=row[1], open=row[2], high=row[3], low=row[4], close=row[5], adj_close=row[6], volume=row[7])])
                session.commit()
            cnt += 1
            row = data.readline().strip("\n").split(",")

def get_price(x):
    engine = create_engine('sqlite:///CI_trades.db')
    DBSession = sessionmaker(bind=engine)
    session = DBSession()
    res = None
    data = session.query(StockData).filter(StockData.symbol == x)
    if data.first():
        res = {}
        for i in data:
            res[i.id] = [i.symbol, i.date, i.close, i.volume]
    else:
        res = f"Invalid Stock Symbol: {x}"
    return res