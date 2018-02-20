import ui
import traceback
import datetime
import dataManagement

'''hanlde choice for various inputs, queries and displays'''
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
        ui.message('Enter the selection from the following to delete data from desired table.')
        choices = ui.get_delete_choices()
        delete_data(choices)
    elif choice == '4':
        ui.message('Enter the selection from the following to drop desired table.')
        choices = ui.get_drop_table_choices()
        drop_tables(choices)
    elif choice == '5':
        ui.message('Enter the selection from the following to search data from the desired table.')
        choices = ui.get_search_data_choices()
        search_data(choices)
    elif choice == '6':
        ui.message('Enter the selection from the following to update data from desired table.')
        choices = ui.get_update_data_choices()
        update_tables(choices)
    elif choice == '7':
        ui.message('Enter the selection from the following to query data from the database.')
        choices = ui.get_query_choices()
        query_data(choices)

'''add data to tables'''
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
'''display data from the tables'''
def display_data(choices):
    if choices == '1':
        dataManagement.show_Events_data()
    elif choices == '2':
        dataManagement.show_Items_data()
    elif choices == '3':
        dataManagement.show_sales_data()
    else:
        ui.message('Please enter the correct choice.')
'''delete data from the tables based on the choices'''
def delete_data(choices):
    if choices == '1':
        dataManagement.delete_event_data()
    elif choices == '2':
        dataManagement.delete_item_data()
    elif choices == '3':
        dataManagement.delete_sale_data()
    else:
        ui.message('Please enter the correct choice.')
'''update data in the tables based on the choices'''
def update_tables(choices):
    if choices == '1':
        dataManagement.update_events_table()
    elif choices == '2':
        dataManagement.update_items_table()
    elif choices == '3':
        dataManagement.update_sales_table()
    else:
        ui.message('Please enter the correct choice.')
'''drop tables based on the choices'''
def drop_tables(choices):
    if choices == '1':
        dataManagement.drop_events_table()
    elif choices == '2':
        dataManagement.drop_items_table()
    elif choices == '3':
        dataManagement.drop_sales_table()
    else:
        ui.message('Please enter the correct choice.')
'''search data from the tables based on the choices'''
def search_data(choices):
    if choices == '1':
        dataManagement.search_events_data()
    elif choices == '2':
        dataManagement.search_items_data()
    elif choices == '3':
        dataManagement.search_sales_data()
    else:
        ui.message('Please enter the correct choice.')
'''query data to tables based on the choices'''
def query_data(choices):
    if choices == '1':
        dataManagement.total_items_sold()
    elif choices == '2':
        dataManagement.maximum_items_sold()
    elif choices == '3':
        dataManagement.minimum_items_sold()
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
