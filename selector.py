import os

from controllers.inisec_controller import Inicia_secion
from controllers.main_controller import MainController
from interfaz.master import Master
from interfaz.registro import Registrar
from controllers.uno_controller import Uno

class Seleccion:

    def __init__(self):
        self.inisec = None
        self.master = None
        self.creamaster = None
        self.registro = None
        self.vpinc = None

    def inicio(self):
        a = None
        try:
            with open(os.path.join(os.getenv('APPDATA'),'Martin Electronics/data/me.db'), 'rb'):
                a = True
        except FileNotFoundError:
            self.mostrar_unomaster()
        if a:
            self.mostrar_inisec2()

    def mostrar_inisec2(self):
        self.inisec = Inicia_secion()
        self.inisec.cambio_vent.connect(self.mostrar_p_principal)
        self.inisec.reg.connect(self.mostrar_master)
        self.inisec.show()

    def mostrar_inisec(self):
        self.creamaster.hide()
        self.inisec = Inicia_secion()
        self.inisec.cambio_vent.connect(self.mostrar_p_principal)
        self.inisec.reg.connect(self.mostrar_master)
        self.inisec.show()

    def mostrar_master(self):
        self.master = Master()
        self.master.setModal(True)
        self.master.cambio_vent.connect(self.mostrar_registro)
        self.master.cierra.connect(lambda: self.inisec.setEnabled(True))
        self.master.show()

    def mostrar_unomaster(self):
        self.creamaster = Uno()
        self.creamaster.cambio_vent.connect(self.mostrar_inisec)
        self.creamaster.show()

    def mostrar_registro(self):
        self.master.hide()
        self.registro = Registrar()
        self.registro.registro.fechna.setCalendarPopup(True)
        self.registro.setModal(True)
        self.registro.cambio_vent.connect(self.registro.hide)
        self.registro.exec()

    def mostrar_p_principal(self):
        self.vpinc = MainController(self.inisec.user)
        self.inisec.hide()
        self.vpinc.showMaximized()