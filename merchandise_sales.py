import ui
import traceback
import datetime
import dataManagement

def handle_choice(choice):
    if choice == '1':
        ui.message('Please enter the selection from the following to enter data to desired table.')
        choices = ui.get_enter_choices()
        add_data(choices)

    elif choice == '2':
        ui.message('Enter the selection from the following to obtain data from the desired table.')
        choices = ui.get_display_choices()
        display_data(choices)

    elif choice == '3':
        add_data_to_sale()
    elif choice == '4':
        display_data()
    elif choice == '5':
        delete_data()
    elif choice == '6':
        drop_table()
    else:
        ui.message('Please enter the correct choice.')


def add_data(choices):
    if choices == '1':
        place =ui.input_event()
        today = datetime.datetime.now()
        dataManagement.create_event_table()
        dataManagement.create_sales_table()
        dataManagement.add_to_event(None,today,place)
    elif choices == '2':
        input_items = ui.input_item()
        dataManagement.create_item_table()
        dataManagement.add_to_item(None,input_items[0], input_items[1])
    elif choices == '3':
        input_sales = ui.input_sale()
        dataManagement.create_sales_table()
        dataManagement.add_to_sales(None, input_sales[0], input_sales[1], input_sales[2])

def display_data(choices):
    if choices == '1':
        dataManagement.show_Events_data()
    elif choices == '2':
        dataManagement.show_Items_data()
    elif choices == '3':
        dataManagement.show_sales_data()
    else:
        ui.message('Please enter the correct choice.')

def main():
    quit = 'q'
    choice = None
    while choice!=quit:
        choice = ui.get_menu_choices()
        handle_choice(choice)
if __name__ == '__main__':
    main()
