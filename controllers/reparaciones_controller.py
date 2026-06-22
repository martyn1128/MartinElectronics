import re

from PySide6.QtCore import Qt, QDateTime, QTimer
from PySide6.QtSql import QSqlQueryModel
from PySide6.QtWidgets import QTableView, QTableWidgetItem, QMessageBox

from models.registros_model import RegistroModel
from models.reparacion_model import ReparacionModel
from models.usarios import UsuariosModel


class ReparacionesController:
    def __init__(self, view):
        self.indrep = 0
        self.idrep = 0
        self.ideq = 0
        self.antrep = 0
        self.ant = 0
        self.aant = 0
        self.cvprin = view
        self.vprin = self.cvprin.ui
        self._conectarEventos()

    def _conectarEventos(self):
        self.vprin.diagnostico.textChanged.connect(self.cvprin.cambio_en_rep)
        self.vprin.repuestos.itemChanged.connect(self.cvprin.cambio_en_rep)
        self.vprin.tecnico.activated.connect(self.cvprin.cambio_en_rep)
        self.vprin.total.valueChanged.connect(self.cvprin.cambio_en_rep)
        self.vprin.servtec.valueChanged.connect(self.cvprin.cambio_en_rep)
        self.vprin.garantia.valueChanged.connect(self.cvprin.cambio_en_rep)
        self.vprin.fecha_rep.textChanged.connect(self.cvprin.cambio_en_rep)
        self.modelrecive = QSqlQueryModel()
        self.vprin.tableView.setModel(self.modelrecive)
        self.vprin.tableView.setSelectionBehavior(QTableView.SelectionBehavior.SelectRows)
        self.vprin.tableView.clicked.connect(self.cvprin.desconecta)
        self.vprin.tableView.clicked.connect(lambda :self.rellena_reparacion())
        self.modelrepa = QSqlQueryModel()
        self.vprin.tableView_2.setModel(self.modelrepa)
        self.vprin.tableView_2.setSelectionBehavior(QTableView.SelectionBehavior.SelectRows)
        self.vprin.tableView_2.clicked.connect(self.cvprin.desconecta)
        self.vprin.tableView_2.clicked.connect(lambda: self.rellena_reparacion(True))
        self.vprin.garantia.valueChanged.connect(self.garantiafech)
        self.vprin.repuestos.cellChanged.connect(self.cambiorepuestos)
        self.vprin.anadir.clicked.connect(self.nuevo_repuesto)
        self.vprin.btneliminarep.clicked.connect(self.eliminar_repuesto)
        self.vprin.servtec.valueChanged.connect(self.calcula_costo)
        self.vprin.total.valueChanged.connect(self.calcula_servtec)
        self.vprin.atras.clicked.connect(self.regresar)
        self.vprin.btnconfirmar.clicked.connect(self.confirma_rep)
        self.vprin.fecharep.dateChanged.connect(self.cambio_fecha)
        self.vprin.hoy.clicked.connect(self.fechahoy)
        self.vprin.btnentsinrep.clicked.connect(self.entregarsinreparar)

    # --REPARACIONES--------------------------------------------------------------------------------------------------
    def carga_tecnicos(self):
        res = UsuariosModel().obtener_tecnicos()
        self.vprin.tecnico.clear()
        for opcion in res:
            self.vprin.tecnico.addItem(opcion[1], opcion[0])
        self.vprin.tecnico.insertItem(0, "")
    def regresar(self):
        #self.vprin.stack.setCurrentIndex(self.ant)
        self.cvprin.blockSignals(True)
        match self.ant:
            case 0:
                self.vprin.btninicio.click()
            case 1:
                self.vprin.btnregistros.blockSignals(True)
                self.vprin.btnregistros.click()
                self.vprin.stack.setCurrentIndex(1)
                self.vprin.btnregistros.blockSignals(False)
            case 2:
                self.vprin.btnreparaciones.click()
                self.vprin.stackreparaciones.setCurrentIndex(0)
                self.vprin.tabrepara.setCurrentIndex(self.antrep)
            case 3:
                self.vprin.btnentregas.click()
            case 4:
                self.vprin.btnclientes.click()
            case 5:
                self.vprin.btnpago.click()
            case 6:
                self.vprin.btnconfig.click()
        self.cvprin.blockSignals(False)


    def reparacion(self):
        self.ant = self.aant
        self.aant = 2
        self.vprin.stack.setCurrentIndex(2)
        self.vprin.stackreparaciones.setCurrentIndex(0)
        self.cvprin.conecta()
        model = ReparacionModel()
        self.modelrecive.setQuery(model.query_recibe(), self.cvprin.conexion)
        self.modelrepa.setQuery(model.query_reparacion(), self.cvprin.conexion)

    def cambio_fecha(self):
        self.vprin.fecha_rep.blockSignals(True)
        self.vprin.fecha_rep.setText(self.vprin.fecharep.dateTime().toString('dd/MM/yyyy hh:mm:ss ap'))
        self.vprin.fecha_rep.blockSignals(False)

    def garantiafech(self, dias):
        self.fh = self.vprin.fecharep.dateTime()
        fechgar = self.fh.addDays(dias)
        self.vprin.fechagarantia.setText(fechgar.toString("dd/MM/yyyy hh:mm:ss"))

    def cambiorepuestos(self, fila, colum):
        self.vprin.repuestos.blockSignals(True)
        if colum:
            precio = 0
            for i in range(self.vprin.repuestos.rowCount()):
                try:
                    p = re.findall(r"\d+\.?\d*", self.vprin.repuestos.item(i, 1).text())[0]
                    precio += float(p)
                    if i == fila:
                        item = QTableWidgetItem("$" + p)
                        item.setTextAlignment(Qt.AlignmentFlag.AlignRight)
                        self.vprin.repuestos.setItem(fila, colum, item)
                except Exception as e:
                    print(e)
                    item = QTableWidgetItem("$0.0")
                    item.setTextAlignment(Qt.AlignmentFlag.AlignRight)
                    self.vprin.repuestos.setItem(fila, colum, item)
            self.vprin.totalrep.setText(str(precio))
            self.calcula_costo()
        self.vprin.repuestos.blockSignals(False)

    def nuevo_repuesto(self):
        self.vprin.repuestos.blockSignals(True)
        nfil = self.vprin.repuestos.rowCount()
        self.vprin.repuestos.insertRow(nfil)
        self.vprin.repuestos.setItem(nfil, 0, QTableWidgetItem('pendiente'))
        item = QTableWidgetItem('$0')
        item.setTextAlignment(Qt.AlignmentFlag.AlignRight)
        self.vprin.repuestos.setItem(nfil, 1, item)
        self.vprin.repuestos.blockSignals(False)

    def eliminar_repuesto(self):
        fila = self.vprin.repuestos.currentRow()
        self.vprin.repuestos.removeRow(fila)

    def calcula_costo(self):
        self.vprin.total.blockSignals(True)
        total = float(self.vprin.totalrep.text()) + self.vprin.servtec.value()
        self.vprin.total.setValue(total)
        self.vprin.total.blockSignals(False)

    def calcula_servtec(self):
        self.vprin.servtec.blockSignals(True)
        servtec = self.vprin.total.value() - float(self.vprin.totalrep.text())
        self.vprin.servtec.setValue(servtec)
        self.vprin.servtec.blockSignals(False)

    def rellena_reparacion(self, rep=None):
        self.carga_tecnicos()
        self.ant = 2
        self.vprin.diagnostico.blockSignals(True)
        self.vprin.diagnostico.setPlainText('')
        self.vprin.diagnostico.blockSignals(False)
        self.vprin.repuestos.setRowCount(0)
        self.nuevo_repuesto()
        self.vprin.total.blockSignals(True)
        self.vprin.servtec.blockSignals(True)
        self.vprin.totalrep.setText('0.00')
        self.vprin.total.setValue(0.00)
        self.vprin.servtec.setValue(0.00)
        self.vprin.total.blockSignals(True)
        self.vprin.servtec.blockSignals(False)
        self.vprin.garantia.setValue(0)
        self.vprin.fecharep.blockSignals(True)
        self.vprin.fecharep.setDateTime(QDateTime.currentDateTime())
        self.vprin.fecharep.blockSignals(False)
        if rep:
            if isinstance(rep, bool):
                equipo = self.vprin.tableView_2.selectedIndexes()
                self.antrep = 1
                self.rellena_inforep(rep)
                self.vprin.repequipo.setText(equipo[1].data())
                self.vprin.repmarca.setText(equipo[2].data())
                self.vprin.repmodelo.setText(equipo[3].data())
                self.vprin.repnserie.setText(equipo[4].data())
                self.vprin.repfalla.setText(equipo[5].data())
                self.vprin.repinfadi.setText(equipo[6].data())
                self.vprin.stackreparaciones.setCurrentIndex(1)
                self.vprin.stackinfrep.setCurrentIndex(1)
                self.vprin.btnconfirmar.setText('Confirmar reparación')
                self.ideq = equipo[0].data()
            """else:
                equipo = rep
                self.vprin.repequipo.setText(str(equipo[2]))
                self.vprin.repmarca.setText(str(equipo[3]))
                self.vprin.repmodelo.setText(str(equipo[4]))
                self.vprin.repnserie.setText(str(equipo[5]))
                self.vprin.repfalla.setText(str(equipo[6]))
                self.vprin.repinfadi.setText(str(equipo[8]))
                self.vprin.stackreparaciones.setCurrentIndex(1)
                self.ideq = equipo[0]
                print(self.vprin.total.value())
                if self.vprin.total.value():
                    self.vprin.btnconfirmar.setText('Confirmar reparación')
                    self.vprin.repant.setEnabled(True)
                    self.vprin.repsig.setEnabled(True)
                    self.rellena_inforep(equipo[0])
                    self.vprin.stackinfrep.setCurrentIndex(1)
                else:
                    self.vprin.btnconfirmar.setText('Confirmar revisión')
                    self.vprin.stackinfrep.setCurrentIndex(0)"""
        else:
            self.vprin.stackreparaciones.setCurrentIndex(1)
            self.vprin.stackinfrep.setCurrentIndex(0)
            self.vprin.btnconfirmar.setText('Confirmar revición')
            equipo = self.vprin.tableView.selectedIndexes()
            self.vprin.repequipo.setText(equipo[1].data())
            self.vprin.repmarca.setText(equipo[2].data())
            self.vprin.repmodelo.setText(equipo[3].data())
            self.vprin.repnserie.setText(equipo[4].data())
            self.vprin.repfalla.setText(equipo[5].data())
            self.vprin.repinfadi.setText(equipo[6].data())
            self.vprin.diagnostico.blockSignals(True)
            self.vprin.diagnostico.setPlainText(equipo[12].data())
            self.vprin.diagnostico.blockSignals(False)
            self.antrep = 0
            self.ideq = equipo[0].data()
        self.fh = QDateTime.currentDateTime()
        self.vprin.fecharep.setMaximumDateTime(self.fh)
        self.cvprin.cambiorep = False

    def rellena_inforep(self, ide=None):
        self.vprin.fecha_rep.blockSignals(True)
        self.vprin.fecha_rep.setText('')
        self.vprin.fecha_rep.blockSignals(False)
        if ide:
            if isinstance(ide, bool):
                if self.vprin.tableView_2.selectedIndexes():
                    idrep = int(self.vprin.tableView_2.selectedIndexes()[12].data())
            else:
                idrep = ide
        else:
            idrep = self.vprin.tableView.selectedIndexes()[12].data()
        rep = ReparacionModel().obtener_por_id(idrep)
        self.vprin.fechagarantia.clear()
        if rep:
            rep = rep[self.indrep]
            self.vprin.diagnostico.blockSignals(True)
            self.vprin.diagnostico.setPlainText(rep[3])
            self.vprin.diagnostico.blockSignals(False)
            if rep[4]:
                repuestos = eval(rep[4])
            else:
                repuestos = ""
            self.vprin.repuestos.setRowCount(0)
            for i in range(len(repuestos) - 1):
                self.vprin.repuestos.insertRow(i)
                self.vprin.repuestos.setItem(i, 0, QTableWidgetItem(repuestos[i][0]))
                item = QTableWidgetItem(repuestos[i][1])
                item.setTextAlignment(Qt.AlignmentFlag.AlignRight)
                self.vprin.repuestos.setItem(i, 1, item)
            indice = self.vprin.tecnico.findData(rep[7], role=Qt.ItemDataRole.UserRole)
            if indice != -1:
                self.vprin.tecnico.setCurrentIndex(indice)
            else:
                self.vprin.tecnico.setCurrentIndex(0)
            self.vprin.servtec.blockSignals(True)
            self.vprin.total.blockSignals(True)
            self.vprin.total.setValue(rep[2] if rep[2] else 0.00)
            self.vprin.servtec.setValue(rep[8])
            self.vprin.servtec.blockSignals(False)
            self.vprin.total.blockSignals(False)
            if rep[5]:
                self.vprin.fecharep.setDateTime(QDateTime().fromString(rep[5], 'dd/MM/yyyy hh:mm:ss ap'))
            self.vprin.garantia.setValue(int(rep[6]) if rep[6] else 0)

    def confirma_rep(self):
        self.vprin.statusbar.showMessage('Guardando........', 1000)
        tecnico = self.vprin.tecnico.currentData()

        diagnostico = self.vprin.diagnostico.toPlainText()
        repuestos = []
        for i in range(self.vprin.repuestos.rowCount()):
            rep = self.vprin.repuestos.item(i, 0).text()
            preci = self.vprin.repuestos.item(i, 1).text()
            repuestos.append((rep, preci))
        repuestos.append(self.vprin.totalrep.text())
        costot = self.vprin.total.value()
        regi = RegistroModel()
        repa = ReparacionModel()
        if self.vprin.stackinfrep.currentIndex():
            idrep = int(self.vprin.tableView_2.selectedIndexes()[12].data())
            idreg = int(self.vprin.tableView_2.selectedIndexes()[13].data())
            if self.vprin.fecha_rep.text():
                regi.actualizar_estatus(reg_id=idreg, estatus="Pendiente de Entrega")
            else:
                conti = QMessageBox.question(
                    self.cvprin,
                    "Martin Electronic's",
                    "Si no selecciona una fecha de reparación el estatus del registro permanecerá en: 'Pendiente de Reparación'\n"
                    "¿Desea continuar?",
                    QMessageBox.StandardButton.Ok | QMessageBox.StandardButton.Cancel
                )
                if conti == QMessageBox.StandardButton.Cancel:
                    return None
            repa.actualizar(idrep, (tecnico, self.vprin.fecha_rep.text(), costot, diagnostico, f"{repuestos}", self.vprin.garantia.value(), None, None, None, self.vprin.servtec.value()))
            msj = 'Reparación guardada correctamente...'
        else:
            idrep = int(self.vprin.tableView.selectedIndexes()[10].data())
            idreg = int(self.vprin.tableView.selectedIndexes()[11].data())
            repa.actualizar(idrep, (tecnico, self.vprin.fecha_rep.text(), costot, diagnostico, f"{repuestos}",self.vprin.garantia.value(), None, None, None, self.vprin.servtec.value()))
            regi.actualizar_estatus(reg_id=idreg, estatus="Pendiente de Reparación")
            msj = 'Revición guardada correctamente...'
        self.cvprin.cambiorep = False
        QTimer.singleShot(500, lambda: self.vprin.statusbar.showMessage(msj, 3000))

    def fechahoy(self):
        self.vprin.fecharep.setDateTime(QDateTime.currentDateTime())
        self.vprin.fecha_rep.setText(self.vprin.fecharep.dateTime().toString('dd/MM/yyyy hh:mm:ss ap'))

    def entregarsinreparar(self):
        self.vprin.statusbar.showMessage('Guardando........', 1000)
        tecnico = self.vprin.tecnico.currentData()
        diagnostico = self.vprin.diagnostico.toPlainText()
        repuestos = []
        for i in range(self.vprin.repuestos.rowCount()):
            rep = self.vprin.repuestos.item(i, 0).text()
            preci = self.vprin.repuestos.item(i, 1).text()
            repuestos.append((rep, preci))
        repuestos.append(self.vprin.totalrep.text())
        costot = self.vprin.total.value()
        regi = RegistroModel()
        repa = ReparacionModel()
        if self.vprin.stackinfrep.currentIndex():
            idrep = int(self.vprin.tableView_2.selectedIndexes()[12].data())
        else:
            idrep = int(self.vprin.tableView.selectedIndexes()[10].data())
        fecha = QDateTime.currentDateTime().toString("dd/MM/yyyy hh:mm")
        conti = QMessageBox.question(
            self.cvprin,
            "Martin Electronic's",
            f"Usted esta entregando el equipo SIN REPARAR con la fecha: {fecha}\n"
            "¿Desea continuar?",
            QMessageBox.StandardButton.Ok | QMessageBox.StandardButton.Cancel
        )
        if conti == QMessageBox.StandardButton.Cancel:
            return None
        regi.actualizar_estatus(rep_id=idrep, estatus="Completado", fe=fecha)
        repa.actualizar(idrep, (tecnico, None, costot, diagnostico, f"{repuestos}",
                                self.vprin.garantia.value(), None, False,
                                None, self.vprin.servtec.value()))
        msj = 'Entrega guardada correctamente...'
        QTimer.singleShot(500, lambda: self.vprin.statusbar.showMessage(msj, 3000))