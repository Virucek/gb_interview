"""
3. Создать два списка с различным количеством элементов. В первом должны быть записаны ключи, во втором —
значения. Необходимо написать функцию, создающую из данных ключей и значений словарь. Если ключу не хватает значения,
в словаре для него должно сохраняться значение None. Значения, которым не хватило ключей, необходимо отбросить.
"""
import itertools


def create_dict_v1(keys, values):
    # вариант 1 через itertools
    return {key: value for key, value in itertools.zip_longest(keys, values) if key is not None}


def create_dict_v2(keys, values):
    # вариант 2 без itertools
    res_dict = {key: None for key in keys}
    for k, v in zip(res_dict.keys(), values):
        res_dict[k] = v
    return res_dict


keys_list = ['Bed', 'Chair', 'Table', 'Sofa']
values_list = [14000, 2500.10, 5600.0]

print('VARIANT 1')
print(create_dict_v1(keys_list, values_list))  # 4 keys, last is None
print(create_dict_v1(values_list, keys_list))  # 3 keys
print('VARIANT 2')
print(create_dict_v2(keys_list, values_list))  # 4 keys, last is None
print(create_dict_v2(values_list, keys_list))  # 3 keys
