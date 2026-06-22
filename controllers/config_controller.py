import os
import time

from PySide6.QtCore import QTimer
from PySide6.QtGui import QPixmap, QIcon, Qt
from PySide6.QtWidgets import QFileDialog, QPushButton, QLabel, QVBoxLayout, QDialog, QMessageBox, QApplication

from models.empresa import EmpresaModel


class ConfigController:
    def __init__(self, view):
        self.cvprin = view
        self.vprin = self.cvprin.ui
        self._conectareventos()

    def _conectareventos(self):
        self.vprin.nombreemp.textEdited.connect(self.cvprin.cambio_en_emp)
        self.vprin.direccionemp.textEdited.connect(self.cvprin.cambio_en_emp)
        self.vprin.tel1emp.textEdited.connect(self.cvprin.cambio_en_emp)
        self.vprin.tel2emp.textEdited.connect(self.cvprin.cambio_en_emp)
        self.vprin.pagweb.textEdited.connect(self.cvprin.cambio_en_emp)
        self.vprin.emailemp.textEdited.connect(self.cvprin.cambio_en_emp)
        self.vprin.notaent.textChanged.connect(self.cvprin.cambio_en_emp)
        self.vprin.notasal.textChanged.connect(self.cvprin.cambio_en_emp)
        self.vprin.listWidget.currentItemChanged.connect(self.cvprin.comprueba_cambio)
        self.vprin.listWidget.currentItemChanged.connect(self.cambiomenu)
        self.vprin.selarch.clicked.connect(self.seleccimagen)
        self.vprin.btnguardainfo.clicked.connect(self.guardar)
        self.vprin.cprep.clicked.connect(self.import_cprep)

    def config(self):
        self.vprin.stack.setCurrentIndex(6)
        self.vprin.listWidget.setCurrentRow(0)

    def cambiomenu(self):
        index = self.vprin.listWidget.currentRow()
        if index == 1:
            self.rellenainfo()
        if index < 3:
            self.vprin.stackedWidget.setCurrentIndex(index)
        else:
            self.mostrar_acerca_de()

    def rellenainfo(self):
        inf = EmpresaModel().informacion()
        self.vprin.notaent.blockSignals(True)
        self.vprin.notasal.blockSignals(True)
        self.vprin.nombreemp.setText('')
        self.vprin.direccionemp.setText('')
        self.vprin.tel1emp.setText('')
        self.vprin.tel2emp.setText('')
        self.vprin.pagweb.setText('')
        self.vprin.emailemp.setText('')
        self.vprin.notaent.setText('')
        self.vprin.notasal.setText('')
        if inf:
            self.vprin.nombreemp.setText(inf[1])
            self.vprin.direccionemp.setText(inf[2])
            self.vprin.tel1emp.setText(inf[3])
            self.vprin.tel2emp.setText(inf[4])
            self.vprin.pagweb.setText(inf[5])
            self.vprin.emailemp.setText(inf[6])
            pix = QPixmap()
            pix.loadFromData(inf[7])
            self.vprin.logo.setPixmap(pix.scaled(180,180))
            self.vprin.notaent.setText(inf[8])
            self.vprin.notasal.setText(inf[9])
        self.vprin.notasal.blockSignals(False)
        self.vprin.notaent.blockSignals(False)

    def seleccimagen(self):
        ruta, _ = QFileDialog.getOpenFileName(
            self.cvprin,
            "Seleccionar Logo",
            "",
            "Images (*.png *.jpg *.jpeg *.ico)"
        )

        if ruta:
            self.cvprin.cambio_en_emp()
            self.vprin.logo.setPixmap(QPixmap(ruta))
            self.vprin.logo.setToolTip(ruta)

    def guardar(self):
        nom = self.vprin.nombreemp.text()
        dir = self.vprin.direccionemp.text()
        t1 = self.vprin.tel1emp.text()
        t2 = self.vprin.tel2emp.text()
        pw = self.vprin.pagweb.text()
        em = self.vprin.emailemp.text()
        n1 = self.vprin.notaent.toPlainText()
        n2 = self.vprin.notasal.toPlainText()
        EmpresaModel().actualiza(nom, dir, t1, t2, pw, em, n1, n2)

        if self.vprin.logo.toolTip():
            with open(self.vprin.logo.toolTip(), "rb") as log:
                img = log.read()
            EmpresaModel().actualiza_logo(img)
        self.cvprin.cambioemp = False

    def import_cprep(self):
        ruta, _ = QFileDialog.getOpenFileName(
            self.cvprin,
            "Seleccionar Base de datos de CP Reparaciones",
            "",
            "BD (*.mdb)"
        )

        if not ruta:
            return

        from models.migrador import MigradorAccess

        migrador = MigradorAccess(ruta, os.path.join(os.getenv('APPDATA'),'Martin Electronics/data/me.db'))

        # 🔹 modo "cargando" (indeterminado)
        self.vprin.progressBar.setMaximum(100)
        self.vprin.progressBar.setValue(0)
        self.vprin.stackedprogres.setCurrentIndex(1)

        QApplication.processEvents()  # 🔥 refresca UI
        for i in range(0, 50, 2):
            self.vprin.progressBar.setValue(i)
            time.sleep(0.05)

        try:
            total, clientes, equipos = migrador.migrar_identificacion()

            # 🔹 terminar barra
            for i in range(50, 100, 1):
                self.vprin.progressBar.setValue(i)
                time.sleep(0.001)
            self.vprin.progressBar.setValue(100)

            QMessageBox.information(
                self.cvprin,
                "Migración completada",
                f"""La importación terminó correctamente:
                
    • Registros migrados: {total}
    • Clientes nuevos: {clientes}
    • Equipos creados: {equipos}
                    """
                )

        except Exception as e:
            QMessageBox.critical(
                self.cvprin,
                "Error",
                f"Ocurrió un error:\n{e} \n intente reiniciar la app y vuelva a intentarlo..."
            )

        finally:
            # 🔹 reset barra
            self.vprin.progressBar.setMaximum(100)
            self.vprin.progressBar.setValue(0)
            self.vprin.stackedprogres.setCurrentIndex(0)

    def actualizar_progreso(self, valor):
        self.vprin.progressBar.setValue(valor)

    def migracion_terminada(self, total, clientes, equipos):

        self.vprin.progressBar.setValue(self.vprin.progressBar.maximum())

        QMessageBox.information(
            self.cvprin,
            "Migración completada",
            f"""La importación terminó correctamente:

                • Registros migrados: {total}
                • Clientes nuevos: {clientes}
                • Equipos creados: {equipos}
                """
                    )
        #self.thread.quit()
        #self.worker.deleteLater()

    def mostrar_acerca_de(self):
        # 1. Crear el diálogo
        dialogo = QDialog(self.cvprin)
        dialogo.setWindowTitle("Acerca de Martin Electronic's")
        dialogo.setFixedSize(400, 500)

        layout = QVBoxLayout()

        # 2. Agregar Logo
        label_logo = QLabel()
        icono_temp = QIcon(":/iconos/iconos/acerca-de.png")
        label_logo.setPixmap(icono_temp.pixmap(200, 200))
        label_logo.setAlignment(Qt.AlignCenter)
        layout.addWidget(label_logo)

        # 3. Agregar Texto Informativo
        label_texto = QLabel("""
    <div style='text-align: center;'>
        <h1 style='color: #0C3C6A;'>Martin Electronics</h1>
        <p style='font-size: 12pt; color: #3c91c7'>Gestión de taller de Electrónica</p>
        <hr>
        <p><b>Desarrollado Por:</b></p>
        <ul style='list-style-type: none; padding: 0; text-align: left;'>
            <li style='margin-left: 60px;'>👤 <i>Luis Martin Lopez Montes</i></li>
        </ul>
        <p style='color: #7f8c8d; font-size: 9pt; '>Version: 1.1</p>
        <p style='color: #7f8c8d; font-size: 9pt;'>2026 © Todos los derechos reservados</p>
        <p style='color: #7f8c8d; font-size: 9pt;'>Instituto Tecnológico de Jiquilpan</p>
    </div>"""
        )
        label_texto.setOpenExternalLinks(True)
        layout.addWidget(label_texto)

        # 4. Botón de cerrar
        btn_cerrar = QPushButton("Cerrar")
        btn_cerrar.clicked.connect(dialogo.accept)
        layout.addWidget(btn_cerrar)

        dialogo.setLayout(layout)
        dialogo.exec()  # Muestra la ventana de forma modal
        self.vprin.btnconfig.animateClick()