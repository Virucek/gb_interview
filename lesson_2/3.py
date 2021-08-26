"""
3. Реализовать возможность переустановки значения цены товара. Необходимо, чтобы и родительский, и дочерний классы
получили новое значение цены. Следует проверить это, вызвав соответствующий метод родительского класса и функцию
дочернего (функция, отвечающая за отображение информации о товаре в одной строке).
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


class ItemDiscountReport(ItemDiscount):

    def get_parent_data(self):
        return f'{self.get_name} - {self.get_price} руб.'


test_child = ItemDiscountReport('диван', 10000)
test_child.set_price(20000)
print(f'child class new price - {test_child.get_parent_data()}')

test_parent = ItemDiscount('диван', 10000)
test_parent.set_price(17000)
print(f'parent class new price - {test_parent.get_price} руб.')
