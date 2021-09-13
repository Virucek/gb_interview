import sqlite3

db_path = 'lesson6.sqlite'


# Создание схемы базы данных
def create_db(conn_):

    cursor = conn_.cursor()
    # Вспомогательные таблицы
    cursor.execute('''CREATE TABLE IF NOT EXISTS categories (
                       category_name TEXT PRIMARY KEY,
                       category_description TEXT NOT NULL ) 
                   ''')

    cursor.execute('''CREATE TABLE IF NOT EXISTS units (
                       unit TEXT PRIMARY KEY )
                   ''')

    cursor.execute('''CREATE TABLE IF NOT EXISTS positions (
                       position TEXT PRIMARY KEY ) 
                   ''')

    # Основные таблицы

    cursor.execute('''CREATE TABLE IF NOT EXISTS goods (
                       good_id INTEGER PRIMARY KEY,
                       good_name TEXT,
                       good_unit TEXT,
                       good_cat TEXT,
                       FOREIGN KEY (good_unit)
                          REFERENCES units (unit)
                             ON DELETE CASCADE
                             ON UPDATE CASCADE,
                       FOREIGN KEY (good_cat)
                          REFERENCES categories (category_name)
                             ON DELETE CASCADE
                             ON UPDATE CASCADE ) 
                   ''')

    cursor.execute('''CREATE TABLE IF NOT EXISTS employees (
                       employee_id INTEGER PRIMARY KEY,
                       employee_fio TEXT,
                       employee_position TEXT,
                       FOREIGN KEY (employee_position)
                          REFERENCES positions (position)
                             ON DELETE CASCADE
                             ON UPDATE CASCADE )
                   ''')

    cursor.execute('''CREATE TABLE IF NOT EXISTS vendors (
                       vendor_id INTEGER PRIMARY KEY,
                       vendor_name TEXT,
                       vendor_ownerchipform TEXT,
                       vendor_address TEXT,
                       vendor_phone TEXT,
                       vendor_email TEXT )
                   ''')


# Проверка таблиц
def test_db(conn_):
    prepare_db(conn_)
    cursor = conn_.cursor()
    cursor.execute('INSERT INTO categories (category_name, category_description) VALUES ("cat_test", "cat_test")')
    cursor.execute('INSERT INTO units (unit) VALUES ("unit_test")')
    cursor.execute('INSERT INTO positions (position) VALUES ("position_test")')
    cursor.execute('INSERT INTO goods (good_id, good_unit, good_cat) VALUES (1, "unit_test", "cat_test")')
    cursor.execute('INSERT INTO employees (employee_id, employee_position) VALUES (1, "position_test")')
    cursor.execute('INSERT INTO vendors (vendor_id, vendor_name) VALUES (1, "vendor_test")')
    conn_.commit()
    test_fetch(conn_)


# Подготовка схемы - удаление всех записей из всех таблиц
def prepare_db(conn_):
    cursor = conn_.cursor()
    tables = cursor.execute('SELECT name FROM sqlite_master WHERE type="table"')
    for table in tables.fetchall():
        cursor.execute(f'DELETE FROM {table[0]}')
        conn_.commit()


# Проверка, что записи появились
def test_fetch(conn_):
    cursor = conn_.cursor()
    tables = cursor.execute('SELECT name FROM sqlite_master WHERE type="table"')
    for table in tables.fetchall():
        res = cursor.execute(f'SELECT COUNT(*) FROM {table[0]}')
        assert res.fetchone()[0] == 1, f'{table[0]} number of record is wrong!'
    print('DB tested successfully!')


if __name__ == '__main__':
    conn = sqlite3.connect(db_path)
    with conn:
        create_db(conn)
        test_db(conn)


def create_db_connection(db_path_):
    conn_ = sqlite3.connect(db_path_)
    create_db(conn_)
    return conn_
