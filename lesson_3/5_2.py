"""
5. Усовершенствовать первую функцию из предыдущего примера. Необходимо во втором списке часть строковых значений
заменить на значения типа example345 (строка+число). Далее — усовершенствовать вторую функцию из предыдущего примера
(функцию извлечения данных). Дополнительно реализовать поиск определенных подстрок в файле по следующим условиям:
вывод первого вхождения, вывод всех вхождений. Реализовать замену всех найденных подстрок на новое значение и вывод
всех подстрок, состоящих из букв и цифр и имеющих пробелы только в начале и конце — например, example345.

ВАРИАНТ 2 - С РАЗДЕЛЬНЫМИ ФУНКЦИЯМИ
"""
import random
import re

STRING_LENGTH = 15
LINES_COUNT = 10


def get_random_string():
    res_str = ''.join([chr(random.randint(ord('a'), ord('z'))) for _ in range(STRING_LENGTH)])
    rate = random.randint(0, 10)
    if rate > 6:  # Только для тестирования поиска подстроки! Гарантированно где-то будет 'test'
        pos = random.randint(0, 10)
        res_str = res_str[:pos] + 'test' + res_str[pos:]
    return res_str


def create_file():
    name = input('Введите имя файла: ')
    if not name:
        print('Имя файла не указано!')
    else:
        try:
            with open(name, 'x') as f:
                text_data = (get_random_string() for _ in range(LINES_COUNT))
                num_data = (random.randint(10000, 9999999) for _ in range(LINES_COUNT))
                for text, num in zip(text_data, num_data):
                    line = random.choice([f'{text}{num}\n', f'{text} {num}\n'])
                    f.write(line)
                return f
        except FileExistsError:
            print('Файл с таким именем уже существует!')


# Функция извлечения данных
def read_file(file):
    with open(file.name, 'r', encoding='utf-8') as f:
        lines = f.readlines()
        for line in lines:
            print(line)


# Функция поиска введенной подстроки
def find_substr(file, substr):
    print(f'----------Подстроки с {substr}------------')
    with open(file.name, 'r', encoding='utf-8') as f:
        lines = f.readlines()
        substr_flag = False
        for num, line in enumerate(lines):
            if substr in line:
                if not substr_flag:
                    print(f'Первое вхождение: {num + 1} - {line}')
                    print('Все вхождения: ')
                    substr_flag = True
                print(f'{num + 1}: {line}')
        if not substr_flag:
            print('Подстрок не найдено')


# Функция поиска подстроки с числами и строками и без пробелов (кроме тех, что в начале и конце)
def find_num_str(file):
    print('----------Подстроки с числами и строками------------')
    with open(file.name, 'r', encoding='utf-8') as f:
        lines = f.readlines()
        find_flag = False
        for num, line in enumerate(lines):
            find_ = re.search(r'[a-zA-Z]\d', line)
            if find_:
                find_flag = True
                print(f'{num + 1}: {line}')
        if not find_flag:
            print('Подстрок не найдено')


# Функция замены искомой подстроки на новую и записью в файл
def replace_substr(file, substr, new_substr):
    with open(file.name, 'r', encoding='utf-8') as f:
        lines = f.readlines()
    with open(file.name, 'w') as f:
        for idxline, line in enumerate(lines):
            ind = line.find(substr)
            if ind != -1:
                line = line[:ind] + line[ind+len(substr):]
                lines[idxline] = line[:ind] + new_substr + line[ind:]
        f.writelines(lines)


if __name__ == '__main__':
    file = create_file()
    if file:
        read_file(file)
        find_num_str(file)
        substr = input('Введите подстроку для поиска. Для тестирования попробуйте test: ')  # Для теста введите test
        if substr:
            find_substr(file, substr)
            new_substr = input('Введите новую подстроку для замены: ')
            if new_substr:
                replace_substr(file, substr, new_substr)
                read_file(file)
    print('Программа завершила работу')


