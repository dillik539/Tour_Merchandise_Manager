'''display menu of choices'''
def get_menu_choices():
    message('''
    1. Enter data
    2. Display data
    3. Delete data
    4. Drop tables
    5. Search data
    6. Update data
    7. Query data
    q. Quit
    ''')
    return input('Enter choice: ')

'''display choices to enter data to tables'''
def get_enter_choices():
    message('''
    1. Enter data to Events table
    2. Enter data to Items table
    3. Enter data to Sales table
    ''')
    return input('Enter choice: ')

'''display choices to display data from tables'''
def get_display_choices():
    print('''
    1. Show Events data
    2. Show Items data
    3. Show Sales data
    ''')
    return input('Enter display choice: ')

'''display choices to delete data from tables'''
def get_delete_choices():
    message('''
    1. Delete Events data
    2. Delete Items data
    3. Delete Sales data
    ''')
    return input('Enter delete choice: ')

'''display choices to drop tables'''
def get_drop_table_choices():
    message('''
    1. Drop Events table
    2. Drop Items table
    3. Drop Sales table
    ''')
    return input('Enter choice to drop desired table: ')

'''display choices to search data from tables'''
def get_search_data_choices():
    message('''
    1. Search data from events
    2. Search data from items
    3. Search data from sales
    ''')
    return input('Enter choice to search data from desired table: ')

'''display choices to update data of tables'''
def get_update_data_choices():
    message('''
    1. Update events table
    2. Update items table
    3. Update sales table
    ''')
    return input('Enter choice to update desired table: ')

'''display choices to query data from tables'''
def get_query_choices():
    message('''
    1. Total items sold
    2. Maximum items sold
    3. Minimum items sold
    ''')
    return input('Enter choice to query data: ')

def input_event():
    return input('Enter venue name: ')

def input_item():
    input_items = []
    item_name = input('Enter the item name: ')
    event_id = int(input('Enter the event id : '))
    input_items.append(event_id)
    input_items.append(item_name)
    return input_items

def input_sale():
    input_sales = []
    item_price = input('Enter the item price: ')
    item_id = int(input('Enter the item id: '))
    no_of_items = int(input('Enter the number of items: '))
    input_sales.append(item_id)
    input_sales.append(item_price)
    input_sales.append(no_of_items)
    return input_sales

def message(msg):
    print (msg)
