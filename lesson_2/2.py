"""
2. Инкапсулировать оба параметра (название и цену) товара родительского класса. Убедиться, что при сохранении текущей
логики работы программы будет сгенерирована ошибка выполнения. Усовершенствовать родительский класс таким образом,
чтобы получить доступ к защищенным переменным. Результат выполнения заданий 1 и 2 должен быть идентичным.
"""


class ItemDiscount:

    def __init__(self, name, price):
        self.__name = name
        self.__price = price

    # Необходим, чтобы получить значение private атрибута price. Можно через property
    def get_price(self):
        return self.__price

    def get_name(self):
        return self.__name


class ItemDiscountReport(ItemDiscount):

    def get_parent_data(self):
        return f'{self.get_name()} - {self.get_price()} руб.'


test = ItemDiscountReport('диван', 10000)
print(test.get_parent_data())

