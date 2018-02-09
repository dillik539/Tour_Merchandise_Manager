import ui
import traceback
import datetime
import dataManagement




def handle_choice(choice):
    if choice == '1':
        add_data()
    elif choice == '2':
        display_data()
    elif choice == '5':
        delete_data()
    else:
        print('Please enter the correct choice.')

def add_data():
    place =input('Enter the venue: ')
    item_name = input('Enter the item name: ')
    item_price = input('Enter the item price: ')
    no_of_items = input('Enter the number of items: ')
    today = datetime.datetime.now()
    dataManagement.create_event_table()
    dataManagement.create_item_table()
    dataManagement.create_sales_table()
    dataManagement.add_to_event(None,today,place)
    event_id = dataManagement.last_rowid()
    dataManagement.add_to_item(None,event_id, item_name, item_price, no_of_items)
    item_id = dataManagement.sales_lastRowID()
    dataManagement.add_to_sales(None,item_id,no_of_items)

def display_data():
    dataManagement.show_Events_data()
    print()
    dataManagement.show_Items_data()
    print()
    dataManagement.show_sales_data()

def delete_data():
    dataManagement.delete_item_data()
    dataManagement.delete_event_data()

def main():
    quit = 'q'
    choice = None
    while choice!=quit:
        choice = ui.get_menu_choices()
        handle_choice(choice)
if __name__ == '__main__':
    main()
