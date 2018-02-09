class Items:
    def __init__(self, item_id, event_id, name, price, quantity):
        self.__item_id = item_id
        self.__event_id = event_id
        self.__name = name
        self.__price = price
        self.__quantity = quantity


    def set_item_id(self, item_id):
        self.__item_id = item_id

    def set_event_id(self, event_id):
        self.__event_id = event_id

    def set_name(self, name):
        self.__name = name

    def set_price(self, price):
        self.__price = price

    def set_quantity(self, quantity):
        self.__quantity = quantity

    def get_item_id(self):
        return self.__item_id

    def get_event_id(self):
        return self.__event_id

    def get_name(self):
        return self.__name

    def get_price(self):
        return self.__price

    def get_quantity(self):
        return self.__quantity
