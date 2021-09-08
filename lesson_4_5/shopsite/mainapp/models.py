from django.db import models


class Goods(models.Model):
    name = models.CharField(verbose_name='Название товара', max_length=64)
    receipt_date = models.DateField(verbose_name='Дата поступления')
    price = models.FloatField(verbose_name='Цена товара')
    unit = models.CharField(verbose_name='Единица измерения', max_length=16)
    supplier_name = models.CharField(verbose_name='Имя поставщика', max_length=64)


