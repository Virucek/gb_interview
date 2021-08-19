"""
2. Дополнить следующую функцию недостающим кодом:
def print_directory_contents(sPath):

Функция принимает имя каталога и распечатывает его содержимое
в виде «путь и имя файла», а также любые другие
файлы во вложенных каталогах.

Эта функция подобна os.walk. Использовать функцию os.walk
нельзя. Данная задача показывает ваше умение работать с
вложенными структурами.
"""
import os


def print_directory_contents(sPath):
    files = []

    for el in os.listdir(sPath):
        full_path = os.path.join(os.path.abspath(sPath), el)
        if os.path.isfile(full_path):
            files.append(full_path)
        else:
            print_directory_contents(full_path)
    print(files)


print_directory_contents('test')