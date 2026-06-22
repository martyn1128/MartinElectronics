from PySide6.QtWidgets import QMainWindow, QMessageBox

from controllers.reparaciones_controller import ReparacionesController
from controllers.registros_controller import RegistrosController
from controllers.clientes_controller import ClientesController
from controllers.entregas_controller import EntregasController
from controllers.config_controller import ConfigController
from controllers.inicio_controller import InicioController
from controllers.menu_controller import MenuController
from controllers.pago_controller import PagoController
from interfaz.principal.principal_ui import Ui_MainWindow
from models.qt_db import QtDB


# noinspection SpellCheckingInspection
class MainController(QMainWindow):
    def __init__(self, user):
        super().__init__()
        self.cambioreg = False
        self.cambiorep = False
        self.cambioent = False
        self.cambioemp = False
        self.db = QtDB()
        self.conexion = None
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.user = user
        self.registros = RegistrosController(self)
        self.clientescontroller = ClientesController(self)
        self.reparaciones = ReparacionesController(self)
        self.entregascontroller = EntregasController(self)
        self.iniciocontroller = InicioController(self)
        self.pagocontroller = PagoController(self)
        self.configcontroller = ConfigController(self)
        self.menucontroller = MenuController(self)

    def closeEvent(self, event):
        self.comprueba_cambio()
        respuesta = QMessageBox.question(
            self,
            'Cerrar Aplicación',
            "¿Estás seguro de que quieres salir?",
            QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No,
            QMessageBox.StandardButton.No
        )

        if respuesta == QMessageBox.StandardButton.Yes:
            event.accept()  # Permite que la ventana se cierre
        else:
            event.ignore()  # Evita que la ventana se cierre

    def conecta(self):
        self.db = QtDB()
        self.conexion = self.db.conecta()

    def desconecta(self):
        if self.db:
            self.db.desconecta()
            self.db = None
            self.conexion = None
        else:
            pass

    def cambio_en_reg(self):
        self.cambioreg = True

    def cambio_en_rep(self):
        self.cambiorep = True

    def cambio_en_ent(self):
        self.cambioent = True

    def cambio_en_emp(self):
        self.cambioemp = True

    def comprueba_cambio(self):
        if self.cambioreg:
            save = QMessageBox.question(self, "Martin Electronics's", "Desea guardar los cambios en Registros?")
            if save == QMessageBox.StandardButton.Yes:
                self.registros.guardar()
            self.cambioreg = False
        elif self.cambiorep:
            save = QMessageBox.question(self, "Martin Electronics's", "Desea guardar los cambios en Reparaciones?")
            if save == QMessageBox.StandardButton.Yes:
                self.reparaciones.confirma_rep()
            self.cambiorep = False
        elif self.cambioent:
            save = QMessageBox.question(self, "Martin Electronics's", "Desea guardar los cambios en Entregas?")
            if save == QMessageBox.StandardButton.Yes:
                self.entregascontroller.guardar()
                self.entregascontroller.eimprimir()
            self.cambioent = False
        elif self.cambioemp:
            save = QMessageBox.question(self, "Martin Electronics's", "Desea guardar los cambios en Empresa?")
            if save == QMessageBox.StandardButton.Yes:
                self.configcontroller.guardar()
            self.cambioemp = False