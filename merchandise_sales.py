import ui
import traceback
import datetime
import dataManagement

def handle_choice(choice):
    if choice == '1':
        add_data_to_event()
    elif choice == '2':
        add_data_to_item()
    elif choice == '3':
        display_data()
    elif choice == '5':
        delete_data()
    else:
        ui.message('Please enter the correct choice.')
        #print('Please enter the correct choice.')

def add_data_to_event():
    place =ui.input_event()

    today = datetime.datetime.now()
    dataManagement.create_event_table()

    dataManagement.create_sales_table()
    dataManagement.add_to_event(None,today,place)

    #item_id = dataManagement.sales_lastRowID()
    #dataManagement.add_to_sales(None,item_id,no_of_items)

def add_data_to_item():
    input_items = ui.input_item()
    dataManagement.create_item_table()
    dataManagement.add_to_item(None,input_items[0], input_items[1], input_items[2], input_items[3])

def display_data():
    dataManagement.show_Events_data()
    print()
    dataManagement.show_Items_data()
    print()
    dataManagement.show_sales_data()

def delete_data():
    dataManagement.delete_item_data()
    dataManagement.delete_event_data()
    dataManagement.delete_sale_data()

def main():
    quit = 'q'
    choice = None
    while choice!=quit:
        choice = ui.get_menu_choices()
        handle_choice(choice)
if __name__ == '__main__':
    main()
