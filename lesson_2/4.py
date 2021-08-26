"""
4. Реализовать расчет цены товара со скидкой. Величина скидки должна передаваться в качестве аргумента в дочерний
класс. Выполнить перегрузку методов конструктора дочернего класса (метод __init__, в который должна передаваться
переменная — скидка), и перегрузку метода __str__ дочернего класса. В этом методе должна пересчитываться цена и
возвращаться результат — цена товара со скидкой. Чтобы все работало корректно, не забудьте инициализировать дочерний
и родительский классы (вторая и третья строка после объявления дочернего класса).
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

    def __init__(self, name, price, discount):
        super().__init__(name, price)
        self.__discount = discount

    def __str__(self):
        return str(self.get_price - self.__discount)

    def get_parent_data(self):
        return f'{self.get_name} - {self.get_price} руб.'


test = ItemDiscountReport('диван', 10000, 2000)
print(test.get_parent_data())
print(f'Цена товара со скидкой: {test} руб.')
