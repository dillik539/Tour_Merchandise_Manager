'''display menu of choices'''
def get_menu_choices():
    print('''
    1. Enter data to Events table
    2. Enter data to Items table
    3. Enter data to sales table
    4. Show total items sold
    5. Update data
    6. Search data
    7. Delete data
    8. Save data
    q. Quit
    ''')
    return input('Enter choice: ')

def input_event():
    return input('Enter venue name: ')

def input_item():
    input_items = []
    item_name = input('Enter the item name: ')
    event_id = int(input('Enter the event id : '))
    item_price = input('Enter the item price: ')
    no_of_items = int(input('Enter the number of items: '))
    input_items.append(event_id)
    input_items.append(item_name)
    input_items.append(item_price)
    input_items.append(no_of_items)
    return input_items

def message(msg):
    print (msg)
