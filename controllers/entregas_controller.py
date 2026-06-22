import re
from datetime import datetime

from PySide6.QtCore import Qt, QDateTime, QTimer
from PySide6.QtGui import QStandardItemModel, QStandardItem, QColor, QIcon, QFont
from PySide6.QtWidgets import (QTableWidgetItem, QMessageBox)

from interfaz.ep import EditaPorcentaje
from models.clientes import ClienteModel
from models.registros_model import RegistroModel
from models.reparacion_model import ReparacionModel
from models.usarios import UsuariosModel
from recursos import recursos_rc
from recursos.reportes.genera_reporte import GeneraReporte


class EntregasController:
    def __init__(self, view):
        self.cvprin = view
        self.vprin = self.cvprin.ui
        self.indrep = 0
        self.propred = 50  # porcentaje del tecnico predeterminado
        self._conectarEventos()

    def _conectarEventos(self):
        # Entregas------------------------------------------------------------------------------------------------------
        self.vprin.diagnosticoe.textChanged.connect(self.cvprin.cambio_en_ent)
        self.vprin.tecnicoe.activated.connect(self.cvprin.cambio_en_ent)
        self.vprin.repuestose.itemChanged.connect(self.cvprin.cambio_en_ent)
        self.vprin.totale.valueChanged.connect(self.cvprin.cambio_en_ent)
        self.vprin.servtece.valueChanged.connect(self.cvprin.cambio_en_ent)
        self.vprin.garantiae.valueChanged.connect(self.cvprin.cambio_en_ent)
        self.vprin.fecharepe.dateTimeChanged.connect(self.cvprin.cambio_en_ent)
        self.vprin.fechaentrega.dateTimeChanged.connect(self.cvprin.cambio_en_ent)
        self.vprin.pagppend.toggled.connect(self.cvprin.cambio_en_ent)
        self.modelentregas = QStandardItemModel()
        self.vprin.listaentregas.setModel(self.modelentregas)
        self.vprin.listaentregas.clicked.connect(self.entregar)
        self.vprin.fecharepe.dateTimeChanged.connect(self.cambio_fechae)
        self.vprin.entregas.tabBarClicked.connect(self.cvprin.comprueba_cambio)
        self.vprin.entregas.tabBarClicked.connect(self.entrega)
        self.vprin.repuestose.cellChanged.connect(self.cambiorepuestose)
        self.vprin.anadire.clicked.connect(self.nuevo_repuestoe)
        self.vprin.btneliminarepe.clicked.connect(self.eliminar_repuestoe)
        self.vprin.totale.valueChanged.connect(self.calcula_servtece)
        self.vprin.garantiae.valueChanged.connect(self.garantiafeche)
        self.vprin.btneditaporce.clicked.connect(self.edita_porcentaje)
        self.vprin.btnimprimir_e.clicked.connect(self.eimprimir)
        self.vprin.btnguardare.clicked.connect(self.guardar)
        self.vprin.servtece.valueChanged.connect(self.calcula_costoe)

        # ---------------------------------------------------------------------------------------------------------------

    # ---Entregas --------------------------------------------------------------------------------
    def entrega(self):
        self.vprin.stack.setCurrentIndex(3)
        self.lista_entregas()
        self.vprin.entregas.setTabEnabled(1, False)

    def garantiafeche(self, dias):
        self.fh = self.vprin.fecharepe.dateTime()
        fechgar = self.fh.addDays(dias)
        self.vprin.fechagarantiae.setText(fechgar.toString("dd/MM/yyyy hh:mm:ss"))

    def cambio_fechae(self):
        self.vprin.fecha_repe.setText(self.vprin.fecharepe.dateTime().toString('dd/MM/yyyy hh:mm:ss ap'))

    def carga_tecnicos(self):
        res = UsuariosModel().obtener_tecnicos()
        self.vprin.tecnicoe.clear()
        for opcion in res:
            self.vprin.tecnicoe.addItem(opcion[1], opcion[0])
        self.vprin.tecnicoe.insertItem(0, "")

    def lista_entregas(self):

        datos = ReparacionModel().obtener_entregas()

        self.modelentregas.clear()

        for item_data in datos:
            rep_id, reg_id, equipo, marca, modelo, serie, cliente, telefono, costo = item_data

            item = QStandardItem(
                f"{equipo.upper()if equipo else ""}\n{marca.upper() if marca else ""}\nModelo: {modelo}\nSerie: {serie}\n\n{cliente}\n📞{telefono}\n\nPrecio: ${costo}"
            )

            item.setIcon(QIcon(":/iconos/iconos/electronicos.png"))
            item.setFont(QFont("Arial", 11, QFont.Weight.DemiBold))
            item.setData(rep_id, Qt.ItemDataRole.UserRole)

            self.modelentregas.appendRow(item)

    def entregar(self, index):
        self.carga_tecnicos()
        self.vprin.entregas.setTabEnabled(1, True)
        self.vprin.entregas.setCurrentIndex(1)
        self.vprin.fecha_rep.setText('')
        self.vprin.garantiae.setValue(0)
        idreg = index.data(Qt.ItemDataRole.UserRole)
        self.imp = ReparacionModel().obtener_por_reg(idreg)
        rep = self.imp[:8]
        self.vprin.fechagarantiae.clear()
        self.vprin.diagnosticoe.blockSignals(True)
        self.vprin.diagnosticoe.setPlainText(rep[3])
        self.vprin.diagnosticoe.blockSignals(False)
        repuestos = eval(rep[4])
        self.vprin.repuestose.setRowCount(0)
        for i in range(len(repuestos) - 1):
            self.vprin.repuestose.insertRow(i)
            self.vprin.repuestose.setItem(i, 0, QTableWidgetItem(repuestos[i][0]))
            item = QTableWidgetItem(repuestos[i][1])
            item.setTextAlignment(Qt.AlignmentFlag.AlignRight)
            self.vprin.repuestose.setItem(i, 1, item)
        self.vprin.tecnicoe.blockSignals(True)
        indice = self.vprin.tecnicoe.findData(rep[7], role=Qt.ItemDataRole.UserRole)
        if indice != -1:
            self.vprin.tecnicoe.setCurrentIndex(indice)
        else:
            self.vprin.tecnicoe.setCurrentIndex(0)
        self.vprin.tecnicoe.blockSignals(False)
        self.vprin.totale.setValue(rep[2] if rep[2] else 0.00)
        if rep[5]:
            self.vprin.fecharepe.setDateTime(QDateTime().fromString(rep[5], 'dd/MM/yyyy hh:mm:ss ap'))
        self.vprin.garantiae.setValue(int(rep[6]) if rep[6] else 0)
        self.vprin.pagppend.setChecked(rep[7] if rep[7] else False)
        self.vprin.fechaentrega.blockSignals(True)
        self.vprin.fechaentrega.setDateTime(QDateTime().currentDateTime())
        self.vprin.fechaentrega.setMaximumDateTime(QDateTime().currentDateTime())
        self.vprin.fechaentrega.blockSignals(False)
        self.cvprin.cambioent = False

    def cambiorepuestose(self, fila, colum):
        self.vprin.repuestose.blockSignals(True)
        self.vprin.porcentaje.setText(str(self.propred))
        if colum:
            precio = 0
            for i in range(self.vprin.repuestose.rowCount()):
                try:
                    p = re.findall(r"\d+\.?\d*", self.vprin.repuestose.item(i, 1).text())[0]
                    precio += float(p)
                    if i == fila:
                        item = QTableWidgetItem("$" + p)
                        item.setTextAlignment(Qt.AlignmentFlag.AlignRight)
                        self.vprin.repuestose.setItem(fila, colum, item)
                except Exception as e:
                    item = QTableWidgetItem("$0.0")
                    item.setTextAlignment(Qt.AlignmentFlag.AlignRight)
                    self.vprin.repuestos.setItem(fila, colum, item)
            self.vprin.totalrepe.setText(str(precio))
            self.calcula_costoe()
        self.vprin.repuestose.blockSignals(False)

    def nuevo_repuestoe(self):
        self.vprin.repuestose.blockSignals(True)
        nfil = self.vprin.repuestose.rowCount()
        self.vprin.repuestose.insertRow(nfil)
        self.vprin.repuestose.setItem(nfil, 0, QTableWidgetItem('pendiente'))
        item = QTableWidgetItem('$0')
        item.setTextAlignment(Qt.AlignmentFlag.AlignRight)
        self.vprin.repuestose.setItem(nfil, 1, item)
        self.vprin.repuestose.blockSignals(False)

    def eliminar_repuestoe(self):
        fila = self.vprin.repuestose.currentRow()
        self.vprin.repuestose.removeRow(fila)

    def calcula_costoe(self):
        total = float(self.vprin.totalrepe.text()) + self.vprin.servtece.value()
        self.vprin.totale.setValue(total)


    def calcula_servtece(self):
        self.vprin.servtece.blockSignals(True)
        servtec = self.vprin.totale.value() - float(self.vprin.totalrepe.text())
        self.vprin.servtece.setValue(servtec)
        self.vprin.servtece.blockSignals(False)

    def edita_porcentaje(self):
        self.ui_edip = EditaPorcentaje(self.cvprin)
        self.ui_edip.exec()


    def guardar(self):
        self.vprin.statusbar.showMessage('Guardando........', 1000)
        tecnico = self.vprin.tecnicoe.currentData()
        diagnostico = self.vprin.diagnosticoe.toPlainText()
        repuestos = []
        for i in range(self.vprin.repuestos.rowCount()):
            rep = self.vprin.repuestose.item(i, 0).text()
            preci = self.vprin.repuestose.item(i, 1).text()
            repuestos.append((rep, preci))
        repuestos.append(self.vprin.totalrep.text())
        costot = self.vprin.totale.value()
        regi = RegistroModel()
        repa = ReparacionModel()
        idrep = int(self.vprin.listaentregas.currentIndex().data(Qt.ItemDataRole.UserRole))
        conti = QMessageBox.question(
                self.cvprin,
                "Martin Electronic's",
                f"Usted esta entregando el equipo con la fecha: {self.vprin.fechaentrega.dateTime().toString("dd/MM/yyyy hh:mm")}'\n"
                "¿Desea continuar?",
                QMessageBox.StandardButton.Ok | QMessageBox.StandardButton.Cancel
            )
        if conti == QMessageBox.StandardButton.Cancel:
            return None
        regi.actualizar_estatus(rep_id=idrep, estatus="Completado", fe=self.vprin.fechaentrega.dateTime().toString("dd/MM/yyyy hh:mm ap "))
        repa.actualizar(idrep, (tecnico, self.vprin.fecha_repe.text(), costot, diagnostico, f"{repuestos}",
                                self.vprin.garantiae.value(), self.vprin.pagppend.isChecked(), True, int(self.vprin.porcentaje.text()), self.vprin.servtece.value()))
        self.cvprin.cambioent = False
        msj = 'Entrega guardada correctamente...'
        QTimer.singleShot(500, lambda: self.vprin.statusbar.showMessage(msj, 3000))

    def eimprimir(self):
        client = ClienteModel().obtener_por_id(self.imp[1])
        datos = {"cliente": client, "equipo": self.imp, "reparacion": self.imp[1:8],
                 "fecha": datetime.now().strftime('%d/%m/%Y  %I:%M:%S %p'), "user":self.cvprin.user}
        GeneraReporte(datos, self.cvprin).reporte_de_salida()