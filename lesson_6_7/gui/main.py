import os
import sys

from PyQt5 import uic, QtSql
from PyQt5.QtSql import QSqlTableModel
from PyQt5.QtWidgets import QWidget, qApp, QApplication, QMainWindow, QFileDialog, QDialog

from signals import categories_click, units_click, positions_click, goods_click, employees_click, vendors_click
from ui import mainform


# todo: Добавить обработчики добавления и удаления записей из таблиц, обновление таблиц
class Window(QMainWindow):
    def __init__(self, parent=None):
        QMainWindow.__init__(self, parent)
        # uic.loadUi(os.path.join('ui', 'main.ui'), self)
        # self.btnExit.clicked.connect(qApp.quit)
        self.ui = mainform.Ui_MainWindow()
        self.ui.setupUi(self)

        conn = QtSql.QSqlDatabase.addDatabase('QSQLITE')

        def open_file_db_diag_window():
            diag = QFileDialog(self.ui.frame)
            file = diag.getSaveFileName(self.ui.frame, filter="Sqlite Files (*.sqlite);")
            self.ui.db_path.clear()
            fileName = file[0]
            self.ui.db_path.setText(fileName)
            if fileName:
                conn.setDatabaseName(fileName)
                activate_conn()
            else:
                deactivate_conn()

        self.ui.selectDb.clicked.connect(open_file_db_diag_window)

        def activate_conn():
            self.ui.categories.setEnabled(True)
            self.ui.categories.triggered.connect(lambda: categories_click(self))
            self.ui.units.setEnabled(True)
            self.ui.units.triggered.connect(lambda: units_click(self))
            self.ui.positions.setEnabled(True)
            self.ui.positions.triggered.connect(lambda: positions_click(self))
            self.ui.goods.setEnabled(True)
            self.ui.goods.triggered.connect(lambda: goods_click(self))
            self.ui.employees.setEnabled(True)
            self.ui.employees.triggered.connect(lambda: employees_click(self))
            self.ui.vendors.setEnabled(True)
            self.ui.vendors.triggered.connect(lambda: vendors_click(self))

        def deactivate_conn():
            self.ui.categories.setEnabled(False)
            self.ui.units.setEnabled(False)
            self.ui.positions.setEnabled(False)
            self.ui.goods.setEnabled(False)
            self.ui.employees.setEnabled(False)
            self.ui.vendors.setEnabled(False)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    win = Window()
    win.show()
    sys.exit(app.exec_())
