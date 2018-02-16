import sqlite3
from events import Events
from items import Items
from sales import Sales

db_name = 'Tour_Merchandise_Manager.db'

def create_event_table():
    with sqlite3.connect(db_name) as db:
        cur = db.cursor()
        cur.execute('''CREATE TABLE IF NOT EXISTS Events (Event_ID INTEGER PRIMARY KEY, Event_date DATE, Venue TEXT)''')


def create_item_table():
    with sqlite3.connect(db_name) as db:
        cur = db.cursor()
        cur.execute('''CREATE TABLE IF NOT EXISTS Items (Item_ID INTEGER PRIMARY KEY, Event_ID INTEGER REFERENCES Events(Event_ID),Item_Name TEXT, Item_Price MONEY, Item_Qty INTEGER)''')


def create_sales_table():
    with sqlite3.connect(db_name) as db:
        cur = db.cursor()
        cur.execute('''CREATE TABLE IF NOT EXISTS Sales (Sales_ID INTEGER PRIMARY KEY, Item_ID INTEGER REFERENCES Items (Item_ID), Sold_Qty INTEGER)''')


def add_to_event(id,e_date,place):
    event = Events(id,e_date,place)
    with sqlite3.connect(db_name) as db:
        cur = db.cursor()
        sql_statement = ('INSERT INTO Events VALUES (:id,:e_date,:place)')
        cur.execute(sql_statement,{'id':event.get_event_id(),'e_date': event.get_event_date(),'place': event.get_venue()})

def add_to_item(id, e_id, name, price, qty):
    item = Items(id, e_id, name, price, qty)
    with sqlite3.connect(db_name) as db:
        cur = db.cursor()
        cur.execute('PRAGMA foreign_keys = ON')
        sql_statement = ('INSERT INTO Items VALUES (?,?,?,?,?)')
        cur.execute(sql_statement,(item.get_item_id(),item.get_event_id(), item.get_name(),item.get_price(),item.get_quantity()))

def add_to_sales(id, i_id, sold_qty):
    sale = Sales(id,i_id,sold_qty)
    with sqlite3.connect(db_name) as db:
        cur = db.cursor()
        cur.execute('PRAGMA foreign_keys = ON')
        sql_statement = ('INSERT INTO Sales VALUES (?,?,?)')
        cur.execute(sql_statement,(sale.get_sales_id(),sale.get_item_id(), sale.get_sold_qty()))

def delete_event_data():
    data_to_delete = input('Enter the id: ')
    with sqlite3.connect(db_name) as db:
        cur = db.cursor()
        cur.execute('DELETE FROM Events WHERE Event_ID = ?',(data_to_delete,))

def delete_item_data():
    data_to_delete = input('Enter the id: ')
    with sqlite3.connect(db_name) as db:
        cur = db.cursor()
        cur.execute('DELETE FROM Items WHERE Item_ID = ?',(data_to_delete,))

def delete_sale_data():
    data_to_delete = input('Enter the id: ')
    with sqlite3.connect(db_name) as db:
        cur = db.cursor()
        cur.execute('DELETE FROM Sales WHERE Sales_ID = ?', (data_to_delete,))

def show_Events_data():
    with sqlite3.connect(db_name) as db:
        cur = db.cursor()
        for r in cur.execute('SELECT * FROM Events'):
            print (r)

def show_Items_data():
    with sqlite3.connect(db_name) as db:
        cur = db.cursor()
        for r in cur.execute('SELECT * FROM Items'):
            print(r)

def show_sales_data():
    db = sqlite3.connect(db_name)
    cur = db.cursor()
    for r in cur.execute('SELECT * FROM Sales'):
        print(r)

def last_rowid():
    with sqlite3.connect(db_name) as db:
        cur = db.cursor()
        last_row = cur.execute('SELECT Event_ID FROM Events ORDER BY Event_ID DESC LIMIT 1').fetchone()
        last_row = last_row[0]
        return last_row

def sales_lastRowID():
    db = sqlite3.connect(db_name)
    cur = db.cursor()
    last_row = cur.execute('SELECT Item_ID FROM Items ORDER BY Item_ID DESC LIMIT 1').fetchone()
    last_rowID = last_row[0]
    return last_rowID
