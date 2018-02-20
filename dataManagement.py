import sqlite3
from events import Events
from items import Items
from sales import Sales

db_name = 'Tour_Merchandise_Manager.db'#database name where all the tables are stored

'''create table to hold event's data'''
def create_event_table():
    with sqlite3.connect(db_name) as db:
        cur = db.cursor()
        cur.execute('''CREATE TABLE IF NOT EXISTS Events (Event_ID INTEGER PRIMARY KEY, Event_date DATE, Venue TEXT)''')

'''create table to hold item's data'''
def create_item_table():
    with sqlite3.connect(db_name) as db:
        cur = db.cursor()
        cur.execute('''CREATE TABLE IF NOT EXISTS Items (Item_ID INTEGER PRIMARY KEY, Event_ID INTEGER REFERENCES Events(Event_ID),Item_Name TEXT)''')

'''create table to hold sale's data'''
def create_sales_table():
    with sqlite3.connect(db_name) as db:
        cur = db.cursor()
        cur.execute('''CREATE TABLE IF NOT EXISTS Sales (Sales_ID INTEGER PRIMARY KEY, Item_ID INTEGER REFERENCES Items (Item_ID), Sale_price MONEY, Sale_Qty INTEGER)''')

'''add event's data'''
def add_to_event(id,e_date,place):
    event = Events(id,e_date,place)
    with sqlite3.connect(db_name) as db:
        cur = db.cursor()
        sql_statement = ('INSERT INTO Events VALUES (:id,:e_date,:place)')
        cur.execute(sql_statement,{'id':event.get_event_id(),'e_date': event.get_event_date(),'place': event.get_venue()})
'''add item's data'''
def add_to_item(id, e_id, name):
    item = Items(id, e_id, name)
    with sqlite3.connect(db_name) as db:
        cur = db.cursor()
        cur.execute('PRAGMA foreign_keys = ON')# forces sqlite to turn on foreign key feature
        sql_statement = ('INSERT INTO Items VALUES (?,?,?)')
        cur.execute(sql_statement,(item.get_item_id(),item.get_event_id(), item.get_name()))
'''add sale's data'''
def add_to_sales(id, i_id, price, qty):
    sale = Sales(id,i_id, price, qty)
    with sqlite3.connect(db_name) as db:
        cur = db.cursor()
        cur.execute('PRAGMA foreign_keys = ON')
        sql_statement = ('INSERT INTO Sales VALUES (?,?,?,?)')
        cur.execute(sql_statement,(sale.get_sales_id(),sale.get_item_id(),sale.get_price(), sale.get_sold_qty()))
'''delete event's specified data'''
def delete_event_data():
    data_to_delete = input('Enter the id: ')
    with sqlite3.connect(db_name) as db:
        cur = db.cursor()
        cur.execute('DELETE FROM Events WHERE Event_ID = ?',(data_to_delete,))
'''delete item's specified data'''
def delete_item_data():
    data_to_delete = input('Enter the id: ')
    with sqlite3.connect(db_name) as db:
        cur = db.cursor()
        cur.execute('DELETE FROM Items WHERE Item_ID = ?',(data_to_delete,))
'''delete sale's specified data'''
def delete_sale_data():
    data_to_delete = input('Enter the id: ')
    with sqlite3.connect(db_name) as db:
        cur = db.cursor()
        cur.execute('DELETE FROM Sales WHERE Sales_ID = ?', (data_to_delete,))
'''display event's data'''
def show_Events_data():
    with sqlite3.connect(db_name) as db:
        cur = db.cursor()
        for r in cur.execute('SELECT * FROM Events'):
            print (r)
'''display item's data'''
def show_Items_data():
    with sqlite3.connect(db_name) as db:
        cur = db.cursor()
        for r in cur.execute('SELECT * FROM Items'):
            print(r)
'''display sale's data'''
def show_sales_data():
    db = sqlite3.connect(db_name)
    cur = db.cursor()
    for r in cur.execute('SELECT * FROM Sales'):
        print(r)
'''update event's data'''
def update_events_table():
    event_id = input('Enter event id: ')
    venue = input('Enter the new venue: ')
    with sqlite3.connect(db_name) as db:
        cur = db.cursor()
        cur.execute('PRAGMA foreign_keys = ON')
        sql_statement = ('UPDATE Events SET Venue = ? WHERE Event_ID = ?')
        cur.execute(sql_statement, (venue, event_id))
