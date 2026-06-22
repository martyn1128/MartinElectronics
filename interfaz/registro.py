from interfaz.registrod.registrod_ui import Ui_Dialog
from PySide6.QtWidgets import QLineEdit, QDialog, QMessageBox
from PySide6.QtCore import Signal
import sqlite3

from models.usarios import UsuariosModel


class Registrar(QDialog):
    cambio_vent = Signal()
    def __init__(self):
        super().__init__()
        self.registro = Ui_Dialog()
        self.registro.setupUi(self)
        self.registro.checkvercont.stateChanged.connect(self.ver_cont)
        self.registro.btnregistrarse.clicked.connect(self.hacer_reg)
        self.registro.cont.editingFinished.connect(lambda: self.registro.checkvercont.setChecked(False))
        self.registro.btncancelar.clicked.connect(self.cambio_vent.emit)

    def ver_cont(self):
        if self.registro.checkvercont.isChecked():
            self.registro.cont.setEchoMode(QLineEdit.EchoMode.Normal)
            self.registro.cont_2.setEchoMode(QLineEdit.EchoMode.Normal)
        else:
            self.registro.cont.setEchoMode(QLineEdit.EchoMode.Password)
            self.registro.cont_2.setEchoMode(QLineEdit.EchoMode.Password)

    def hacer_reg(s):
        nombre = s.registro.nombre.text()
        if nombre:
            usuario = s.registro.usuario.text()
            if usuario:
                cont = s.registro.cont.text()
                if cont:
                    sex = s.registro.sexo.currentText()
                    email = s.registro.email.text()
                    fn = s.registro.fechna.date().toString("dd/MM/yyyy")
                    tipo = s.registro.tipo.currentText()
                    if cont == s.registro.cont_2.text():
                        datos = nombre, usuario, sex, email, fn, cont, tipo
                        UsuariosModel().nuevo(datos)
                        QMessageBox.information(s, "Éxito", "Usuario creado correctamente")
                        s.cambio_vent.emit()
                    else:
                        s.registro.mensaje.setText('       Las contraseñas no coinsiden...')
                else:
                    s.registro.mensaje.setText('       Ingrese una contraseña')
            else:
                s.registro.mensaje.setText('       Ingrese un usuario')
        else:
            s.registro.mensaje.setText('       Ingrese su nombre')