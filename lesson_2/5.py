"""
5. Проверить на практике возможности полиморфизма. Необходимо разделить дочерний класс ItemDiscountReport на два
класса. Инициализировать классы необязательно. Внутри каждого поместить функцию get_info, которая в первом классе
будет отвечать за вывод названия товара, а вторая — его цены. Далее реализовать выполнение каждой из функции тремя
способами.
"""


class ItemDiscount:

    def __init__(self, name, price):
        self.__name = name
        self.__price = price

    @property
    def get_price(self):
        return self.__price

    @property
    def get_name(self):
        return self.__name

    def set_price(self, val):
        self.__price = val


class ItemDiscountReportName(ItemDiscount):

    def get_info(self):
        print(self.get_name)


class ItemDiscountReportPrice(ItemDiscount):

    def get_info(self):
        print(self.get_price)


print('Option 1')
item_1 = ItemDiscountReportName('диван', 10000)
item_1.get_info()

item_2 = ItemDiscountReportPrice('стол', 3500)
item_2.get_info()

print('Option 2')


def show_info(obj):
    obj.get_info()


show_info(item_1)
show_info(item_2)

print('Option 3')
for i in [item_1, item_2]:
    i.get_info()
