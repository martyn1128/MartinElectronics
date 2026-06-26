from interfaz.inicio.inicio_ui import Ui_MainWindow
from PySide6.QtCore import Signal
from PySide6.QtWidgets import QLineEdit, QMainWindow
import pickle

from models.usarios import UsuariosModel


class Inicia_secion(QMainWindow):
    cambio_vent = Signal()
    reg = Signal()
    def __init__(self):
        #self.app = QtWidgets.QApplication([])
        super().__init__()
        self.user = ''
        self.inicio = Ui_MainWindow()
        self.inicio.setupUi(self)
        # Botones de inicio
        self._conectareventos()

    def _conectareventos(self):
        self.inicio.checkvercont.stateChanged.connect(self.ver_cont)
        self.inicio.btniniciar.clicked.connect(self.loguin)
        self.inicio.btnregistrarse.clicked.connect(self.reg.emit)
        self.inicio.usuario.returnPressed.connect(self.inicio.cont.setFocus)
        self.inicio.usuario.textChanged.connect(self.valida_usuario)
        self.inicio.cont.editingFinished.connect(lambda: self.inicio.checkvercont.setChecked(False))
        self.inicio.cont.returnPressed.connect(self.inicio.btniniciar.click)


        #self.inicio.show()
        #self.app.exec()


    def loguin(self):
        self.inicio.checkvercont.setChecked(False)
        usuario = self.inicio.usuario.text()
        contraseña = self.inicio.cont.text()
        if usuario and contraseña:
            cont = UsuariosModel().autenticacion(usuario)
            if cont and cont[0] == contraseña:
                self.inicio.mensaje.setText("   Acceso aprobado")
                self.user = (cont[2],cont[1])
                self.cambio_vent.emit()
            else :
                if " " in self.inicio.usuario.text():
                    self.inicio.mensaje.setText("El ususario no puede tener espacios")
                    self.inicio.mensaje.setStyleSheet("color: rgb(255, 255, 0);")
                else:
                    self.inicio.mensaje.setText("  Usuario o contraseña incorrecta")
                    self.inicio.mensaje.setStyleSheet("")
        else:
            if usuario:
                self.inicio.cont.setFocus()
            else:
                self.inicio.usuario.setFocus()
            self.inicio.mensaje.setText("Por favor complete todos los campos")

    def get_acceso(self, user, cont):
        try:
            with open("users.lm", 'rb') as us:
                try:
                    while True:
                        usuario = pickle.load(us)
                        if usuario.get_user() == user and usuario.get_cont() == cont:
                            return True
                except EOFError:
                    self.inicio.mensaje.setText("  Usuario o contraseña incorrecto")
                    return False
        except FileNotFoundError:
            self.inicio.mensaje.setText('     No hay usuarios registrados')

    def ver_cont(s):
        if s.inicio.checkvercont.isChecked():
            s.inicio.cont.setEchoMode(QLineEdit.EchoMode.Normal)
        else:
            s.inicio.cont.setEchoMode(QLineEdit.EchoMode.Password)

    def valida_usuario(self):
        if " " in self.inicio.usuario.text():
            self.inicio.mensaje.setText("El ususario no puede tener espacios")
            self.inicio.mensaje.setStyleSheet("color: rgb(255, 255, 0);")
        else:
            self.inicio.mensaje.setText("")
            self.inicio.mensaje.setStyleSheet("")