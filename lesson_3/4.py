"""
4. Написать программу, в которой реализовать две функции. В первой должен создаваться простой текстовый файл. Если
файл с таким именем уже существует, выводим соответствующее сообщение. Необходимо открыть файл и подготовить два
списка: с текстовой и числовой информацией. Для создания списков использовать генераторы. Применить к спискам функцию
zip(). Результат выполнения этой функции должен должен быть обработан и записан в файл таким образом, чтобы каждая
строка файла содержала текстовое и числовое значение. Вызвать вторую функцию. В нее должна передаваться ссылка на
созданный файл. Во второй функции необходимо реализовать открытие файла и простой построчный вывод содержимого. Вся
программа должна запускаться по вызову первой функции.
"""
import random

STRING_LENGTH = 15
LINES_COUNT = 10


def get_random_string():
    return ''.join([chr(random.randint(ord('a'), ord('z'))) for _ in range(STRING_LENGTH)])


def create_file():
    # Т.к. вся программа должна запускаться по вызову функции, определяем input внутри функции (имхо, не очень решение)
    name = input('Введите имя файла: ')
    if not name:
        print('Имя файла не указано!')
    else:
        try:
            with open(name, 'x') as f:
                text_data = (get_random_string() for _ in range(LINES_COUNT))
                num_data = (random.randint(10000, 9999999) for _ in range(LINES_COUNT))
                for text, num in zip(text_data, num_data):
                    f.write(f'{text} {num}\n')
                return f
            #     file = f
            # read_file(file)
            # Непонятно, если программа должна запускаться по первой функции, то и вторую надо
            # вызывать в первой?
        except FileExistsError:
            print('Файл с таким именем уже существует!')


def read_file(file):
    with open(file.name, 'r', encoding='utf-8') as f:
        for line in f:
            print(line)


if __name__ == '__main__':
    file = create_file()
    if file:
        read_file(file)

