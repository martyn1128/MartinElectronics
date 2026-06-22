from PySide6.QtCharts import QPieSeries, QChart, QChartView
from PySide6.QtCore import QMargins
from PySide6.QtGui import QStandardItem, QColor, QIcon, QFont, Qt, QStandardItemModel, QPainter
from PySide6.QtSql import QSqlQueryModel
from PySide6.QtWidgets import QMessageBox

from models.clientes import ClienteModel
from models.equipos import EquipoModel
from models.qt_db import QtDB
from models.registros_model import RegistroModel
from models.reparacion_model import ReparacionModel
from models.usarios import UsuariosModel


class InicioController:
    def __init__(self, view):
        self.cvprin = view
        self.vprin = self.cvprin.ui
        self.vprin.usuario.setText(self.cvprin.user[1])
        self._conectareventos()

    def _conectareventos(self):
        self.modelclientes = QStandardItemModel()
        self.vprin.listView_3.setModel(self.modelclientes)
        self.modeltec = QStandardItemModel()
        self.vprin.listView_4.setModel(self.modeltec)
        self.modelpconf = QSqlQueryModel()
        self.vprin.tablaconf.setModel(self.modelpconf)
        self.vprin.btnconfirmarpre.clicked.connect(self.confirmapresup)

    def iniciom(self):
        self.vprin.stack.setCurrentIndex(0)
        self.vprin.totalreg.setText(str(RegistroModel().numero()[0]))
        clientes = ClienteModel()
        self.vprin.totalclientes.setText(str(clientes.numero()[0]))
        self.vprin.teet.setText(str(EquipoModel().equipos_en_taller()[0]))
        rep = ReparacionModel()
        self.vprin.pendrep.setText(str(rep.pend_rep()[0]))
        self.vprin.pendconf.setText(str(rep.pend_conf()[0]))
        self.vprin.pendrev.setText(str(rep.pend_rev()[0]))
        self.top_clientes(clientes)
        self.top_tecnicos()
        self.grafica()
        self.tabla_pend_conf()

    def top_clientes(self, clientes):
        client = clientes.top_clientes()
        TOP_COLORS = {
            0: "#8C7333",  # Oro Envejecido (Oscurecido)
            1: "#5E6266",  # Plata Oxidada / Plomo
            2: "#6B3E26",  # Bronce Quemado
            3: "#243036",  # Carbón Azulado (Muy oscuro)
            4: "#0D1317"  # Negro Profundo (Apenas visible)
        }
        medallas = ["🥇", "🥈", "🥉", "👤", "👤"]
        self.modelclientes.clear()
        for i in range(len(client)):
            item = QStandardItem(f"{medallas[i]} {client[i][1]}\n Equipos:{client[i][2]}")
            item.setBackground(QColor(12, 60, 106, 140))
            item.setIcon(QIcon(':/iconos/iconos/person_user.ico'))
            item.setFont(QFont("Arial", 11, QFont.Weight.DemiBold))
            item.setData(client[i][0], Qt.ItemDataRole.UserRole)
            self.modelclientes.appendRow(item)

    def top_tecnicos(self):
        tec = UsuariosModel().top_tecnicos()
        TOP_COLORS = {
            0: "#E0AF41",  # Oro Envejecido (Oscurecido)
            1: "#8D8E96",  # Plata Oxidada / Plomo
            2: "#A1684F",  # Bronce Quemado
            3: "#243036",  # Carbón Azulado (Muy oscuro)
            4: "#0D1317"  # Negro Profundo (Apenas visible)
        }
        medallas = ["🥇", "🥈", "🥉", "👤", "👤"]
        self.modeltec.clear()
        for i in range(len(tec)):
            item = QStandardItem(f"{medallas[i]} {tec[i][1]}\n Reparaciones:{tec[i][2]}")
            item.setBackground(QColor(12, 60, 106, 140))
            item.setIcon(QIcon(':/iconos/iconos/mecanico.ico'))
            item.setFont(QFont("Arial", 11, QFont.Weight.DemiBold))
            item.setData(tec[i][0], Qt.ItemDataRole.UserRole)
            self.modeltec.appendRow(item)

    def grafica(self):
        # 1. Crear la serie de datos
        series = QPieSeries()
        series.setHoleSize(0.50)
        # 2. Agregar los datos (Rangos de entrega)
        # Usamos los colores oscuros/metálicos que definimos antes
        res = RegistroModel().entregas()
        if res:
            # 1. Rápido (Índice 0)
            slice_rapido = series.append(res[0][0], res[0][1])
            slice_rapido.setBrush(QColor("#FFED61"))
            slice_rapido.setLabelVisible(True)
            # Mostramos el nombre y el porcentaje con 1 decimal
            slice_rapido.setLabel(f"{slice_rapido.label()}:  {res[0][1]}")

            if len(res) > 1:
                # 2. Medio (Índice 1)
                slice_medio = series.append(res[1][0], res[1][1])
                slice_medio.setBrush(QColor("#09F687"))
                slice_medio.setLabelVisible(True)
                slice_medio.setLabel(f"{slice_medio.label()}:  {res[1][1]}")

                if len(res) > 2:
                    # 3. Tarde (Índice 2)
                    slice_tarde = series.append(res[2][0], res[2][1])
                    slice_tarde.setBrush(QColor("#FF6161"))
                    slice_tarde.setExploded(True)
                    slice_tarde.setLabelVisible(True)
                    slice_tarde.setLabel(f"{slice_tarde.label()}:  {res[2][1]}")

        # 4. Configurar el Chart
        chart = QChart()
        chart.addSeries(series)
        #chart.setTitle("Tiempos de Entrega")
        chart.setAnimationOptions(QChart.SeriesAnimations)  # Animación suave al cargar
        chart.setBackgroundVisible(False)  # Para que se integre con tu modo oscuro
        #chart.legend().hide()
        chart.setMargins(QMargins(10, 0, 10, 20))
        # 5. El View (Donde se dibuja)
        self.vprin.graficai.setRenderHint(QPainter.Antialiasing)  # Suaviza los bordes
        self.vprin.graficai.setChart(chart)
        self.vprin.graficai.setMinimumSize(300,300)
        self.vprin.graficai.setMaximumSize(600, 600)
        #self.vprin.graficai.resize(600, 600)

        series.hovered.connect(self.on_slice_hovered)

    def on_slice_hovered(self, slice, state):
        slice.setExploded(state)
        slice.setLabelVisible(state)

    def tabla_pend_conf(self):
        self.cvprin.conecta()
        self.modelpconf.setQuery(ReparacionModel().query_pconf(), self.cvprin.conexion)

    def confirmapresup(self):
        reg = [i.data() for i in self.vprin.tablaconf.selectedIndexes()]
        if reg:
            save = QMessageBox.question(self.cvprin, "Martin Electronics's",
                                        f"Confirma que se acepto el presupuesto de: \n Equipo: {reg[5]}\n Marca: {reg[6]} \n Modelo: {reg[7]} \n Diagnostico: {reg[2]} \n Total: ${reg[1]} \n¿DESEA CONTINUAR?")
            if save == QMessageBox.StandardButton.Yes:
                ReparacionModel().autorizar(reg[13])
            else:
                pass
            self.iniciom()