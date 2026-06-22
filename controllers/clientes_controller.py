import sqlite3

from PySide6.QtCore import Qt, QSortFilterProxyModel
from PySide6.QtGui import QStandardItem, QColor, QIcon, QFont, QStandardItemModel, QIntValidator

from models.clientes import ClienteModel
from models.equipos import EquipoModel


class ClientesController:
    def __init__(self, view):
        self.cvprin = view
        self.vprin = self.cvprin.ui
        self.registrando = False
        self.cliente_id = None
        self._conectareventos()


    def _conectareventos(self):
        # clientes -----------------------------------------------------------------------------------------------------
        self.modelequipos = QStandardItemModel()
        self.modelclientes = QStandardItemModel()
        self.vprin.telefono.setValidator(QIntValidator(0, 1000000000))  # (mínimo, máximo)
        self.filtro = QSortFilterProxyModel(self.cvprin)
        self.filtro.setSourceModel(self.modelclientes)
        self.filtro.setFilterCaseSensitivity(Qt.CaseSensitivity.CaseInsensitive)
        self.vprin.buscarcliente.textChanged.connect(self.filtro.setFilterFixedString)
        self.vprin.listView.setModel(self.filtro)
        self.vprin.listView_2.setModel(self.modelequipos)
        # botones clientes----------------------------------------------------------------------------------------------
        self.vprin.btnnuevoclient.clicked.connect(self.nuevo_cliente)
        self.vprin.btneditaclient.clicked.connect(self.edita_cliente)
        self.vprin.btnguardaclient.clicked.connect(self.guardar_cliente)
        self.vprin.listView.clicked.connect(self.al_clic)
        self.vprin.listView_2.clicked.connect(self.cvprin.registros.carga_clientes)
        self.vprin.listView_2.clicked.connect(self.clic_equipo)


    def clientes(self):
        self.lista_clientes()
        self.vprin.stack.setCurrentIndex(4)

    def nuevo_cliente(self, reg=False):
        self.registrando = reg
        self.vprin.idcliente.setText('')
        self.vprin.nombre.setText('')
        self.vprin.telefono.setText('')
        self.vprin.email.setText('')
        self.vprin.direccion.setText('')
        self.vprin.rfc.setText('')
        self.vprin.nombre.setFocus()
        self.cliente_read_only(False)

    def rellena_cliente(self, cid, registrando = True):
        cliente = ClienteModel()
        cliente.obtener_por_id(cid)
        self.registrando = registrando
        self.vprin.idcliente.setText(str(cid))
        self.vprin.nombre.setText(cliente.nombre)
        self.vprin.telefono.setText(cliente.telefono)
        self.vprin.email.setText(cliente.email)
        self.vprin.direccion.setText(cliente.direccion)
        self.vprin.rfc.setText(cliente.rfc)
        self.cliente_read_only(True)

    def guardar_cliente(self):
        nombre = self.vprin.nombre.text().upper()
        telefono = self.vprin.telefono.text()
        email = self.vprin.email.text()
        rfc = self.vprin.rfc.text().upper()
        direccion = self.vprin.direccion.toPlainText()
        idc = self.vprin.idcliente.text()
        if not idc:
            nid = ClienteModel().insertar((nombre,telefono,direccion,email,rfc))
            self.vprin.idcliente.setText(str(nid))
            idc = nid
        else:
            ClienteModel().actualizar(idc, (nombre, telefono, direccion, email, rfc))
        self.lista_clientes()
        if self.registrando:
            self.cvprin.registros.carga_clientes()
            self.vprin.stack.setCurrentIndex(1)
            self.vprin.rnombre.setCurrentIndex(self.vprin.rnombre.findData(idc))
            self.cvprin.cambioreg = True
            self.registrando = False

    def cliente_read_only(self, var):
        self.vprin.nombre.setReadOnly(var)
        self.vprin.telefono.setReadOnly(var)
        self.vprin.email.setReadOnly(var)
        self.vprin.direccion.setReadOnly(var)
        self.vprin.rfc.setReadOnly(var)

    def edita_cliente(self):
        self.cliente_read_only(False)

    def al_clic(self, index):
        item = self.filtro.mapToSource(index)
        cid = item.data(Qt.ItemDataRole.UserRole)
        self.rellena_cliente(cid)
        self.lista_equipos(cid)

    def clic_equipo(self):
        self.cvprin.registros.registros_cliente(self.cliente_id, self.vprin.listView_2.currentIndex().row())
        # self.vprin.btnregistros.click()

    def lista_clientes(self):
        client = ClienteModel().obtener_todos()
        self.modelclientes.clear()
        for i in range(len(client)):
            item = QStandardItem(f"{client[i][1]}\n📞{client[i][2]}")
            #item.setBackground(QColor("#728393"))
            item.setIcon(QIcon(':/iconos/iconos/person_user.ico'))
            item.setFont(QFont("Arial", 11, QFont.Weight.DemiBold))
            item.setData(client[i][0], Qt.ItemDataRole.UserRole)
            self.modelclientes.appendRow(item)

    def lista_equipos(self, cid):
        equipos = EquipoModel().obtener_por_idc(cid)
        self.modelequipos.clear()
        for i in range(len(equipos)):
            item = QStandardItem(
                f"{equipos[i][1]} \n{equipos[i][2]}\nModelo: {equipos[i][3]}\nEstatus: {equipos[i][5]}")
            item.setIcon(QIcon(':/iconos/iconos/electronicos.png'))
            item.setFont(QFont("Arial", 16, QFont.Weight.Medium))
            self.modelequipos.appendRow(item)
        self.cliente_id = cid
        #self.cvprin.registros.rellenar_registro(self.cliente_id)