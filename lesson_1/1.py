"""
1. Написать функцию, реализующую вывод таблицы умножения размерностью AｘB. Первый и второй множитель должны
задаваться в виде аргументов функции. Значения каждой строки таблицы должны быть представлены списком,
который формируется в цикле. После этого осуществляется вызов внешней lambda-функции, которая формирует на основе
списка строку. Полученная строка выводится в главной функции. Элементы строки (элементы таблицы умножения) должны
разделяться табуляцией.
"""

# Решение БЕЗ lambda-функции


def print_table(a, b):
    for i in range(1, a + 1):
        row = []
        for j in range(1, b + 1):
            row.append(i * j)
        print('\t'.join([str(k) for k in row]))


print_table(3, 5)

print('\n' + '===================' + '\n')
# Решение С внешней lambda-функцией (PEP-8: E731 не рекомендует)

f = lambda row: '\t'.join([str(k) for k in row])


def print_table(a, b):
    for i in range(1, a + 1):
        row = []
        for j in range(1, b + 1):
            row.append(i * j)
        print(f(row))


print_table(3, 5)
