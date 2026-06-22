from PySide6.QtCharts import QLineSeries, QChart, QChartView, QValueAxis
from PySide6.QtCore import QDateTime, QSortFilterProxyModel, Qt, QMargins
from PySide6.QtGui import QPainter, QPen, QColor
from PySide6.QtSql import QSqlQueryModel
from PySide6.QtWidgets import QTableView

from models.pago_model import PagoModel
from models.qt_db import QtDB
from models.reparacion_model import ReparacionModel
from models.usarios import UsuariosModel


class PagoController:
    def __init__(self, view):
        self.cvprin = view
        self.vprin = self.cvprin.ui

        self.anios_disponibles = []
        self.indice_anio_actual = 0
        self.tecnico_actual_id = None  # Asegúrate de asignarlo cuando cargues al técnico
        self._conectareventos()

    def _conectareventos(self):
        self.vprin.grafica2.setStyleSheet("""
                            background-color: transparent;
                            border: none;
                        """)
        self.vprin.grafica3.setStyleSheet("""
                            background-color: transparent;
                            border: none;
                        """)
        self.crear_grafica2()
        self.crear_grafica3()
        self.carga_tecnicos()
        self.vprin.fechape_1.setDateTime(QDateTime().currentDateTime())
        self.vprin.fechape_1.setMaximumDateTime(QDateTime().currentDateTime())
        self.vprin.fechape_2.setDateTime(QDateTime().currentDateTime())
        self.vprin.fechape_2.setMaximumDateTime(QDateTime().currentDateTime())
        self.vprin.fechape_1.dateChanged.connect(self.cambio_fecha1)
        self.vprin.fechape_2.dateChanged.connect(self.cambio_fecha2)
        self.modelpagos = QSqlQueryModel()
        self.busq = QSortFilterProxyModel(self.cvprin)
        self.busq.setSourceModel(self.modelpagos)
        self.busq.setFilterCaseSensitivity(Qt.CaseSensitivity.CaseInsensitive)
        self.busq.setFilterKeyColumn(-1)
        self.vprin.buscarp.textChanged.connect(self.busca)
        self.vprin.tablapagos.setModel(self.busq)
        self.vprin.tablapagos.setSelectionBehavior(QTableView.SelectRows)
        self.vprin.tablapagos.setSelectionMode(QTableView.MultiSelection)
        self.vprin.tecnico_p.currentIndexChanged.connect(self.tabla_pago)

        self.vprin.btnlimpiar.clicked.connect(self.limpiar)
        self.vprin.seleccp.toggled.connect(self.seleccionar_todo)
        self.vprin.tablapagos.selectionModel().selectionChanged.connect(self.on_selection_changed)

        self.vprin.btncambiografica.clicked.connect(self.siguiente_anio)
        self.vprin.btnautorizap.clicked.connect(self.pagos_autorizados)


    def pago(self):
        self.vprin.stack.setCurrentIndex(5)

    def carga_tecnicos(self):
        res = UsuariosModel().obtener_tecnicos()
        self.vprin.tecnico_p.clear()
        for opcion in res:
            self.vprin.tecnico_p.addItem(opcion[1], opcion[0])
        self.vprin.tecnico_p.insertItem(0, "")

    def cambio_fecha1(self):
        self.vprin.fechap_1.setText(self.vprin.fechape_1.dateTime().toString('dd/MM/yyyy HH:mm:ss'))
        self.vprin.fechape_2.setMinimumDateTime(self.vprin.fechape_1.dateTime())
        self.tabla_pago()

    def cambio_fecha2(self):
        self.vprin.fechap_2.setText(self.vprin.fechape_2.dateTime().toString('dd/MM/yyyy HH:mm:ss'))
        self.vprin.fechape_1.setMaximumDateTime(self.vprin.fechape_2.dateTime())
        self.tabla_pago()

    def tabla_pago(self):
        f1 = self.vprin.fechap_1.text()
        f2 = self.vprin.fechap_2.text()
        idt = self.vprin.tecnico_p.currentData()
        self.cvprin.conecta()
        self.modelpagos.setQuery(PagoModel().query_pagos(f1=f1, f2=f2, id_tecnico=idt), self.cvprin.conexion)
        self.crear_grafica_1(idt)


    def busca(self, cad):
        self.busq.setFilterFixedString(cad)
        if self.vprin.buscarreg.text():
            self.vprin.msjp.setText('Resultados:')
        else:
            self.vprin.msjp.setText('Todos los registros:')

    def limpiar(self):
        ahora = QDateTime.currentDateTime()

        # reset fechas
        self.vprin.fechape_1.setDateTime(ahora)
        self.vprin.fechape_2.setDateTime(ahora)

        # quitar restricción
        self.vprin.fechape_1.setMaximumDateTime(QDateTime())
        dt = QDateTime.fromString('01/01/2000', 'dd/MM/yyyy')
        self.vprin.fechape_2.setMinimumDateTime(dt)

        # limpiar texto
        self.vprin.fechap_1.clear()
        self.vprin.fechap_2.clear()
        self.tabla_pago()

    def seleccionar_todo(self, checked):
        if checked:
            self.vprin.tablapagos.selectAll()
        else:
            self.vprin.tablapagos.clearSelection()

    def on_selection_changed(self):
        tabla = self.vprin.tablapagos
        modelo = tabla.model()

        if not modelo:
            return

        total_filas = modelo.rowCount()
        seleccionadas = tabla.selectionModel().selectedRows()

        # bloquear señal para evitar bucle infinito
        self.vprin.seleccp.blockSignals(True)

        if len(seleccionadas) == total_filas and total_filas > 0:
            self.vprin.seleccp.setChecked(True)
        else:
            self.vprin.seleccp.setChecked(False)

        self.vprin.seleccp.blockSignals(False)

        total = 0
        modelo = self.vprin.tablapagos.model()
        for index in seleccionadas:
            fila = index.row()
            total += float(modelo.index(fila, 1).data())*(float(modelo.index(fila, 2).data())/100)
        self.vprin.total_p.setText(str(total))

    '''def crear_grafica_1(self, tecnico_id):

        # Datos (ejemplo)
        dat = PagoModel().promedio_por_mes(tecnico_id)
        datos = []
        for año, mes, valor in dat:
            if mes:
                datos.append((mes,valor))

        # Serie
        serie = QLineSeries()
        for mes, valor in datos:
            serie.append(mes, valor)

        # Promedio total
        promedio_total = sum(valor for _, valor in datos) / len(datos)

        # Mostrar en QLabel (ajusta el nombre)
        self.vprin.labelPromedio.setText(f"${promedio_total:,.0f}")

        #Estilo de línea moderno
        pen = QPen(QColor("#00C853"))  # verde pro
        pen.setWidth(3)
        serie.setPen(pen)
        serie.setPointsVisible(False)

        #Chart
        chart = QChart()
        chart.addSeries(serie)

        chart.legend().hide()
        chart.setBackgroundVisible(False)
        chart.setMargins(QMargins(0, 0, 0, 0))
        chart.setTitle("")
        chart.setAnimationOptions(QChart.SeriesAnimations)

        #Ejes limpios
        axisX = QValueAxis()
        axisX.setRange(1, 12)
        axisX.setLabelFormat("%d")
        axisX.setGridLineVisible(False)
        axisX.setLabelsColor(Qt.gray)

        axisY = QValueAxis()
        axisY.setLabelsColor(Qt.gray)
        axisY.setGridLineVisible(True)

        chart.addAxis(axisX, Qt.AlignBottom)
        chart.addAxis(axisY, Qt.AlignLeft)

        serie.attachAxis(axisX)
        serie.attachAxis(axisY)

        #Estilo del widget
        self.vprin.grafica1.setStyleSheet("""
            background-color: transparent;
            border: none;
        """)

        self.vprin.grafica1.setRenderHint(QPainter.Antialiasing)
        self.vprin.grafica1.setChart(chart)
        self.vprin.grafica1.setFixedSize(300, 150)
        if datos[-1][1] > datos[0][1]:
            self.vprin.labelPromedio.setStyleSheet("color: #00C853; font-size: 16px; font-weight: bold;")
        else:
            self.vprin.labelPromedio.setStyleSheet("color: #D50000; font-size: 16px; font-weight: bold;")
'''
    def crear_grafica2(self):
        self.vprin.grafica2.setChart(QChart())

        self.vprin.grafica2.chart().setBackgroundVisible(False)


    def crear_grafica3(self):
        self.vprin.grafica3.setChart(QChart())
        self.vprin.grafica3.chart().setBackgroundVisible(False)


    def siguiente_anio(self):
        """Hace avanzar el año y redibuja la gráfica"""
        if not self.anios_disponibles:
            return

        # Aumentar el índice y resetear a 0 si llegamos al final (Lógica Cíclica)
        self.indice_anio_actual += 1
        if self.indice_anio_actual >= len(self.anios_disponibles):
            self.indice_anio_actual = 0

        anio_a_mostrar = self.anios_disponibles[self.indice_anio_actual]

        # Actualizar el texto del botón o un label para que el usuario sepa qué año ve
        self.vprin.labely.setText(f"Año: {anio_a_mostrar}")

        # Llamar a la función de dibujo
        self.crear_grafica_1(self.tecnico_actual_id, anio_a_mostrar)

    def crear_grafica_1(self, tecnico_id, anio_objetivo=None):
        """
        Crea una gráfica de líneas para un técnico y año específicos.
        Si anio_objetivo es None, intenta usar el índice actual del ciclo de años.
        """
        # 1. Obtener todos los datos del modelo
        # Se espera: [(anio, mes, valor), (anio, mes, valor), ...]
        dat = PagoModel().promedio_por_mes(tecnico_id)
        self.tecnico_actual_id = tecnico_id

        if not dat:
            self.vprin.labelPromedio.setText("$0")
            return

        # 2. Gestionar la lista de años disponibles (Solo si la lista está vacía)
        if not self.anios_disponibles:
            # Extraemos años únicos, los convertimos a string y ordenamos
            self.anios_disponibles = sorted(list(set(str(f[0]) for f in dat if f[0])))
            self.indice_anio_actual = 0  # Empezar por el primer año encontrado

        # 3. Determinar qué año mostrar
        if anio_objetivo is None and self.anios_disponibles:
            anio_objetivo = self.anios_disponibles[self.indice_anio_actual]

        # Actualizar texto del botón para feedback del usuario
        if hasattr(self.vprin, 'btnCambiarAnio'):
            self.vprin.btnCambiarAnio.setText(f"Año: {anio_objetivo}")

        # 4. Filtrar y preparar los datos del año seleccionado
        # Importante: Usamos float() para evitar errores de tipos en el gráfico
        datos_filtrados = []
        for anio, mes, valor in dat:
            if str(anio) == str(anio_objetivo) and mes:
                datos_filtrados.append((int(mes), float(valor)))

        # Ordenamos por mes para que la línea no se cruce
        datos_filtrados.sort()

        if not datos_filtrados:
            return

        # 5. Crear la Serie de datos
        serie = QLineSeries()
        for mes, valor in datos_filtrados:
            serie.append(mes, valor)

        # 6. Cálculo de Promedio y Lógica de Color (Tendencia)
        total_valores = [v for m, v in datos_filtrados]
        promedio_total = sum(total_valores) / len(total_valores)
        self.vprin.labelPromedio.setText(f"${promedio_total:,.0f}")

        # Definir color: Verde si el último mes >= primer mes del año, si no Rojo
        color_hex = "#00C853" if total_valores[-1] >= total_valores[0] else "#D50000"

        # Aplicar estilo al Label del Promedio
        self.vprin.labelPromedio.setStyleSheet(f"color: {color_hex}; font-size: 16px; font-weight: bold;")

        # Estilo de la línea del gráfico
        pen = QPen(QColor(color_hex))
        pen.setWidth(3)
        serie.setPen(pen)
        serie.setPointsVisible(True)  # Opcional: muestra puntos en cada mes

        # 7. Configuración del Chart (Lienzo)
        chart = QChart()
        chart.addSeries(serie)
        chart.legend().hide()
        chart.setBackgroundVisible(False)
        chart.setMargins(QMargins(10, 10, 10, 10))
        chart.setAnimationOptions(QChart.SeriesAnimations)

        # 8. Configuración de Ejes
        # Eje X: Meses del 1 al 12
        axisX = QValueAxis()
        axisX.setRange(1, 12)
        axisX.setTickCount(12)
        axisX.setLabelFormat("%d")
        axisX.setGridLineVisible(False)
        axisX.setLabelsColor(QColor("gray"))

        # Eje Y: Valores monetarios
        axisY = QValueAxis()
        axisY.setLabelsColor(QColor("gray"))
        axisY.setGridLineVisible(True)
        # Ajuste dinámico del rango Y para que no se corte la línea
        if total_valores:
            max_y = max(total_valores) * 1.2
            axisY.setRange(0, max_y)

        # Vincular ejes
        chart.addAxis(axisX, Qt.AlignBottom)
        chart.addAxis(axisY, Qt.AlignLeft)
        serie.attachAxis(axisX)
        serie.attachAxis(axisY)

        # 9. Renderizado final en el QChartView
        self.vprin.grafica1.setChart(chart)
        self.vprin.grafica1.setRenderHint(QPainter.Antialiasing)
        self.vprin.grafica1.setFixedSize(310, 150)

        # Estilo del contenedor
        self.vprin.grafica1.setStyleSheet("background-color: transparent; border: none;")

    def pagos_autorizados(self):
        # 1. Obtener los índices seleccionados (son objetos QModelIndex)
        indices = self.vprin.tablapagos.selectedIndexes()

        if not indices:
            print("No hay nada seleccionado.")
            return

        # 2. Extraer solo los números de fila únicos
        # Usamos un set para no repetir el proceso si hay varias columnas seleccionadas
        filas_unicas = set(index.row() for index in indices)

        # 3. Procesar cada fila
        for fila in filas_unicas:
            # 4. Obtener el ID de la columna 0 para esa fila
            # .data() extrae el contenido de la celda directamente
            id_item = self.vprin.tablapagos.model().index(fila, 12).data()
            print(id_item)
            if id_item is not None:
                # 5. Llamar a tu métod de base de datos
                # Reemplaza 'tu_metodo_bd' por el nombre real de tu función
                ReparacionModel().actualizar_ptecnico(id_item)

        # 6. Refrescar la tabla para mostrar los cambios
        self.tabla_pago()
        self.vprin.total_p.setText("0")