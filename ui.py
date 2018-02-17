'''display menu of choices'''
def get_menu_choices():
    print('''
    1. Enter data
    2. Display data
    3. Delete data
    6. Drop tables
    7. Search data
    8. Update data
    9. Save data
    q. Quit
    ''')
    return input('Enter choice: ')

def get_enter_choices():
    print('''
    1. Enter data to Events table
    2. Enter data to Items table
    3. Enter data to Sales table
    ''')
    return input('Enter choice: ')

def get_display_choices():
    print('''
    1. Show Events data
    2. Show Items data
    3. Show Sales data
    ''')
    return input('Enter display choice: ')

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
