from models.qt_db import QtDB


class MenuController:
    def __init__(self, view):
        self.cvprin = view
        self.vprin = self.cvprin.ui
        self._conectareventos()

    def _conectareventos(self):
        # --MENU---------------------------------------------------------------------------------------------------------
        self.vprin.btninicio.clicked.connect(self.cvprin.comprueba_cambio)
        self.vprin.btninicio.clicked.connect(self.cvprin.desconecta)
        self.vprin.btninicio.clicked.connect(self.cvprin.iniciocontroller.iniciom)
        self.vprin.btnregistros.clicked.connect(self.cvprin.comprueba_cambio)
        self.vprin.btnregistros.clicked.connect(self.cvprin.desconecta)
        self.vprin.btnregistros.clicked.connect(self.cvprin.registros.registros)
        self.vprin.btnreparaciones.clicked.connect(self.cvprin.comprueba_cambio)
        self.vprin.btnreparaciones.clicked.connect(self.cvprin.desconecta)
        self.vprin.btnreparaciones.clicked.connect(self.cvprin.reparaciones.reparacion)
        self.vprin.btnentregas.clicked.connect(self.cvprin.comprueba_cambio)
        self.vprin.btnentregas.clicked.connect(self.cvprin.desconecta)
        self.vprin.btnentregas.clicked.connect(self.cvprin.entregascontroller.entrega)
        self.vprin.btnclientes.clicked.connect(self.cvprin.comprueba_cambio)
        self.vprin.btnclientes.clicked.connect(self.cvprin.desconecta)
        self.vprin.btnclientes.clicked.connect(self.cvprin.clientescontroller.clientes)
        self.vprin.btnpago.clicked.connect(self.cvprin.comprueba_cambio)
        self.vprin.btnpago.clicked.connect(self.cvprin.desconecta)
        self.vprin.btnpago.clicked.connect(self.cvprin.pagocontroller.pago)
        self.vprin.btnconfig.clicked.connect(self.cvprin.comprueba_cambio)
        self.vprin.btnconfig.clicked.connect(self.cvprin.desconecta)
        self.vprin.btnconfig.clicked.connect(self.cvprin.configcontroller.config)
        self.vprin.btnmenu.clicked.connect(self.menum)
        self.vprin.btnclientes.click()
        self.vprin.btninicio.animateClick()

    def menum(self):
        if self.vprin.btnmenu.isChecked():
            self.vprin.menu.setMaximumSize(0,0)
        else:
            self.vprin.menu.setMaximumSize(200, 1000)