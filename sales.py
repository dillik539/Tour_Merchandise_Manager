class Sales:
    def __init__(self,sales_id,item_id, sold_qty):
        self.__sales_id = sales_id
        self.__item_id = item_id
        self.__sold_qty = sold_qty


    def set_sales_id(self, sales_id):
        self.__sales_id = sales_id


    def set_item_id(self, item_id):
        self.__item_id = item_id


    def set_sold_qty(self,sold_qty):
        self.__sold_qty = sold_qty


    def get_sales_id(self):
        return self.__sales_id

    def get_item_id(self):
        return self.__item_id


    def get_sold_qty(self):
        return self.__sold_qty
