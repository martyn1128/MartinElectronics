import os

from PySide6.QtSql import QSqlDatabase, QSqlQuery


class QtDB:
    def __init__(self):
        self.db = None
        self.db_path = os.path.join(os.getenv('APPDATA'), 'Martin Electronics/data/me.db')

    def conecta(self):
        self.db = QSqlDatabase.addDatabase('QSQLITE')
        self.db.setDatabaseName(self.db_path)
        self.db.open()
        return self.db

    def desconecta(self):
        if self.db:
            self.db.close()

