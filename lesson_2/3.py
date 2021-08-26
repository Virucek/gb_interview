"""
3. Реализовать возможность переустановки значения цены товара. Необходимо, чтобы и родительский, и дочерний классы
получили новое значение цены. Следует проверить это, вызвав соответствующий метод родительского класса и функцию
дочернего (функция, отвечающая за отображение информации о товаре в одной строке).
"""


class ItemDiscount:

    def __init__(self, name, price):
        self.__name = name
        self.__price = price

    def get_price(self):
        return self.__price

    def get_name(self):
        return self.__name

    def set_price(self, val):
        self.__price = val


class ItemDiscountReport(ItemDiscount):

    def get_parent_data(self):
        return f'{self.get_name()} - {self.get_price()} руб.'


test = ItemDiscountReport('диван', 10000)
print(test.get_parent_data())
test.set_price(20000)
print(test.get_parent_data())