'''update item's data'''
def update_items_table():
    item_id = input('Enter item id: ')
    event_id = input('Enter event id: ')
    item = input('Enter the new item: ')
    with sqlite3.connect(db_name) as db:
        cur = db.cursor()
        cur.execute('PRAGMA foreign_keys = ON')
        sql_statement = ('UPDATE Items SET Item_Name = ? WHERE Event_ID = ? AND Item_ID = ?')
        cur.execute(sql_statement, (item, event_id, item_id))
'''update sale's data'''
def update_sales_table():
    sale_id = input('Enter sale id: ')
    item_id = input('Enter item id: ')
    sale_price = input('Enter sale price: ')
    sale_qty = input('Enter new sale quantity: ')
    with sqlite3.connect(db_name) as db:
        cur = db.cursor()
        cur.execute('PRAGMA foreign_keys = ON')
        sql_statement = ('UPDATE Sales SET Sale_Qty = ? WHERE Item_ID = ? AND Sales_ID = ?')
        cur.execute(sql_statement, (sale_qty, item_id, sale_id))
'''drop events table'''
def drop_events_table():
    with sqlite3.connect(db_name) as db:
        cur = db.cursor()
        cur.execute('DROP TABLE Events')
'''drop items table'''
def drop_items_table():
    with sqlite3.connect(db_name) as db:
        cur = db.cursor()
        cur.execute('DROP TABLE Items')
'''drop sales table'''
def drop_sales_table():
    with sqlite3.connect(db_name) as db:
        cur = db.cursor()
        cur.execute('DROP TABLE Sales')
'''search data from the events table based on the id the user supplies'''
def search_events_data():
    search_id = input('Enter id to begin search: ')
    db = sqlite3.connect(db_name)
    cur = db.cursor()
    sql_statement = ('SELECT * FROM Events WHERE Event_ID = ?')
    for r in cur.execute(sql_statement, (search_id,)):
        print(r)
'''search items by id'''
def search_items_data():
    search_id = input('Enter id to begin search: ')
    db = sqlite3.connect(db_name)
    cur = db.cursor()
    sql_statement = ('SELECT * FROM Items WHERE Item_ID = ?')
    for r in cur.execute(sql_statement, (search_id,)):
        print(r)
'''search sales by id'''
def search_sales_data():
    search_id = input('Enter id to begin search: ')
    db = sqlite3.connect(db_name)
    cur = db.cursor()
    sql_statement = ('SELECT * FROM Sales WHERE Sales_ID = ?')
    for r in cur.execute(sql_statement, (search_id,)):
        print(r)
'''display the total number of specific items sold in a specific event'''
def total_items_sold():
    item_id = input('Enter the Item id: ')
    db = sqlite3.connect(db_name)
    cur = db.cursor()
    sql_statement = ('SELECT Venue, Item_Name, SUM(Sale_Qty) FROM Sales JOIN Items ON Sales.Item_ID = Items.Item_ID JOIN Events ON Events.Event_ID = Items.Event_ID WHERE Sales.Item_ID  = ?')
    items_sold = cur.execute(sql_statement, (item_id, )).fetchall()
    for r in items_sold:
        print(r[2], r[1],'were sold at',r[0])
'''find the minimum specific items sold in a specific event'''
def minimum_items_sold():
    item = input('Enter item id: ')
    db = sqlite3.connect(db_name)
    cur = db.cursor()
    sql_statement =  ('SELECT Venue, Item_Name, MIN(Sale_Qty) FROM Events JOIN Items ON Events.Event_ID =  Items.Event_ID JOIN Sales ON Items.Item_ID = Sales.Item_ID WHERE Items.Item_ID = ?')
    for r in cur.execute(sql_statement, (item,)):
        print('At minimum,', r[2], r[1],'were sold at', r[0])
'''find the maximum of specific item sold in a specific event'''
def maximum_items_sold():
    item = input('Enter item id: ')
    db = sqlite3.connect(db_name)
    cur = db.cursor()
    sql_statement = ('SELECT Venue, Item_Name, MAX(Sale_Qty) FROM Events JOIN Items ON Events.Event_ID =  Items.Event_ID JOIN Sales ON Items.Item_ID = Sales.Item_ID WHERE Items.Item_ID = ?')
    for r in cur.execute(sql_statement, (item,)):
        print('At maximum,', r[2], r[1],'were sold at', r[0])
