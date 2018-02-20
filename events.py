'''this class holds the events information'''
class Events:
    def __init__(self, event_id, event_date, venue):
        self.__event_id = event_id
        self.__event_date = event_date
        self.__venue = venue



    def set_event_id(self, event_id):
        self.__event_id = event_id

    def set_event_date(self,event_date):
        self.__event_date = event_date

    def set_venue(self,venue):
        self.__venue = venue

    def get_event_id(self):
        return self.__event_id

    def get_event_date(self):
        return self.__event_date

    def get_venue(self):
        return self.__venue
