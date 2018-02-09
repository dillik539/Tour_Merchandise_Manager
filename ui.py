'''display menu of choices'''
def get_menu_choices():
    print('''
    1. Enter data
    2. Show total items sold
    3. Update data
    4. Search data
    5. Delete data
    6. Save data
    q. Quit
    ''')
    return input('Enter choice: ')
