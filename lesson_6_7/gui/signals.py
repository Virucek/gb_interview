from PyQt5.QtSql import QSqlTableModel

from db_create_scripts import create_table_factory


def set_table_model(table, window):
    create_table_factory(table)
    model = QSqlTableModel()
    model.setTable(table)
    model.select()
    window.ui.tableView.setModel(model)


def categories_click(window):
    table = 'categories'
    set_table_model(table, window)


def units_click(window):
    table = 'units'
    set_table_model(table, window)


def positions_click(window):
    table = 'positions'
    set_table_model(table, window)


def goods_click(window):
    table = 'goods'
    set_table_model(table, window)


def employees_click(window):
    table = 'employees'
    set_table_model(table, window)


def vendors_click(window):
    table = 'vendors'
    set_table_model(table, window)
