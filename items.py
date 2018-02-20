'''this class holds the items information'''
class Items:
    def __init__(self, item_id, event_id, name):
        self.__item_id = item_id
        self.__event_id = event_id
        self.__name = name


    def set_item_id(self, item_id):
        self.__item_id = item_id

    def set_event_id(self, event_id):
        self.__event_id = event_id

    def set_name(self, name):
        self.__name = name

    def get_item_id(self):
        return self.__item_id

    def get_event_id(self):
        return self.__event_id

    def get_name(self):
        return self.__name
