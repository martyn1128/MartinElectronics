import re
from datetime import datetime

from PySide6.QtCore import Qt, QSortFilterProxyModel, QTimer, QDateTime
from PySide6.QtGui import QFont
from PySide6.QtSql import QSqlQueryModel
from PySide6.QtWidgets import QLineEdit, QCheckBox, QMessageBox, QCompleter, QTableWidgetItem

from controllers.entregas_controller import EntregasController
from interfaz import registro
from interfaz.ep_2 import EditaPorcentaje
from models.clientes import ClienteModel
from models.equipos import EquipoModel
from models.registros_model import RegistroModel
from models.reparacion_model import ReparacionModel
from recursos.reportes.genera_reporte import GeneraReporte

class RegistrosController:
    def __init__(self, view):
        self.cvprin = view
        self.vprin = self.cvprin.ui
        self.long = 0
        self.nuevo_reg = False
        self.ant = 0
        self.aant = 0
        self.ind = 0
        self.propred = 50
        self.nuevo_reg = False
        self.eex = None
        self.ui_edip = None
        self._conectareventos()

    def cambio(self):
        self.cvprin.cambio_en_reg()

    def equipo_existe(self):
        if self.nuevo_reg and self.vprin.nserie.text():
            equipo = EquipoModel()
            equipo.obtener_por_serie(serie=self.vprin.nserie.text())
            if equipo.id:
                save = QMessageBox.question(self.cvprin, "Martin Electronics's",
                                            f"se encontro un equipo con el numero de serie identico \n Equipo: {equipo.equipo}\n Marca: {equipo.marca} \n Modelo: {equipo.modelo} \n DESEA CREAR UNA NUEVA REPARACION PARA ESTE EQUIPO?\n (si no verifique el numero de serie)")
                if save == QMessageBox.StandardButton.Yes:
                    self.equipoqueexiste(equipo)
                else:
                    self.vprin.nserie.setText("")
                    self.vprin.nserie.setFocus()

    def _conectareventos(self):
        # Registros------------------------------------------------------------------------------------------------------
        for le in self.vprin.infoequipo.findChildren(QLineEdit):
            le.textEdited.connect(self.cambio)
        self.vprin.infadi.textChanged.connect(self.cambio)
        for cb in self.vprin.accesorios.findChildren(QCheckBox):
            cb.clicked.connect(self.cambio)
        self.vprin.accotro.textEdited.connect(self.cambio)
        self.vprin.rnombre.lineEdit().textEdited.connect(self.cambio)
        fuente = QFont()
        fuente.setPointSize(12)
        completer = QCompleter(self.vprin.rnombre.model(), self.cvprin)
        completer.setCompletionMode(QCompleter.CompletionMode.PopupCompletion)
        completer.setFilterMode(Qt.MatchFlag.MatchContains)  # ← busca en cualquier parte del texto
        completer.setCaseSensitivity(Qt.CaseSensitivity.CaseInsensitive)
        completer.popup().setFont(fuente)
        self.vprin.nserie.editingFinished.connect(self.equipo_existe)
        self.vprin.rnombre.setCompleter(completer)
        self.vprin.rnombre.lineEdit().setPlaceholderText('--Seleccione un cliente--')
        self.vprin.rnombre.currentIndexChanged.connect(self.actclient)
        self.vprin.rnombre.activated.connect(self.cambio)
        self.modelregistros = QSqlQueryModel()
        self.busq = QSortFilterProxyModel(self.cvprin)
        self.busq.setSourceModel(self.modelregistros)
        self.busq.setFilterCaseSensitivity(Qt.CaseSensitivity.CaseInsensitive)
        self.busq.setFilterKeyColumn(-1)
        self.vprin.buscarreg.textChanged.connect(self.busca)
        self.vprin.tableViewregistros.setModel(self.busq)
        self.vprin.repuestos_2.cellChanged.connect(self.cambiorepuestos)
        self.vprin.total_2.valueChanged.connect(self.calcula_servtec)
        self.vprin.garantia_2.valueChanged.connect(self.garantiafech)
        self.vprin.servtec_2.valueChanged.connect(self.calcula_costo)
        self.vprin.tabregistros.currentChanged.connect(self.cvprin.comprueba_cambio)
        self.vprin.tabregistros.currentChanged.connect(self.al_cambiar_pestaña)
        self.vprin.ods.valueChanged.connect(self.cambio_ods)
        self.vprin.fechaentrega_2.dateTimeChanged.connect(self.cambio_fechae)
        # botones registro----------------------------------------------------------------------------------------------
        #self.vprin.btnirrep.clicked.connect(self.ir_rep)
        self.vprin.btnnuevo.clicked.connect(self.nuevo)
        self.vprin.btnfin.clicked.connect(self.fin)
        self.vprin.btnant.clicked.connect(self.anterior)
        self.vprin.btnsig.clicked.connect(self.siguiente)
        self.vprin.btneliminar.clicked.connect(self.eliminar)
        self.vprin.btnguardar.clicked.connect(self.guardar)
        self.vprin.btninicior.clicked.connect(self.inicio)
        self.vprin.btnnuevocliente.clicked.connect(self.n_cliente)
        self.vprin.rbtneditaclient.clicked.connect(self.redita_cliente)
        self.vprin.btnimprimir.clicked.connect(self.rimprimir)
        self.vprin.tableViewregistros.doubleClicked.connect(self.abrir_registro)
        self.vprin.buscar.clicked.connect(self.busqueda_profunda)
        self.vprin.buscar.clicked.connect(lambda :self.vprin.statusbar.showMessage("Buscando...", 3000))
        self.vprin.fecharep_2.dateChanged.connect(self.cambio_fecha)
        self.vprin.repant_2.clicked.connect(self.ant_rep)
        self.vprin.repsig_2.clicked.connect(self.sig_rep)
        self.vprin.btneditaporce_2.clicked.connect(self.edita_porcentaje)

    def cambio_ods(self, num):
        if num > RegistroModel().ultimo()[0]:
            num = 1
            self.vprin.ods.setValue(num)
        elif num == 0:
            num = RegistroModel().ultimo()[0]
            self.vprin.ods.setValue(num)
        self.rellenar_registro(idr = num)

    def al_cambiar_pestaña(self, i):
        match i:
            case 0:
                self.vprin.tabregistros.setTabEnabled(2, False)
                self.cvprin.desconecta()
            case 1:
                self.cvprin.conecta()
                query = RegistroModel().query_todos()
                self.modelregistros.setQuery(query, self.cvprin.conexion)
            case 2:
                pass

    def cambio_fecha(self):
        self.vprin.fecha_rep_2.setText(self.vprin.fecharep_2.dateTime().toString('dd/MM/yyyy hh:mm:ss ap'))

    def garantiafech(self, dias):
        self.fh = self.vprin.fecharep_2.dateTime()
        fechgar = self.fh.addDays(dias)
        self.vprin.fechagarantia_2.setText(fechgar.toString("dd/MM/yyyy hh:mm:ss"))

    def registros(self):
        self.vprin.tabregistros.setTabEnabled(2, False)
        self.cliente_id = None
        self.vprin.stack.setCurrentIndex(1)
        self.vprin.tabregistros.setCurrentIndex(0)
        self.carga_clientes()
        self.rellenar_registro()

    def carga_clientes(self):
        clientes = ClienteModel().obtener_todos()

        self.vprin.rnombre.clear()
        for client in clientes:
            self.vprin.rnombre.addItem(client[1], client[0])

        self.vprin.rnombre.insertItem(0, "")

    def rimprimir(self):
        self.cvprin.comprueba_cambio()
        client = ClienteModel()
        client.obtener_por_id(self.imp[2])
        if not client:
            client = ['', '', '', '', '', '']
        datos = {"cliente": client, "equipo": self.imp, "fecha": datetime.now().strftime('%d/%m/%Y  %I:%M:%S %p')}
        GeneraReporte(datos, self.cvprin).reporte_de_entrada()
        #QDesktopServices.openUrl(QUrl.fromLocalFile(str(datos["equipo"][0]) + ".pdf"))

    def abrir_registro(self):
        fila = self.vprin.tableViewregistros.currentIndex().row()
        contenido = [self.vprin.tableViewregistros.model().index(fila, i).data() for i in range(14)]
        match contenido[8]:
            case 'Completado':
                self.lista_registros(contenido)
            case 'Pendiente de Revisión':
                self.vprin.btnreparaciones.click()
                self.cvprin.reparaciones.rellena_reparacion(contenido)
            case 'Pendiente de Reparación':
                self.vprin.btnreparaciones.click()
                self.cvprin.reparaciones.rellena_reparacion(contenido,1)
            case 'Pendiente de Entrega':
                self.vprin.btnentregas.click()
                self.cvprin.entregascontroller.entregar(idreg=contenido[0])

    def lista_registros(self, contenido):
        self.vprin.tabregistros.setTabEnabled(2, True)
        self.vprin.equipo_2.setText(contenido[2])
        self.vprin.marca_2.setText(contenido[3])
        self.vprin.modelo_2.setText(contenido[4])
        self.vprin.nserie_2.setText(contenido[5])

        cliente = ClienteModel().obtener_por_id(contenido[12])
        self.vprin.nombre_2.setText(cliente[1])
        self.vprin.telefono_2.setText(cliente[2])
        self.vprin.direccion_2.setText(cliente[3])
        self.vprin.email_2.setText(cliente[4])
        self.vprin.rfc_2.setText(cliente[5])

        self.infreg = RegistroModel().obtener_todos_por_idequipo(contenido[1])
        self.vprin.rep_2.setText("1")
        self.vprin.rde_2.setText(str(len(self.infreg)))
        self.indreg = 0
        self.rellena_info_registro()

        self.vprin.tabregistros.setCurrentIndex(2)

    def rellena_info_registro(self):
        self.vprin.garantia_2.setValue(0)
        self.vprin.fechaent.setText("")
        self.vprin.rep_2.setText(str(self.indreg+1))
        reg = self.infreg[self.indreg]
        rep = ReparacionModel().obtener_todo_por_idr(reg[0])
        self.vprin.falla_2.setText(reg[3])
        accesorios = reg[4]
        self.vprin.fecharep_2.blockSignals(True)
        self.vprin.fecharep_2.setDateTime(QDateTime.currentDateTime())
        self.vprin.fecharep_2.blockSignals(False)
        self.vprin.cableac_2.setChecked(False)
        self.vprin.controlr_2.setChecked(False)
        self.vprin.eliminador_2.setChecked(False)
        self.vprin.base_2.setChecked(False)
        self.vprin.basepared_2.setChecked(False)
        self.vprin.pilas_2.setChecked(False)
        self.vprin.cables_2.setChecked(False)
        if accesorios:
            if 'Cable AC' in accesorios:
                self.vprin.cableac_2.setChecked(True)
            if 'Control Remoto' in accesorios:
                self.vprin.controlr_2.setChecked(True)
            if 'Eliminador' in accesorios:
                self.vprin.eliminador_2.setChecked(True)
            if 'Base,' in accesorios:
                self.vprin.base_2.setChecked(True)
            if 'Base de Pared' in accesorios:
                self.vprin.basepared_2.setChecked(True)
            if 'Pilas' in accesorios:
                self.vprin.pilas_2.setChecked(True)
            if 'Cables' in accesorios:
                self.vprin.cables_2.setChecked(True)
            part = accesorios.split("\n")
            ot = part.pop()
            if ot == "Cable AC" or ot == "Control Remoto" or ot == "Eliminador" or ot == "Base" or ot == "Base Pared" or ot == "Plias" or ot == "Cables":
                pass
            else:
                self.vprin.accotro_2.setText(ot)
        self.vprin.infadi_2.setText(reg[5])
        self.vprin.estatus_2.setText(reg[6])
        self.vprin.fecha_2.setText(reg[7])
        self.vprin.fechaentrega_2.setDateTime(QDateTime().fromString(reg[8], 'dd/MM/yyyy hh:mm:ss ap'))
        self.vprin.fechagarantia_2.clear()
        if rep:
            self.vprin.diagnostico_2.setPlainText(rep[6])
            if rep[7]:
                repuestos = eval(rep[7])
            else:
                repuestos = ""
            self.vprin.repuestos_2.setRowCount(0)
            for i in range(len(repuestos) - 1):
                self.vprin.repuestos_2.insertRow(i)
                self.vprin.repuestos_2.setItem(i, 0, QTableWidgetItem(repuestos[i][0]))
                item = QTableWidgetItem(repuestos[i][1])
                item.setTextAlignment(Qt.AlignmentFlag.AlignRight)
                self.vprin.repuestos_2.setItem(i, 1, item)
            indice = self.vprin.tecnico_2.findData(rep[2], role=Qt.ItemDataRole.UserRole)
            if indice != -1:
                self.vprin.tecnico_2.setCurrentIndex(indice)
            else:
                self.vprin.tecnico_2.setCurrentIndex(0)
            self.vprin.total_2.setValue(rep[4] if rep[4] else 0.00)
            self.vprin.presupuesto_2.setChecked(rep[12] if rep[12] else False)
            if rep[3]:
                self.vprin.fecharep_2.setDateTime(QDateTime().fromString(rep[3], 'dd/MM/yyyy hh:mm:ss ap'))
            self.vprin.garantia_2.setValue(int(rep[8]) if rep[8] else 0)

    def registros_cliente(self,cid,ind):
        self.ind = ind
        self.vprin.stack.setCurrentIndex(1)
        self.vprin.tabregistros.setCurrentIndex(0)
        self.rellenar_registro(cid)

    def n_cliente(self):  # nuevo cliente
        self.cvprin.cambioreg = False
        self.vprin.btnclientes.blockSignals(True)
        self.vprin.btnclientes.animateClick()
        self.vprin.btnclientes.blockSignals(False)
        self.vprin.stack.setCurrentIndex(4)
        self.cvprin.clientescontroller.nuevo_cliente(reg=True)


    def redita_cliente(self):
        self.vprin.btnclientes.click()
        if self.vprin.rnombre.currentData():
            self.cvprin.clientescontroller.rellena_cliente(self.vprin.rnombre.currentData(), registrando=True)
        self.vprin.btneditaclient.click()

    def actclient(self):
        if self.vprin.rnombre.currentData():
            cliente = ClienteModel()
            cliente.obtener_por_id(self.vprin.rnombre.currentData())
            self.vprin.rtelefono.setText(cliente.telefono)
            self.vprin.rdireccion.setText(cliente.direccion)
            self.vprin.remail.setText(cliente.email)
            self.vprin.rrfc.setText(cliente.rfc)
        else:
            self.vprin.rtelefono.setText('')
            self.vprin.rdireccion.setText('')
            self.vprin.remail.setText('')
            self.vprin.rrfc.setText('')


    def rellenar_registro(self, cid=None, id=None, idr = None):
        res2 = None
        rid = None
        self.nuevo_reg = False
        self.ant = self.aant
        self.aant = 1
        self.indrep = 0
        self.vprin.tableView_2.clearSelection()
        self.cvprin.comprueba_cambio()
        self.vprin.btnant.setEnabled(True)
        self.vprin.btnsig.setEnabled(True)
        if id:
            res = RegistroModel().obtener_todos_por_equipo(id)
            self.long = len(res) - 1
            self.ind = 0
        elif cid:
            res = RegistroModel().obtener_por_cliente(cid)
            self.cliente_id = cid
            self.long = len(res) - 1
        elif idr:
            res2 = RegistroModel().obtener_por_idr(idr)
            self.ind = idr-1
            self.long = RegistroModel().numero()[0]-1
        else:
            res = RegistroModel().obtener_todos()
            self.long = len(res) - 1

        self.vprin.no.setText(str(self.ind + 1))
        self.vprin.de.setText(str(self.long + 1))
        if res2:
            self.imp = res2[0]
            rid, eid, cliente_id, equipo, marca, modelo, serie, problema, accesorios, info_adicional, estatus, fecha_ingreso, user = \
                res2[0]
        elif res:
            self.imp = res[self.ind]
            rid, eid, cliente_id, equipo, marca, modelo, serie, problema, accesorios, info_adicional, estatus, fecha_ingreso, user = \
            res[self.ind]
        if rid:
            self.registro_actual = rid
            self.equipo_actual = eid
            self.vprin.equipo.setText(equipo)
            self.vprin.marca.setText(marca)
            self.vprin.modelo.setText(modelo)
            self.vprin.nserie.setText(serie)
            self.vprin.falla.setText(problema)
            self.vprin.infadi.blockSignals(True)
            self.vprin.infadi.setText(info_adicional)
            self.vprin.infadi.blockSignals(False)
            self.vprin.fecha.setText(fecha_ingreso)
            self.vprin.ods.blockSignals(True)
            self.vprin.ods.setValue(rid)
            self.vprin.ods.blockSignals(False)
            self.vprin.restatus.setText(estatus)
            #self.cvprin.reparaciones.rellena_reparacion(res[self.ind])
            self.vprin.cableac.setChecked(False)
            self.vprin.controlr.setChecked(False)
            self.vprin.eliminador.setChecked(False)
            self.vprin.base.setChecked(False)
            self.vprin.basepared.setChecked(False)
            self.vprin.pilas.setChecked(False)
            self.vprin.cables.setChecked(False)
            if accesorios:
                if 'Cable AC' in accesorios:
                    self.vprin.cableac.setChecked(True)
                if 'Control Remoto' in accesorios:
                    self.vprin.controlr.setChecked(True)
                if 'Eliminador' in accesorios:
                    self.vprin.eliminador.setChecked(True)
                if 'Base,' in accesorios:
                    self.vprin.base.setChecked(True)
                if 'Base de Pared' in accesorios:
                    self.vprin.basepared.setChecked(True)
                if 'Pilas' in accesorios:
                    self.vprin.pilas.setChecked(True)
                if 'Cables' in accesorios:
                    self.vprin.cables.setChecked(True)
                part = accesorios.split("\n")
                ot = part.pop()
                if ot == "Cable AC" or ot == "Control Remoto" or ot == "Eliminador" or ot == "Base" or ot == "Base Pared" or ot == "Plias" or ot == "Cables":
                    pass
                else:
                    self.vprin.accotro.setText(ot)
            indice = self.vprin.rnombre.findData(cliente_id, role=Qt.ItemDataRole.UserRole)
            if indice != -1:
                self.vprin.rnombre.setCurrentIndex(indice)
            else:
                self.vprin.rnombre.setCurrentIndex(0)


    def nuevo(self):
        self.nuevo_reg = True
        self.ind = self.long + 1
        self.vprin.rnombre.setCurrentIndex(0)
        fecha = datetime.now()
        fh = fecha.strftime('%d/%m/%Y  %I:%M:%S %p')
        self.vprin.no.setText(str(self.long + 2))
        self.vprin.de.setText(str(self.long + 2))
        self.vprin.ods.blockSignals(True)
        self.vprin.ods.setValue(0)
        self.vprin.ods.blockSignals(False)
        self.vprin.fecha.setText(fh)
        self.vprin.equipo.setText('')
        self.vprin.marca.setText('')
        self.vprin.modelo.setText('')
        self.vprin.nserie.setText('')
        self.vprin.falla.setText('')
        self.vprin.infadi.setText('')
        self.vprin.accotro.setText('')
        self.vprin.restatus.setText('Pendiente de Revisión')
        self.vprin.cableac.setChecked(False)
        self.vprin.controlr.setChecked(False)
        self.vprin.eliminador.setChecked(False)
        self.vprin.base.setChecked(False)
        self.vprin.basepared.setChecked(False)
        self.vprin.pilas.setChecked(False)
        self.vprin.cables.setChecked(False)
        self.vprin.equipo.setFocus()

    def eliminar(self):
        ide = self.vprin.ods.text()
        if ide == '--':
            self.cvprin.cambioreg = False
        else:
            delete = QMessageBox.question(self.cvprin, "Martin Electronics's", "Desea Eliminar el registro?")
            if delete == QMessageBox.StandardButton.Yes:
                RegistroModel().eliminar(self.registro_actual)
                self.long -= 1
                self.ind -= 1
        self.rellenar_registro()

    def guardar(self):
        self.vprin.statusbar.showMessage('Guardando.....', 1000)
        if not self.vprin.rnombre.currentData():
            QMessageBox.warning(self.cvprin, "Martin Electronic's", "No ha seleccionado ningun cliente")
        self.cvprin.cambioreg = False
        equipo_data = (
            self.vprin.rnombre.currentData(),
            self.vprin.equipo.text(),
            self.vprin.marca.text(),
            self.vprin.modelo.text(),
            self.vprin.nserie.text()
        )

        # construir accesorios
        accesorios = ''
        if self.vprin.cableac.isChecked():
            accesorios += 'Cable AC, \n'
        if self.vprin.controlr.isChecked():
            accesorios += 'Control Remoto, \n'
        if self.vprin.eliminador.isChecked():
            accesorios += 'Eliminador, \n'
        if self.vprin.base.isChecked():
            accesorios += 'Base, \n'
        if self.vprin.basepared.isChecked():
            accesorios += 'Base de Pared, \n'
        if self.vprin.pilas.isChecked():
            accesorios += 'Pilas, \n'
        if self.vprin.cables.isChecked():
            accesorios += 'Cables, \n'
        if self.vprin.accotro.text():
            accesorios += self.vprin.accotro.text()

        registro_data = (
            self.vprin.falla.text(),
            accesorios,
            self.vprin.infadi.toPlainText(),
            self.vprin.restatus.text(),
            self.vprin.fecha.text(),
            self.cvprin.user[0]
        )
        ide = self.vprin.ods.text()

        equipo_model = EquipoModel()
        registro_model = RegistroModel()

        # 🔵 INSERT
        if ide == '--':
            msj = "Guardando..."
            if self.eex:
                #equipo_model.actualizar(equipo_data, self.eex)
                equipo_id = self.eex
                self.eex = None
            else:
                equipo_id = equipo_model.insertar(equipo_data)

            registro_model.insertar((
                        equipo_id,
                        *registro_data,
                    ))
            self.long += 1

        # 🟡 UPDATE
        else:
            msj = "Actualizando....."
            equipo_id = self.equipo_actual

            # actualizar equipo
            equipo_model.actualizar(equipo_id, equipo_data)

            # actualizar registro
            registro_model.actualizar(equipo_id, registro_data)

        self.rellenar_registro()
        QTimer.singleShot(500, lambda: self.vprin.statusbar.showMessage(msj, 3000))
        self.rellenar_registro()

    def inicio(self):
        self.ind = 0
        self.rellenar_registro(self.cliente_id)
        self.vprin.btnsig.setEnabled(True)
        self.vprin.btnant.setEnabled(False)

    def fin(self):
        self.ind = self.long
        self.rellenar_registro(self.cliente_id)
        self.vprin.btnant.setEnabled(True)
        self.vprin.btnsig.setEnabled(False)

    def anterior(self):
        if self.ind == 0:
            self.vprin.btnant.setEnabled(False)
        else:
            self.ind -= 1
            self.rellenar_registro(self.cliente_id)
            self.vprin.btnsig.setEnabled(True)

    def siguiente(self):
        if self.ind < self.long:
            self.ind += 1
            self.rellenar_registro(self.cliente_id)
            self.vprin.btnant.setEnabled(True)
        else:
            self.vprin.btnsig.setEnabled(False)

    def busca(self, cad):
        self.busq.setFilterFixedString(cad)
        if self.vprin.buscarreg.text():
            self.vprin.msjreg.setText('Resultados:')
        else:
            self.vprin.msjreg.setText('Todos los registros:')

    def busqueda_profunda(self):
        cad = self.vprin.buscarreg.text()
        self.vprin.buscarreg.setText("")
        for i in range(0, RegistroModel().numero()[0] - 1, 5):
            self.vprin.tableViewregistros.selectRow(i)

        self.vprin.buscarreg.setText(cad)

    def cambiorepuestos(self, fila, colum):
        self.vprin.repuestos_2.blockSignals(True)
        self.vprin.porcentaje_2.setText(str(self.propred))
        if colum:
            precio = 0
            for i in range(self.vprin.repuestos_2.rowCount()):
                try:
                    p = re.findall(r"\d+\.?\d*", self.vprin.repuestos_2.item(i, 1).text())[0]
                    precio += float(p)
                    if i == fila:
                        item = QTableWidgetItem("$" + p)
                        item.setTextAlignment(Qt.AlignmentFlag.AlignRight)
                        self.vprin.repuestos_2.setItem(fila, colum, item)
                except Exception as e:
                    print(e)
                    item = QTableWidgetItem("$0.0")
                    item.setTextAlignment(Qt.AlignmentFlag.AlignRight)
                    self.vprin.repuestos_2.setItem(fila, colum, item)
            self.vprin.totalrep_2.setText(str(precio))
            self.calcula_costo()
        self.vprin.repuestos_2.blockSignals(False)

    def calcula_costo(self):
        self.vprin.total_2.blockSignals(True)
        total = float(self.vprin.totalrep_2.text()) + self.vprin.servtec_2.value()
        self.vprin.total_2.setValue(total)
        self.vprin.total_2.blockSignals(False)

    def calcula_servtec(self):
        self.vprin.servtec_2.blockSignals(True)
        servtec = self.vprin.total_2.value() - float(self.vprin.totalrep_2.text())
        self.vprin.servtec_2.setValue(servtec)
        self.vprin.servtec_2.blockSignals(False)

    def ant_rep(self):
            self.indreg -= 1
            if self.indreg <= 0:
                if self.indreg < 0:
                    self.indreg += 1
                self.vprin.repant_2.setEnabled(False)
            self.vprin.repsig_2.setEnabled(True)
            self.rellena_info_registro()

    def sig_rep(self):
        self.indreg += 1
        if self.indreg >= int(self.vprin.rde_2.text()) - 1:
            if self.indreg > int(self.vprin.rde_2.text()) - 1:
                self.indreg -= 1
            self.vprin.repsig_2.setEnabled(False)
        self.vprin.repant_2.setEnabled(True)
        self.rellena_info_registro()

    def edita_porcentaje(self):
        self.ui_edip = EditaPorcentaje(self.cvprin)
        self.ui_edip.exec()

    def equipoqueexiste(self, equipo):
        self.vprin.equipo.setText(equipo.equipo)
        self.vprin.marca.setText(equipo.marca)
        self.vprin.modelo.setText(equipo.modelo)
        self.vprin.nserie.setText(equipo.serie)
        indice = self.vprin.rnombre.findData(equipo.clientid, role=Qt.ItemDataRole.UserRole)
        if indice != -1:
            self.vprin.rnombre.setCurrentIndex(indice)
        else:
            self.vprin.rnombre.setCurrentIndex(0)
        self.eex = equipo.id

    def cambio_fechae(self):
        self.vprin.fechaent.setText(self.vprin.fechaentrega_2.dateTime().toString('dd/MM/yyyy hh:mm:ss ap'))


