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
