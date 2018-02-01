import ui
import sqlite3
import traceback
import datetime

db_name = 'Tour_Merchandise_Manager.db'

def handle_choice(choice):
    if choice =='1':
        add_data()
    elif choice == '2':
        show_data()
    else:
        print('Please enter the correct choice.')


def add_data():
    '''take user input and add to respective tables'''
    place = input('Enter venue: ')
    item_name = input('Enter name of item: ')
    item_price = input('Enter price: ')
    No_of_items = input('Enter number of items: ')
    date = datetime.datetime.now()
    create_event_table()

    with sqlite3.connect(db_name) as db:
        cur = db.cursor()
        sql_statement = ('INSERT INTO Events VALUES (?,?,?)')
        cur.execute(sql_statement,(None, date, place))

def create_event_table():
    '''create table'''
    with sqlite3.connect(db_name) as db:
        cur = db.cursor()
        cur.execute('''CREATE TABLE if not exists Events
        (Event_ID INTEGER PRIMARY KEY, Event_date DATETIME, Venue Text)''')

def show_data():
    '''display the data from the table'''
    with sqlite3.connect(db_name) as db:
        cur = db.cursor()
        cur.execute('SELECT * FROM Events')
        for r in cur.execute('SELECT * FROM Events'):
            print(r)

def main():
    quit = 'q'
    choice = None
    while choice!=quit:
        choice = ui.get_menu_choice()
        handle_choice(choice)
main()
