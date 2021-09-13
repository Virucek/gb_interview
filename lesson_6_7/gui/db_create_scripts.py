from PyQt5 import QtSql


def categories_db_create():
    query = QtSql.QSqlQuery()
    query.exec('''CREATE TABLE IF NOT EXISTS categories (
                           category_name TEXT PRIMARY KEY,
                           category_description TEXT NOT NULL ) 
                ''')


def units_db_create():
    query = QtSql.QSqlQuery()
    query.exec('''CREATE TABLE IF NOT EXISTS units (
                       unit TEXT PRIMARY KEY )
                ''')


def positions_db_create():
    query = QtSql.QSqlQuery()
    query.exec('''CREATE TABLE IF NOT EXISTS positions (
                       position TEXT PRIMARY KEY ) 
                ''')


def goods_db_create():
    query = QtSql.QSqlQuery()
    query.exec('''CREATE TABLE IF NOT EXISTS goods (
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


def employees_db_create():
    query = QtSql.QSqlQuery()
    query.exec('''CREATE TABLE IF NOT EXISTS employees (
                       employee_id INTEGER PRIMARY KEY,
                       employee_fio TEXT,
                       employee_position TEXT,
                       FOREIGN KEY (employee_position)
                          REFERENCES positions (position)
                             ON DELETE CASCADE
                             ON UPDATE CASCADE )
                   ''')


def vendors_db_create():
    query = QtSql.QSqlQuery()
    query.exec('''CREATE TABLE IF NOT EXISTS vendors (
                       vendor_id INTEGER PRIMARY KEY,
                       vendor_name TEXT,
                       vendor_ownerchipform TEXT,
                       vendor_address TEXT,
                       vendor_phone TEXT,
                       vendor_email TEXT )
                   ''')


def create_table_factory(table):
    tables_scripts = {
        'categories': categories_db_create,
        'units': units_db_create,
        'positions': positions_db_create,
        'goods': goods_db_create,
        'employees': employees_db_create,
        'vendors': vendors_db_create,
    }
    try:
        tables_scripts[table]()
    except KeyError:
        print(f'Обработчика для таблицы {table} нет!')

