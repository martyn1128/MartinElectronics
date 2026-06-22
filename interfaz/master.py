from interfaz.masterc.masterd_ui import Ui_Dialog
from PySide6.QtWidgets import QLineEdit, QDialog
from PySide6.QtCore import Signal
import sqlite3, bcrypt

from models.master import MasterController


class Master(QDialog):
    cambio_vent = Signal()
    cierra = Signal()

    def __init__(self):
        super().__init__()
        self.master = Ui_Dialog()
        self.master.setupUi(self)
        # Botones masterc
        self.master.btnsig.clicked.connect(self.accesom)
        self.master.checkvercont.stateChanged.connect(self.ver_contm)

    def ver_contm(self):
        if self.master.checkvercont.isChecked():
            self.master.cont.setEchoMode(QLineEdit.EchoMode.Normal)
        else:
            self.master.cont.setEchoMode(QLineEdit.EchoMode.Password)

    def accesom(self):
        cont = self.master.cont.text().encode("utf-8")
        mast = MasterController().accesom()
        if bcrypt.checkpw(cont, mast[0].encode('utf-8')):
            self.cambio_vent.emit()
        elif cont:
            self.master.mensaje.setText('   Contraseña incorrecta')
            self.master.cont.setFocus()
        else:
            self.master.mensaje.setText('   Complete el campo')
            self.master.cont.setFocus()