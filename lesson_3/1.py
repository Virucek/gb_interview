"""
1. Написать программу, которая будет содержать функцию для получения имени файла из полного пути до него. При вызове
функции в качестве аргумента должно передаваться имя файла с расширением. В функции необходимо реализовать поиск
полного пути по имени файла, а затем «выделение» из этого пути имени файла (без расширения).
"""
import os


def get_filename(full_name):
    if len(full_name.split('.')) > 1:
        if os.path.isfile(full_name):
            full_path = os.path.abspath(full_name)
            print(f"full path: {full_path};\nfile name: {os.path.split(full_path)[-1].split('.')[0]}")
        else:
            print('File doesn\'t exist')
    else:
        print('File without extension!')


get_filename('test.txt')
