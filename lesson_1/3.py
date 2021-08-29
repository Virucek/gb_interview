"""
3. Разработать генератор случайных чисел. В функцию передавать начальное и конечное число генерации (нуль
необходимо исключить). Заполнить этими данными список и словарь. Ключи словаря должны создаваться по шаблону:
“elem_<номер_элемента>”. Вывести содержимое созданных списка и словаря.
"""
import random


def gen_rand(start, stop):
    res_list = []
    res_dict = {}
    # Проверка входных данных
    if start > stop:
        print('Конечное число генерации должно быть больше начального!')
        return None
    elif stop == 0:
        print('Конечное число генерации не должно быть нулем!')
        return None

    for n in range(10):
        # Приведение генерируемых чисел к int для красоты
        el = int((stop - start) * random.random() + start)
        res_list.append(el)
        res_dict[f'elem_{n}'] = el

    return res_list, res_dict


print(gen_rand(5, 18))
