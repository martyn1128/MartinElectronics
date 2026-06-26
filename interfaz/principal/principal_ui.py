# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'principal.ui'
##
## Created by: Qt User Interface Compiler version 6.11.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCharts import QChartView
from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QAbstractItemView, QAbstractScrollArea, QAbstractSpinBox, QApplication,
    QCheckBox, QComboBox, QDateTimeEdit, QDoubleSpinBox,
    QFormLayout, QFrame, QGridLayout, QGroupBox,
    QHBoxLayout, QHeaderView, QLabel, QLineEdit,
    QListView, QListWidget, QListWidgetItem, QMainWindow,
    QPlainTextEdit, QProgressBar, QPushButton, QRadioButton,
    QScrollArea, QSizePolicy, QSlider, QSpacerItem,
    QSpinBox, QStackedWidget, QStatusBar, QTabWidget,
    QTableView, QTableWidget, QTableWidgetItem, QTextEdit,
    QToolButton, QVBoxLayout, QWidget)
from recursos import recursos_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.setEnabled(True)
        MainWindow.resize(800, 600)
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setMinimumSize(QSize(800, 600))
        icon = QIcon()
        icon.addFile(u":/iconos/iconos/Logo.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setStyleSheet(u"")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Ignored, QSizePolicy.Policy.Ignored)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.centralwidget.sizePolicy().hasHeightForWidth())
        self.centralwidget.setSizePolicy(sizePolicy1)
        self.centralwidget.setMaximumSize(QSize(16777215, 16777215))
        self.centralwidget.setStyleSheet(u"")
        self.horizontalLayout = QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setSpacing(6)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 9, 0)
        self.menu = QWidget(self.centralwidget)
        self.menu.setObjectName(u"menu")
        self.menu.setMaximumSize(QSize(250, 16777215))
        self.menu.setStyleSheet(u"#menu{\n"
"	background-color: rgba(7, 39, 67, 140);\n"
"}\n"
"QWidget#centralwidget QPushButton:hover {\n"
"	\n"
"	background-color: qlineargradient(spread:pad, x1:1, y1:1, x2:1, y2:1, stop:0 rgba(15, 58, 90, 185), stop:1 rgba(255, 255, 255, 255));\n"
"	border-top-left-radius: 20px\n"
"}\n"
"QWidget#centralwidget QPushButton{\n"
"	border-bottom-right-radius:20px\n"
"}\n"
"QWidget#centralwidget QPushButton:checked {\n"
"       /* al presionar */\n"
"	background-color: rgb(7, 39, 67);\n"
"    border-top-left-radius: 20px;\n"
"	color: rgb(255,255,255);\n"
"}\n"
"\n"
"")
        self.verticalLayout = QVBoxLayout(self.menu)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, -1, 0, -1)
        self.verticalSpacer_2 = QSpacerItem(20, 60, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)

        self.verticalLayout.addItem(self.verticalSpacer_2)

        self.btninicio = QPushButton(self.menu)
        self.btninicio.setObjectName(u"btninicio")
        self.btninicio.setStyleSheet(u"QPushButton{\n"
"border: none;\n"
"font: 600 11pt \"Segoe UI\";\n"
"text-align: left;\n"
"padding: 10px 5px;\n"
"}\n"
"QWidget#centralwidget QPushButton:checked {\n"
"	background-color: rgb(7, 39, 67);\n"
"	border-top-left-radius: 20px\n"
"}\n"
"\n"
"\n"
"\n"
"")
        icon1 = QIcon()
        icon1.addFile(u":/iconos/iconos/casa.ico", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.btninicio.setIcon(icon1)
        self.btninicio.setIconSize(QSize(30, 30))
        self.btninicio.setCheckable(True)
        self.btninicio.setChecked(True)
        self.btninicio.setAutoRepeat(False)
        self.btninicio.setAutoExclusive(True)

        self.verticalLayout.addWidget(self.btninicio)

        self.btnregistros = QPushButton(self.menu)
        self.btnregistros.setObjectName(u"btnregistros")
        self.btnregistros.setStyleSheet(u"QPushButton{\n"
"border:none;\n"
"font: 600 11pt \"Segoe UI\";\n"
"text-align: left;\n"
"padding: 10px 5px;\n"
"}\n"
"QWidget#centralwidget QPushButton:checked {\n"
"       /* al presionar */\n"
"	background-color: rgb(7, 39, 67);\n"
"    border-top-left-radius: 20px\n"
"}\n"
"")
        icon2 = QIcon()
        icon2.addFile(u":/iconos/iconos/recivir.ico", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.btnregistros.setIcon(icon2)
        self.btnregistros.setIconSize(QSize(40, 40))
        self.btnregistros.setCheckable(True)
        self.btnregistros.setAutoExclusive(True)

        self.verticalLayout.addWidget(self.btnregistros)

        self.btnreparaciones = QPushButton(self.menu)
        self.btnreparaciones.setObjectName(u"btnreparaciones")
        self.btnreparaciones.setStyleSheet(u"QPushButton{\n"
"border:none;\n"
"font: 600 11pt \"Segoe UI\";\n"
"text-align: left;\n"
"padding: 10px 5px;\n"
"}\n"
"QWidget#centralwidget QPushButton:checked {\n"
"       /* al presionar */\n"
"	background-color: rgb(7, 39, 67);\n"
"    border-top-left-radius: 20px\n"
"}\n"
"")
        icon3 = QIcon()
        icon3.addFile(u":/iconos/iconos/multimetro.ico", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.btnreparaciones.setIcon(icon3)
        self.btnreparaciones.setIconSize(QSize(40, 40))
        self.btnreparaciones.setCheckable(True)
        self.btnreparaciones.setAutoExclusive(True)

        self.verticalLayout.addWidget(self.btnreparaciones)

        self.btnentregas = QPushButton(self.menu)
        self.btnentregas.setObjectName(u"btnentregas")
        self.btnentregas.setStyleSheet(u"QPushButton{\n"
"border:none;\n"
"font: 600 11pt \"Segoe UI\";\n"
"text-align: left;\n"
"padding: 10px 5px;\n"
"}\n"
"QWidget#centralwidget QPushButton:checked {\n"
"       /* al presionar */\n"
"	background-color: rgb(7, 39, 67);\n"
"    border-top-left-radius: 20px\n"
"}\n"
"")
        icon4 = QIcon()
        icon4.addFile(u":/iconos/iconos/entrega.ico", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.btnentregas.setIcon(icon4)
        self.btnentregas.setIconSize(QSize(35, 35))
        self.btnentregas.setCheckable(True)
        self.btnentregas.setAutoExclusive(True)

        self.verticalLayout.addWidget(self.btnentregas)

        self.btnclientes = QPushButton(self.menu)
        self.btnclientes.setObjectName(u"btnclientes")
        self.btnclientes.setStyleSheet(u"QPushButton{\n"
"border:none;\n"
"font: 600 11pt \"Segoe UI\";\n"
"text-align: left;\n"
"padding: 10px 5px;\n"
"}\n"
"QWidget#centralwidget QPushButton:checked {\n"
"       /* al presionar */\n"
"	background-color: rgb(7, 39, 67);\n"
"    border-top-left-radius: 20px\n"
"}\n"
"")
        icon5 = QIcon()
        icon5.addFile(u":/iconos/iconos/clientes.ico", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.btnclientes.setIcon(icon5)
        self.btnclientes.setIconSize(QSize(35, 35))
        self.btnclientes.setCheckable(True)
        self.btnclientes.setAutoExclusive(True)

        self.verticalLayout.addWidget(self.btnclientes)

        self.btnpago = QPushButton(self.menu)
        self.btnpago.setObjectName(u"btnpago")
        self.btnpago.setStyleSheet(u"QPushButton{\n"
"border:none;\n"
"font: 600 11pt \"Segoe UI\";\n"
"text-align: left;\n"
"padding: 10px 9px;\n"
"}\n"
"QWidget#centralwidget QPushButton:checked {\n"
"       /* al presionar */\n"
"	background-color: rgb(7, 39, 67);\n"
"    border-top-left-radius: 20px\n"
"}\n"
"")
        icon6 = QIcon()
        icon6.addFile(u":/iconos/iconos/pago.ico", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.btnpago.setIcon(icon6)
        self.btnpago.setIconSize(QSize(35, 35))
        self.btnpago.setCheckable(True)
        self.btnpago.setAutoExclusive(True)

        self.verticalLayout.addWidget(self.btnpago)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer)

        self.btnconfig = QPushButton(self.menu)
        self.btnconfig.setObjectName(u"btnconfig")
        self.btnconfig.setStyleSheet(u"QPushButton{\n"
"border:none;\n"
"font: 600 11pt \"Segoe UI\";\n"
"text-align: left;\n"
"padding: 10px 5px;\n"
"}\n"
"QWidget#centralwidget QPushButton:checked {\n"
"       /* al presionar */\n"
"	background-color: rgb(7, 39, 67);\n"
"    border-top-left-radius: 20px\n"
"}\n"
"")
        icon7 = QIcon()
        icon7.addFile(u":/iconos/iconos/config.ico", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.btnconfig.setIcon(icon7)
        self.btnconfig.setIconSize(QSize(30, 30))
        self.btnconfig.setCheckable(True)
        self.btnconfig.setAutoExclusive(True)

        self.verticalLayout.addWidget(self.btnconfig)


        self.horizontalLayout.addWidget(self.menu)

        self.pprincipal = QWidget(self.centralwidget)
        self.pprincipal.setObjectName(u"pprincipal")
        self.pprincipal.setMinimumSize(QSize(0, 0))
        self.pprincipal.setStyleSheet(u"")
        self.verticalLayout_2 = QVBoxLayout(self.pprincipal)
        self.verticalLayout_2.setSpacing(2)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(2, 2, 1, 0)
        self.widget_2 = QWidget(self.pprincipal)
        self.widget_2.setObjectName(u"widget_2")
        self.widget_2.setMinimumSize(QSize(0, 80))
        self.widget_2.setMaximumSize(QSize(16777215, 70))
        self.widget_2.setStyleSheet(u"border-radius: 10px;")
        self.verticalLayout_3 = QVBoxLayout(self.widget_2)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, -1)
        self.widget_3 = QWidget(self.widget_2)
        self.widget_3.setObjectName(u"widget_3")
        self.widget_3.setMinimumSize(QSize(0, 70))
        self.widget_3.setMaximumSize(QSize(16777215, 50))
        self.widget_3.setStyleSheet(u"background-color: rgb(8, 42, 73);\n"
"color: rgb(255, 255, 255);")
        self.horizontalLayout_2 = QHBoxLayout(self.widget_3)
        self.horizontalLayout_2.setSpacing(2)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(2, 10, 20, 5)
        self.btnmenu = QPushButton(self.widget_3)
        self.btnmenu.setObjectName(u"btnmenu")
        self.btnmenu.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.btnmenu.setAutoFillBackground(False)
        self.btnmenu.setStyleSheet(u"QPushButton{\n"
"background-color:rgb(5, 31, 53);\n"
"font: 600 11pt \"Segoe UI\";\n"
"text-align: left;\n"
"padding: 2px 4px\n"
"}\n"
"QWidget#centralwidget QPushButton:checked {\n"
"	background-color: rgb(7, 39, 67);\n"
"	border-top-left-radius: 20px\n"
"}")
        icon8 = QIcon()
        icon8.addFile(u":/iconos/iconos/menu.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.btnmenu.setIcon(icon8)
        self.btnmenu.setIconSize(QSize(26, 30))
        self.btnmenu.setCheckable(True)
        self.btnmenu.setFlat(False)

        self.horizontalLayout_2.addWidget(self.btnmenu)

        self.atras = QToolButton(self.widget_3)
        self.atras.setObjectName(u"atras")
        icon9 = QIcon()
        icon9.addFile(u":/iconos/iconos/anterior.ico", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.atras.setIcon(icon9)
        self.atras.setIconSize(QSize(30, 30))

        self.horizontalLayout_2.addWidget(self.atras)

        self.widget = QWidget(self.widget_3)
        self.widget.setObjectName(u"widget")
        self.verticalLayout_4 = QVBoxLayout(self.widget)
        self.verticalLayout_4.setSpacing(2)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.label = QLabel(self.widget)
        self.label.setObjectName(u"label")
        font = QFont()
        font.setFamilies([u"Cooper"])
        font.setPointSize(18)
        font.setBold(True)
        self.label.setFont(font)
        self.label.setStyleSheet(u"")

        self.verticalLayout_4.addWidget(self.label)

        self.widget_67 = QWidget(self.widget)
        self.widget_67.setObjectName(u"widget_67")
        self.horizontalLayout_49 = QHBoxLayout(self.widget_67)
        self.horizontalLayout_49.setSpacing(0)
        self.horizontalLayout_49.setObjectName(u"horizontalLayout_49")
        self.horizontalLayout_49.setContentsMargins(0, 0, 0, 0)
        self.horizontalSpacer_10 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_49.addItem(self.horizontalSpacer_10)

        self.label_59 = QLabel(self.widget_67)
        self.label_59.setObjectName(u"label_59")
        font1 = QFont()
        font1.setPointSize(10)
        font1.setBold(True)
        self.label_59.setFont(font1)

        self.horizontalLayout_49.addWidget(self.label_59)

        self.usuario = QLabel(self.widget_67)
        self.usuario.setObjectName(u"usuario")
        font2 = QFont()
        font2.setPointSize(10)
        self.usuario.setFont(font2)

        self.horizontalLayout_49.addWidget(self.usuario)


        self.verticalLayout_4.addWidget(self.widget_67)


        self.horizontalLayout_2.addWidget(self.widget)


        self.verticalLayout_3.addWidget(self.widget_3)


        self.verticalLayout_2.addWidget(self.widget_2)

        self.stack = QStackedWidget(self.pprincipal)
        self.stack.setObjectName(u"stack")
        self.stack.setMinimumSize(QSize(0, 0))
        self.page = QWidget()
        self.page.setObjectName(u"page")
        self.page.setMaximumSize(QSize(16777215, 16777215))
        self.verticalLayout_5 = QVBoxLayout(self.page)
        self.verticalLayout_5.setSpacing(4)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setContentsMargins(0, 2, 0, 0)
        self.widget_7 = QWidget(self.page)
        self.widget_7.setObjectName(u"widget_7")
        sizePolicy.setHeightForWidth(self.widget_7.sizePolicy().hasHeightForWidth())
        self.widget_7.setSizePolicy(sizePolicy)
        self.verticalLayout_41 = QVBoxLayout(self.widget_7)
        self.verticalLayout_41.setObjectName(u"verticalLayout_41")
        self.scrollArea = QScrollArea(self.widget_7)
        self.scrollArea.setObjectName(u"scrollArea")
        self.scrollArea.setEnabled(True)
        self.scrollArea.setMinimumSize(QSize(0, 110))
        self.scrollArea.setMaximumSize(QSize(16777215, 130))
        self.scrollArea.setFocusPolicy(Qt.FocusPolicy.NoFocus)
        self.scrollArea.setStyleSheet(u"")
        self.scrollArea.setVerticalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        self.scrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 1458, 109))
        self.scrollAreaWidgetContents.setStyleSheet(u"QWidget#scrollAreaWidgetContents{\n"
"	background-color: qlineargradient(spread:pad, x1:1, y1:1, x2:1, y2:1, stop:0 rgba(8, 42, 73, 114), stop:1 rgba(255, 255, 255, 255));\n"
"\n"
"}\n"
"")
        self.horizontalLayout_3 = QHBoxLayout(self.scrollAreaWidgetContents)
        self.horizontalLayout_3.setSpacing(30)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(-1, 0, -1, -1)
        self.widget_5 = QWidget(self.scrollAreaWidgetContents)
        self.widget_5.setObjectName(u"widget_5")
        self.widget_5.setMinimumSize(QSize(180, 0))
        self.widget_5.setMaximumSize(QSize(16777215, 100))
        self.widget_5.setStyleSheet(u"\n"
"border-radius: 15px")
        self.horizontalLayout_6 = QHBoxLayout(self.widget_5)
        self.horizontalLayout_6.setSpacing(2)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.horizontalLayout_6.setContentsMargins(3, 0, 3, 4)
        self.widget_6 = QWidget(self.widget_5)
        self.widget_6.setObjectName(u"widget_6")
        self.verticalLayout_6 = QVBoxLayout(self.widget_6)
        self.verticalLayout_6.setSpacing(5)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.verticalLayout_6.setContentsMargins(3, -1, 3, 0)
        self.widget_9 = QWidget(self.widget_6)
        self.widget_9.setObjectName(u"widget_9")
        self.widget_9.setMinimumSize(QSize(0, 55))
        self.horizontalLayout_7 = QHBoxLayout(self.widget_9)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.pendrev = QLabel(self.widget_9)
        self.pendrev.setObjectName(u"pendrev")
        font3 = QFont()
        font3.setPointSize(18)
        font3.setBold(True)
        self.pendrev.setFont(font3)
        self.pendrev.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout_7.addWidget(self.pendrev)

        self.label_13 = QLabel(self.widget_9)
        self.label_13.setObjectName(u"label_13")
        self.label_13.setMinimumSize(QSize(50, 45))
        self.label_13.setMaximumSize(QSize(60, 16777215))
        self.label_13.setPixmap(QPixmap(u":/iconos/iconos/multimetro.ico"))
        self.label_13.setScaledContents(True)

        self.horizontalLayout_7.addWidget(self.label_13)


        self.verticalLayout_6.addWidget(self.widget_9)

        self.label_9 = QLabel(self.widget_6)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setMinimumSize(QSize(50, 20))

        self.verticalLayout_6.addWidget(self.label_9)


        self.horizontalLayout_6.addWidget(self.widget_6)


        self.horizontalLayout_3.addWidget(self.widget_5)

        self.widget_8 = QWidget(self.scrollAreaWidgetContents)
        self.widget_8.setObjectName(u"widget_8")
        self.widget_8.setMinimumSize(QSize(180, 0))
        self.widget_8.setMaximumSize(QSize(16777215, 100))
        self.widget_8.setStyleSheet(u"\n"
"border-radius: 15px")
        self.horizontalLayout_10 = QHBoxLayout(self.widget_8)
        self.horizontalLayout_10.setSpacing(2)
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.horizontalLayout_10.setContentsMargins(3, -1, 3, 4)
        self.widget_13 = QWidget(self.widget_8)
        self.widget_13.setObjectName(u"widget_13")
        self.verticalLayout_8 = QVBoxLayout(self.widget_13)
        self.verticalLayout_8.setSpacing(5)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.verticalLayout_8.setContentsMargins(3, 0, 3, 0)
        self.widget_14 = QWidget(self.widget_13)
        self.widget_14.setObjectName(u"widget_14")
        self.widget_14.setMinimumSize(QSize(0, 55))
        self.horizontalLayout_11 = QHBoxLayout(self.widget_14)
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.pendconf = QLabel(self.widget_14)
        self.pendconf.setObjectName(u"pendconf")
        self.pendconf.setFont(font3)
        self.pendconf.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout_11.addWidget(self.pendconf)

        self.label_16 = QLabel(self.widget_14)
        self.label_16.setObjectName(u"label_16")
        self.label_16.setMinimumSize(QSize(50, 45))
        self.label_16.setMaximumSize(QSize(60, 16777215))
        self.label_16.setPixmap(QPixmap(u":/iconos/iconos/confirm.ico"))
        self.label_16.setScaledContents(True)

        self.horizontalLayout_11.addWidget(self.label_16)


        self.verticalLayout_8.addWidget(self.widget_14)

        self.label_17 = QLabel(self.widget_13)
        self.label_17.setObjectName(u"label_17")
        self.label_17.setMinimumSize(QSize(50, 20))

        self.verticalLayout_8.addWidget(self.label_17)


        self.horizontalLayout_10.addWidget(self.widget_13)


        self.horizontalLayout_3.addWidget(self.widget_8)

        self.widget_10 = QWidget(self.scrollAreaWidgetContents)
        self.widget_10.setObjectName(u"widget_10")
        self.widget_10.setMinimumSize(QSize(180, 0))
        self.widget_10.setMaximumSize(QSize(16777215, 100))
        font4 = QFont()
        font4.setBold(True)
        self.widget_10.setFont(font4)
        self.widget_10.setStyleSheet(u"\n"
"border-radius: 15px")
        self.horizontalLayout_8 = QHBoxLayout(self.widget_10)
        self.horizontalLayout_8.setSpacing(2)
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.horizontalLayout_8.setContentsMargins(3, 0, 3, 4)
        self.widget_11 = QWidget(self.widget_10)
        self.widget_11.setObjectName(u"widget_11")
        self.verticalLayout_7 = QVBoxLayout(self.widget_11)
        self.verticalLayout_7.setSpacing(5)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.verticalLayout_7.setContentsMargins(3, 0, 3, 0)
        self.widget_12 = QWidget(self.widget_11)
        self.widget_12.setObjectName(u"widget_12")
        self.widget_12.setMinimumSize(QSize(0, 55))
        self.horizontalLayout_9 = QHBoxLayout(self.widget_12)
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.pendrep = QLabel(self.widget_12)
        self.pendrep.setObjectName(u"pendrep")
        self.pendrep.setFont(font3)
        self.pendrep.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout_9.addWidget(self.pendrep)

        self.label_10 = QLabel(self.widget_12)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setMinimumSize(QSize(60, 50))
        self.label_10.setMaximumSize(QSize(60, 16777215))
        self.label_10.setPixmap(QPixmap(u":/iconos/iconos/cautin.png"))
        self.label_10.setScaledContents(True)

        self.horizontalLayout_9.addWidget(self.label_10)


        self.verticalLayout_7.addWidget(self.widget_12)

        self.label_14 = QLabel(self.widget_11)
        self.label_14.setObjectName(u"label_14")
        self.label_14.setMinimumSize(QSize(50, 20))
        self.label_14.setFont(font4)

        self.verticalLayout_7.addWidget(self.label_14)


        self.horizontalLayout_8.addWidget(self.widget_11)


        self.horizontalLayout_3.addWidget(self.widget_10)

        self.widget_18 = QWidget(self.scrollAreaWidgetContents)
        self.widget_18.setObjectName(u"widget_18")
        self.widget_18.setMinimumSize(QSize(180, 0))
        self.widget_18.setMaximumSize(QSize(16777215, 100))
        self.widget_18.setStyleSheet(u"\n"
"border-radius: 15px")
        self.horizontalLayout_14 = QHBoxLayout(self.widget_18)
        self.horizontalLayout_14.setSpacing(2)
        self.horizontalLayout_14.setObjectName(u"horizontalLayout_14")
        self.horizontalLayout_14.setContentsMargins(3, 0, 3, 4)
        self.widget_19 = QWidget(self.widget_18)
        self.widget_19.setObjectName(u"widget_19")
        self.verticalLayout_10 = QVBoxLayout(self.widget_19)
        self.verticalLayout_10.setSpacing(5)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.verticalLayout_10.setContentsMargins(3, 0, 3, 0)
        self.widget_20 = QWidget(self.widget_19)
        self.widget_20.setObjectName(u"widget_20")
        self.widget_20.setMinimumSize(QSize(0, 55))
        self.horizontalLayout_15 = QHBoxLayout(self.widget_20)
        self.horizontalLayout_15.setObjectName(u"horizontalLayout_15")
        self.horizontalLayout_15.setContentsMargins(-1, -1, -1, 5)
        self.teet = QLabel(self.widget_20)
        self.teet.setObjectName(u"teet")
        self.teet.setFont(font3)
        self.teet.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.teet.setMargin(12)

        self.horizontalLayout_15.addWidget(self.teet)

        self.label_22 = QLabel(self.widget_20)
        self.label_22.setObjectName(u"label_22")
        self.label_22.setMinimumSize(QSize(50, 65))
        self.label_22.setMaximumSize(QSize(60, 16777215))
        self.label_22.setPixmap(QPixmap(u":/iconos/iconos/almacen.ico"))
        self.label_22.setScaledContents(True)

        self.horizontalLayout_15.addWidget(self.label_22)


        self.verticalLayout_10.addWidget(self.widget_20)

        self.label_23 = QLabel(self.widget_19)
        self.label_23.setObjectName(u"label_23")
        self.label_23.setMinimumSize(QSize(50, 20))

        self.verticalLayout_10.addWidget(self.label_23)


        self.horizontalLayout_14.addWidget(self.widget_19)


        self.horizontalLayout_3.addWidget(self.widget_18)

        self.widget_21 = QWidget(self.scrollAreaWidgetContents)
        self.widget_21.setObjectName(u"widget_21")
        self.widget_21.setMinimumSize(QSize(180, 0))
        self.widget_21.setMaximumSize(QSize(16777215, 100))
        self.widget_21.setStyleSheet(u"\n"
"border-radius: 15px")
        self.horizontalLayout_17 = QHBoxLayout(self.widget_21)
        self.horizontalLayout_17.setSpacing(2)
        self.horizontalLayout_17.setObjectName(u"horizontalLayout_17")
        self.horizontalLayout_17.setContentsMargins(3, 0, 3, 4)
        self.widget_23 = QWidget(self.widget_21)
        self.widget_23.setObjectName(u"widget_23")
        self.verticalLayout_12 = QVBoxLayout(self.widget_23)
        self.verticalLayout_12.setSpacing(5)
        self.verticalLayout_12.setObjectName(u"verticalLayout_12")
        self.verticalLayout_12.setContentsMargins(3, 0, 3, 0)
        self.widget_24 = QWidget(self.widget_23)
        self.widget_24.setObjectName(u"widget_24")
        self.widget_24.setMinimumSize(QSize(0, 55))
        self.horizontalLayout_18 = QHBoxLayout(self.widget_24)
        self.horizontalLayout_18.setObjectName(u"horizontalLayout_18")
        self.horizontalLayout_18.setContentsMargins(-1, -1, -1, 5)
        self.totalreg = QLabel(self.widget_24)
        self.totalreg.setObjectName(u"totalreg")
        self.totalreg.setFont(font3)
        self.totalreg.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.totalreg.setMargin(12)

        self.horizontalLayout_18.addWidget(self.totalreg)

        self.label_28 = QLabel(self.widget_24)
        self.label_28.setObjectName(u"label_28")
        self.label_28.setMinimumSize(QSize(50, 65))
        self.label_28.setMaximumSize(QSize(60, 16777215))
        self.label_28.setPixmap(QPixmap(u":/iconos/iconos/registros.ico"))
        self.label_28.setScaledContents(True)

        self.horizontalLayout_18.addWidget(self.label_28)


        self.verticalLayout_12.addWidget(self.widget_24)

        self.label_29 = QLabel(self.widget_23)
        self.label_29.setObjectName(u"label_29")
        self.label_29.setMinimumSize(QSize(50, 20))

        self.verticalLayout_12.addWidget(self.label_29)


        self.horizontalLayout_17.addWidget(self.widget_23)


        self.horizontalLayout_3.addWidget(self.widget_21)

        self.widget_25 = QWidget(self.scrollAreaWidgetContents)
        self.widget_25.setObjectName(u"widget_25")
        self.widget_25.setMinimumSize(QSize(180, 0))
        self.widget_25.setMaximumSize(QSize(16777215, 100))
        self.widget_25.setStyleSheet(u"\n"
"border-radius: 15px")
        self.horizontalLayout_19 = QHBoxLayout(self.widget_25)
        self.horizontalLayout_19.setSpacing(2)
        self.horizontalLayout_19.setObjectName(u"horizontalLayout_19")
        self.horizontalLayout_19.setContentsMargins(3, 0, 3, 4)
        self.widget_26 = QWidget(self.widget_25)
        self.widget_26.setObjectName(u"widget_26")
        self.verticalLayout_13 = QVBoxLayout(self.widget_26)
        self.verticalLayout_13.setSpacing(5)
        self.verticalLayout_13.setObjectName(u"verticalLayout_13")
        self.verticalLayout_13.setContentsMargins(3, -1, 3, 0)
        self.widget_27 = QWidget(self.widget_26)
        self.widget_27.setObjectName(u"widget_27")
        self.widget_27.setMinimumSize(QSize(0, 55))
        self.horizontalLayout_20 = QHBoxLayout(self.widget_27)
        self.horizontalLayout_20.setObjectName(u"horizontalLayout_20")
        self.totalclientes = QLabel(self.widget_27)
        self.totalclientes.setObjectName(u"totalclientes")
        self.totalclientes.setMinimumSize(QSize(0, 40))
        self.totalclientes.setFont(font3)
        self.totalclientes.setStyleSheet(u"")
        self.totalclientes.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout_20.addWidget(self.totalclientes)

        self.label_30 = QLabel(self.widget_27)
        self.label_30.setObjectName(u"label_30")
        self.label_30.setMinimumSize(QSize(40, 40))
        self.label_30.setMaximumSize(QSize(60, 16777215))
        self.label_30.setPixmap(QPixmap(u":/iconos/iconos/clientes.ico"))
        self.label_30.setScaledContents(True)

        self.horizontalLayout_20.addWidget(self.label_30)


        self.verticalLayout_13.addWidget(self.widget_27)

        self.label_32 = QLabel(self.widget_26)
        self.label_32.setObjectName(u"label_32")
        self.label_32.setMinimumSize(QSize(50, 20))

        self.verticalLayout_13.addWidget(self.label_32)


        self.horizontalLayout_19.addWidget(self.widget_26)


        self.horizontalLayout_3.addWidget(self.widget_25)

        self.widget_15 = QWidget(self.scrollAreaWidgetContents)
        self.widget_15.setObjectName(u"widget_15")
        self.widget_15.setEnabled(False)
        self.widget_15.setMinimumSize(QSize(180, 0))
        self.widget_15.setMaximumSize(QSize(16777215, 100))
        self.widget_15.setStyleSheet(u"\n"
"border-radius: 15px")
        self.horizontalLayout_12 = QHBoxLayout(self.widget_15)
        self.horizontalLayout_12.setSpacing(2)
        self.horizontalLayout_12.setObjectName(u"horizontalLayout_12")
        self.horizontalLayout_12.setContentsMargins(3, -1, 3, 4)
        self.widget_16 = QWidget(self.widget_15)
        self.widget_16.setObjectName(u"widget_16")
        self.verticalLayout_9 = QVBoxLayout(self.widget_16)
        self.verticalLayout_9.setSpacing(5)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.verticalLayout_9.setContentsMargins(3, -1, 3, 0)
        self.widget_17 = QWidget(self.widget_16)
        self.widget_17.setObjectName(u"widget_17")
        self.widget_17.setMinimumSize(QSize(0, 55))
        self.horizontalLayout_13 = QHBoxLayout(self.widget_17)
        self.horizontalLayout_13.setObjectName(u"horizontalLayout_13")
        self.label_19 = QLabel(self.widget_17)
        self.label_19.setObjectName(u"label_19")
        self.label_19.setMinimumSize(QSize(40, 40))
        self.label_19.setMaximumSize(QSize(60, 16777215))
        self.label_19.setPixmap(QPixmap(u":/iconos/iconos/$.ico"))
        self.label_19.setScaledContents(True)

        self.horizontalLayout_13.addWidget(self.label_19)

        self.pagact = QLabel(self.widget_17)
        self.pagact.setObjectName(u"pagact")
        self.pagact.setMinimumSize(QSize(0, 40))
        font5 = QFont()
        font5.setPointSize(18)
        self.pagact.setFont(font5)

        self.horizontalLayout_13.addWidget(self.pagact)


        self.verticalLayout_9.addWidget(self.widget_17)

        self.label_20 = QLabel(self.widget_16)
        self.label_20.setObjectName(u"label_20")
        self.label_20.setMinimumSize(QSize(50, 20))
        self.label_20.setFont(font4)

        self.verticalLayout_9.addWidget(self.label_20)


        self.horizontalLayout_12.addWidget(self.widget_16)


        self.horizontalLayout_3.addWidget(self.widget_15)

        self.scrollArea.setWidget(self.scrollAreaWidgetContents)

        self.verticalLayout_41.addWidget(self.scrollArea)

        self.scrollArea_3 = QScrollArea(self.widget_7)
        self.scrollArea_3.setObjectName(u"scrollArea_3")
        self.scrollArea_3.setWidgetResizable(True)
        self.scrollAreaWidgetContents_7 = QWidget()
        self.scrollAreaWidgetContents_7.setObjectName(u"scrollAreaWidgetContents_7")
        self.scrollAreaWidgetContents_7.setGeometry(QRect(0, 0, 603, 355))
        self.verticalLayout_40 = QVBoxLayout(self.scrollAreaWidgetContents_7)
        self.verticalLayout_40.setObjectName(u"verticalLayout_40")
        self.widget_73 = QWidget(self.scrollAreaWidgetContents_7)
        self.widget_73.setObjectName(u"widget_73")
        self.horizontalLayout_52 = QHBoxLayout(self.widget_73)
        self.horizontalLayout_52.setObjectName(u"horizontalLayout_52")
        self.groupBox_14 = QGroupBox(self.widget_73)
        self.groupBox_14.setObjectName(u"groupBox_14")
        self.verticalLayout_11 = QVBoxLayout(self.groupBox_14)
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.listView_3 = QListView(self.groupBox_14)
        self.listView_3.setObjectName(u"listView_3")
        self.listView_3.setStyleSheet(u"QListView::item:hover {\n"
"        /* Capa negra con 30% de opacidad para oscurecer el fondo actual */\n"
"        background-color: rgba(0, 0, 0, 10); \n"
"        \n"
"        /* Opcional: un borde sutil para definir la selecci\u00f3n */\n"
"        border: 1px solid rgba(255, 255, 255, 10);\n"
"    }\n"
"    \n"
"    QListView::item:selected {\n"
"        /* Al seleccionar, podemos oscurecerlo a\u00fan m\u00e1s */\n"
"        background-color: rgba(0, 0, 0, 40);\n"
"        border: 1px solid rgba(255, 255, 255, 30);\n"
"    }")
        self.listView_3.setAutoScrollMargin(16)
        self.listView_3.setEditTriggers(QAbstractItemView.EditTrigger.NoEditTriggers)
        self.listView_3.setAlternatingRowColors(True)
        self.listView_3.setIconSize(QSize(50, 50))
        self.listView_3.setMovement(QListView.Movement.Static)

        self.verticalLayout_11.addWidget(self.listView_3)


        self.horizontalLayout_52.addWidget(self.groupBox_14)

        self.groupBox_15 = QGroupBox(self.widget_73)
        self.groupBox_15.setObjectName(u"groupBox_15")
        self.verticalLayout_39 = QVBoxLayout(self.groupBox_15)
        self.verticalLayout_39.setObjectName(u"verticalLayout_39")
        self.listView_4 = QListView(self.groupBox_15)
        self.listView_4.setObjectName(u"listView_4")
        self.listView_4.setStyleSheet(u"QListView::item:hover {\n"
"        /* Capa negra con 30% de opacidad para oscurecer el fondo actual */\n"
"        background-color: rgba(0, 0, 0, 10); \n"
"        \n"
"        /* Opcional: un borde sutil para definir la selecci\u00f3n */\n"
"        border: 1px solid rgba(255, 255, 255, 10);\n"
"    }\n"
"    \n"
"    QListView::item:selected {\n"
"        /* Al seleccionar, podemos oscurecerlo a\u00fan m\u00e1s */\n"
"        background-color: rgba(0, 0, 0, 40);\n"
"        border: 1px solid rgba(255, 255, 255, 30);\n"
"    }")
        self.listView_4.setAutoScrollMargin(16)
        self.listView_4.setAlternatingRowColors(True)
        self.listView_4.setIconSize(QSize(50, 50))
        self.listView_4.setMovement(QListView.Movement.Static)

        self.verticalLayout_39.addWidget(self.listView_4)


        self.horizontalLayout_52.addWidget(self.groupBox_15)

        self.widget_74 = QWidget(self.widget_73)
        self.widget_74.setObjectName(u"widget_74")
        sizePolicy.setHeightForWidth(self.widget_74.sizePolicy().hasHeightForWidth())
        self.widget_74.setSizePolicy(sizePolicy)
        self.verticalLayout_42 = QVBoxLayout(self.widget_74)
        self.verticalLayout_42.setObjectName(u"verticalLayout_42")
        self.label_11 = QLabel(self.widget_74)
        self.label_11.setObjectName(u"label_11")
        self.label_11.setMaximumSize(QSize(16777215, 30))
        font6 = QFont()
        font6.setPointSize(11)
        font6.setBold(True)
        self.label_11.setFont(font6)
        self.label_11.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)

        self.verticalLayout_42.addWidget(self.label_11)

        self.graficai = QChartView(self.widget_74)
        self.graficai.setObjectName(u"graficai")
        sizePolicy.setHeightForWidth(self.graficai.sizePolicy().hasHeightForWidth())
        self.graficai.setSizePolicy(sizePolicy)

        self.verticalLayout_42.addWidget(self.graficai)


        self.horizontalLayout_52.addWidget(self.widget_74)


        self.verticalLayout_40.addWidget(self.widget_73)

        self.widget_72 = QWidget(self.scrollAreaWidgetContents_7)
        self.widget_72.setObjectName(u"widget_72")
        sizePolicy.setHeightForWidth(self.widget_72.sizePolicy().hasHeightForWidth())
        self.widget_72.setSizePolicy(sizePolicy)
        self.verticalLayout_33 = QVBoxLayout(self.widget_72)
        self.verticalLayout_33.setObjectName(u"verticalLayout_33")
        self.verticalLayout_33.setContentsMargins(-1, -1, -1, 0)
        self.label_2 = QLabel(self.widget_72)
        self.label_2.setObjectName(u"label_2")

        self.verticalLayout_33.addWidget(self.label_2)

        self.tablaconf = QTableView(self.widget_72)
        self.tablaconf.setObjectName(u"tablaconf")
        self.tablaconf.setMinimumSize(QSize(0, 100))
        self.tablaconf.setSizeAdjustPolicy(QAbstractScrollArea.SizeAdjustPolicy.AdjustToContentsOnFirstShow)
        self.tablaconf.setSelectionBehavior(QAbstractItemView.SelectionBehavior.SelectRows)
        self.tablaconf.horizontalHeader().setStretchLastSection(True)

        self.verticalLayout_33.addWidget(self.tablaconf)

        self.btnconfirmarpre = QToolButton(self.widget_72)
        self.btnconfirmarpre.setObjectName(u"btnconfirmarpre")
        self.btnconfirmarpre.setMinimumSize(QSize(62, 0))
        self.btnconfirmarpre.setMaximumSize(QSize(16777215, 60))
        icon10 = QIcon()
        icon10.addFile(u":/iconos/iconos/confirm.ico", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.btnconfirmarpre.setIcon(icon10)
        self.btnconfirmarpre.setIconSize(QSize(40, 40))
        self.btnconfirmarpre.setToolButtonStyle(Qt.ToolButtonStyle.ToolButtonTextUnderIcon)

        self.verticalLayout_33.addWidget(self.btnconfirmarpre)


        self.verticalLayout_40.addWidget(self.widget_72)

        self.scrollArea_3.setWidget(self.scrollAreaWidgetContents_7)

        self.verticalLayout_41.addWidget(self.scrollArea_3)


        self.verticalLayout_5.addWidget(self.widget_7)

        self.stack.addWidget(self.page)
        self.page_2 = QWidget()
        self.page_2.setObjectName(u"page_2")
        self.page_2.setMaximumSize(QSize(16777215, 16777215))
        self.verticalLayout_14 = QVBoxLayout(self.page_2)
        self.verticalLayout_14.setObjectName(u"verticalLayout_14")
        self.verticalLayout_14.setContentsMargins(-1, 2, -1, 0)
        self.tabregistros = QTabWidget(self.page_2)
        self.tabregistros.setObjectName(u"tabregistros")
        self.tab_3 = QWidget()
        self.tab_3.setObjectName(u"tab_3")
        self.horizontalLayout_33 = QHBoxLayout(self.tab_3)
        self.horizontalLayout_33.setSpacing(2)
        self.horizontalLayout_33.setObjectName(u"horizontalLayout_33")
        self.horizontalLayout_33.setContentsMargins(-1, 2, -1, 2)
        self.widget_22 = QWidget(self.tab_3)
        self.widget_22.setObjectName(u"widget_22")
        self.verticalLayout_15 = QVBoxLayout(self.widget_22)
        self.verticalLayout_15.setSpacing(0)
        self.verticalLayout_15.setObjectName(u"verticalLayout_15")
        self.verticalLayout_15.setContentsMargins(-1, 0, -1, 0)
        self.widget_32 = QWidget(self.widget_22)
        self.widget_32.setObjectName(u"widget_32")
        self.horizontalLayout_5 = QHBoxLayout(self.widget_32)
        self.horizontalLayout_5.setSpacing(6)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_5.setContentsMargins(-1, 0, -1, 0)
        self.label_36 = QLabel(self.widget_32)
        self.label_36.setObjectName(u"label_36")
        self.label_36.setMaximumSize(QSize(130, 16777215))
        font7 = QFont()
        font7.setPointSize(12)
        self.label_36.setFont(font7)

        self.horizontalLayout_5.addWidget(self.label_36)

        self.ods = QSpinBox(self.widget_32)
        self.ods.setObjectName(u"ods")
        self.ods.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)
        self.ods.setMinimum(0)
        self.ods.setMaximum(999999999)
        self.ods.setStepType(QAbstractSpinBox.StepType.DefaultStepType)

        self.horizontalLayout_5.addWidget(self.ods)

        self.horizontalSpacer_5 = QSpacerItem(20, 0, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_5.addItem(self.horizontalSpacer_5)

        self.label_38 = QLabel(self.widget_32)
        self.label_38.setObjectName(u"label_38")
        self.label_38.setMaximumSize(QSize(65, 16777215))
        self.label_38.setFont(font7)

        self.horizontalLayout_5.addWidget(self.label_38)

        self.no = QLabel(self.widget_32)
        self.no.setObjectName(u"no")
        self.no.setMinimumSize(QSize(100, 0))
        self.no.setMaximumSize(QSize(16777215, 25))
        self.no.setFont(font7)
        self.no.setStyleSheet(u"")
        self.no.setMargin(3)

        self.horizontalLayout_5.addWidget(self.no)

        self.label_40 = QLabel(self.widget_32)
        self.label_40.setObjectName(u"label_40")
        self.label_40.setMaximumSize(QSize(30, 16777215))
        self.label_40.setFont(font7)

        self.horizontalLayout_5.addWidget(self.label_40)

        self.de = QLabel(self.widget_32)
        self.de.setObjectName(u"de")
        self.de.setMaximumSize(QSize(16777215, 25))
        self.de.setFont(font7)
        self.de.setMargin(5)

        self.horizontalLayout_5.addWidget(self.de)

        self.btnimprimir = QToolButton(self.widget_32)
        self.btnimprimir.setObjectName(u"btnimprimir")
        icon11 = QIcon()
        icon11.addFile(u":/iconos/iconos/imprimir.ico", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.btnimprimir.setIcon(icon11)
        self.btnimprimir.setIconSize(QSize(20, 20))
        self.btnimprimir.setToolButtonStyle(Qt.ToolButtonStyle.ToolButtonTextUnderIcon)

        self.horizontalLayout_5.addWidget(self.btnimprimir)


        self.verticalLayout_15.addWidget(self.widget_32)

        self.widget_34 = QWidget(self.widget_22)
        self.widget_34.setObjectName(u"widget_34")
        self.horizontalLayout_25 = QHBoxLayout(self.widget_34)
        self.horizontalLayout_25.setObjectName(u"horizontalLayout_25")
        self.horizontalLayout_25.setContentsMargins(-1, 0, -1, 0)
        self.label_48 = QLabel(self.widget_34)
        self.label_48.setObjectName(u"label_48")
        self.label_48.setFont(font7)

        self.horizontalLayout_25.addWidget(self.label_48)

        self.fecha = QLabel(self.widget_34)
        self.fecha.setObjectName(u"fecha")
        self.fecha.setMinimumSize(QSize(100, 0))
        self.fecha.setMaximumSize(QSize(16777215, 25))
        self.fecha.setFont(font7)
        self.fecha.setStyleSheet(u"")
        self.fecha.setMargin(5)

        self.horizontalLayout_25.addWidget(self.fecha)

        self.horizontalSpacer_6 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_25.addItem(self.horizontalSpacer_6)


        self.verticalLayout_15.addWidget(self.widget_34)

        self.widget_29 = QWidget(self.widget_22)
        self.widget_29.setObjectName(u"widget_29")
        self.widget_29.setMaximumSize(QSize(16777215, 500))
        self.horizontalLayout_22 = QHBoxLayout(self.widget_29)
        self.horizontalLayout_22.setObjectName(u"horizontalLayout_22")
        self.horizontalLayout_22.setContentsMargins(-1, 2, -1, -1)
        self.infoequipo = QGroupBox(self.widget_29)
        self.infoequipo.setObjectName(u"infoequipo")
        self.infoequipo.setMaximumSize(QSize(600, 500))
        self.infoequipo.setFont(font7)
        self.verticalLayout_49 = QVBoxLayout(self.infoequipo)
        self.verticalLayout_49.setObjectName(u"verticalLayout_49")
        self.verticalLayout_49.setContentsMargins(-1, -1, -1, 0)
        self.scrollArea_8 = QScrollArea(self.infoequipo)
        self.scrollArea_8.setObjectName(u"scrollArea_8")
        self.scrollArea_8.setWidgetResizable(True)
        self.scrollAreaWidgetContents_5 = QWidget()
        self.scrollAreaWidgetContents_5.setObjectName(u"scrollAreaWidgetContents_5")
        self.scrollAreaWidgetContents_5.setGeometry(QRect(0, 0, 288, 402))
        self.formLayout_2 = QFormLayout(self.scrollAreaWidgetContents_5)
        self.formLayout_2.setObjectName(u"formLayout_2")
        self.label_3 = QLabel(self.scrollAreaWidgetContents_5)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setFont(font7)

        self.formLayout_2.setWidget(0, QFormLayout.ItemRole.LabelRole, self.label_3)

        self.equipo = QLineEdit(self.scrollAreaWidgetContents_5)
        self.equipo.setObjectName(u"equipo")
        self.equipo.setFont(font7)

        self.formLayout_2.setWidget(0, QFormLayout.ItemRole.FieldRole, self.equipo)

        self.label_24 = QLabel(self.scrollAreaWidgetContents_5)
        self.label_24.setObjectName(u"label_24")
        self.label_24.setFont(font7)

        self.formLayout_2.setWidget(1, QFormLayout.ItemRole.LabelRole, self.label_24)

        self.marca = QLineEdit(self.scrollAreaWidgetContents_5)
        self.marca.setObjectName(u"marca")
        self.marca.setFont(font7)

        self.formLayout_2.setWidget(1, QFormLayout.ItemRole.FieldRole, self.marca)

        self.label_25 = QLabel(self.scrollAreaWidgetContents_5)
        self.label_25.setObjectName(u"label_25")
        self.label_25.setFont(font7)

        self.formLayout_2.setWidget(2, QFormLayout.ItemRole.LabelRole, self.label_25)

        self.modelo = QLineEdit(self.scrollAreaWidgetContents_5)
        self.modelo.setObjectName(u"modelo")
        self.modelo.setFont(font7)

        self.formLayout_2.setWidget(2, QFormLayout.ItemRole.FieldRole, self.modelo)

        self.label_26 = QLabel(self.scrollAreaWidgetContents_5)
        self.label_26.setObjectName(u"label_26")
        self.label_26.setFont(font7)

        self.formLayout_2.setWidget(3, QFormLayout.ItemRole.LabelRole, self.label_26)

        self.nserie = QLineEdit(self.scrollAreaWidgetContents_5)
        self.nserie.setObjectName(u"nserie")
        self.nserie.setFont(font7)

        self.formLayout_2.setWidget(3, QFormLayout.ItemRole.FieldRole, self.nserie)

        self.label_33 = QLabel(self.scrollAreaWidgetContents_5)
        self.label_33.setObjectName(u"label_33")
        self.label_33.setFont(font7)

        self.formLayout_2.setWidget(4, QFormLayout.ItemRole.LabelRole, self.label_33)

        self.falla = QLineEdit(self.scrollAreaWidgetContents_5)
        self.falla.setObjectName(u"falla")
        self.falla.setFont(font7)

        self.formLayout_2.setWidget(4, QFormLayout.ItemRole.FieldRole, self.falla)

        self.label_34 = QLabel(self.scrollAreaWidgetContents_5)
        self.label_34.setObjectName(u"label_34")
        font8 = QFont()
        font8.setPointSize(11)
        self.label_34.setFont(font8)

        self.formLayout_2.setWidget(5, QFormLayout.ItemRole.LabelRole, self.label_34)

        self.infadi = QTextEdit(self.scrollAreaWidgetContents_5)
        self.infadi.setObjectName(u"infadi")
        self.infadi.setMaximumSize(QSize(16777215, 80))
        self.infadi.setFont(font7)

        self.formLayout_2.setWidget(5, QFormLayout.ItemRole.FieldRole, self.infadi)

        self.label_27 = QLabel(self.scrollAreaWidgetContents_5)
        self.label_27.setObjectName(u"label_27")

        self.formLayout_2.setWidget(6, QFormLayout.ItemRole.LabelRole, self.label_27)

        self.restatus = QLineEdit(self.scrollAreaWidgetContents_5)
        self.restatus.setObjectName(u"restatus")
        self.restatus.setReadOnly(True)

        self.formLayout_2.setWidget(6, QFormLayout.ItemRole.FieldRole, self.restatus)

        self.label_35 = QLabel(self.scrollAreaWidgetContents_5)
        self.label_35.setObjectName(u"label_35")
        self.label_35.setFont(font7)

        self.formLayout_2.setWidget(7, QFormLayout.ItemRole.LabelRole, self.label_35)

        self.widget_30 = QWidget(self.scrollAreaWidgetContents_5)
        self.widget_30.setObjectName(u"widget_30")
        self.horizontalLayout_4 = QHBoxLayout(self.widget_30)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.scrollArea_4 = QScrollArea(self.widget_30)
        self.scrollArea_4.setObjectName(u"scrollArea_4")
        self.scrollArea_4.setMinimumSize(QSize(100, 80))
        self.scrollArea_4.setWidgetResizable(True)
        self.accesorios = QWidget()
        self.accesorios.setObjectName(u"accesorios")
        self.accesorios.setGeometry(QRect(0, 0, 159, 259))
        self.verticalLayout_17 = QVBoxLayout(self.accesorios)
        self.verticalLayout_17.setObjectName(u"verticalLayout_17")
        self.cableac = QCheckBox(self.accesorios)
        self.cableac.setObjectName(u"cableac")

        self.verticalLayout_17.addWidget(self.cableac)

        self.controlr = QCheckBox(self.accesorios)
        self.controlr.setObjectName(u"controlr")

        self.verticalLayout_17.addWidget(self.controlr)

        self.eliminador = QCheckBox(self.accesorios)
        self.eliminador.setObjectName(u"eliminador")

        self.verticalLayout_17.addWidget(self.eliminador)

        self.base = QCheckBox(self.accesorios)
        self.base.setObjectName(u"base")

        self.verticalLayout_17.addWidget(self.base)

        self.basepared = QCheckBox(self.accesorios)
        self.basepared.setObjectName(u"basepared")

        self.verticalLayout_17.addWidget(self.basepared)

        self.pilas = QCheckBox(self.accesorios)
        self.pilas.setObjectName(u"pilas")

        self.verticalLayout_17.addWidget(self.pilas)

        self.cables = QCheckBox(self.accesorios)
        self.cables.setObjectName(u"cables")

        self.verticalLayout_17.addWidget(self.cables)

        self.accotro = QLineEdit(self.accesorios)
        self.accotro.setObjectName(u"accotro")

        self.verticalLayout_17.addWidget(self.accotro)

        self.scrollArea_4.setWidget(self.accesorios)

        self.horizontalLayout_4.addWidget(self.scrollArea_4)


        self.formLayout_2.setWidget(7, QFormLayout.ItemRole.FieldRole, self.widget_30)

        self.scrollArea_8.setWidget(self.scrollAreaWidgetContents_5)

        self.verticalLayout_49.addWidget(self.scrollArea_8)

        self.widget_42 = QWidget(self.infoequipo)
        self.widget_42.setObjectName(u"widget_42")
        self.horizontalLayout_31 = QHBoxLayout(self.widget_42)
        self.horizontalLayout_31.setObjectName(u"horizontalLayout_31")
        self.horizontalLayout_31.setContentsMargins(0, 2, -1, 0)

        self.verticalLayout_49.addWidget(self.widget_42)


        self.horizontalLayout_22.addWidget(self.infoequipo)

        self.groupBox = QGroupBox(self.widget_29)
        self.groupBox.setObjectName(u"groupBox")
        self.groupBox.setMinimumSize(QSize(0, 0))
        self.groupBox.setFont(font7)
        self.gridLayout = QGridLayout(self.groupBox)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setVerticalSpacing(2)
        self.gridLayout.setContentsMargins(-1, 0, -1, 2)
        self.rnombre = QComboBox(self.groupBox)
        self.rnombre.setObjectName(u"rnombre")
        self.rnombre.setMaximumSize(QSize(250, 16777215))
        self.rnombre.setEditable(True)
        self.rnombre.setFrame(True)

        self.gridLayout.addWidget(self.rnombre, 2, 0, 1, 1)

        self.label_47 = QLabel(self.groupBox)
        self.label_47.setObjectName(u"label_47")
        self.label_47.setMinimumSize(QSize(10, 10))
        self.label_47.setMaximumSize(QSize(50, 50))
        self.label_47.setPixmap(QPixmap(u"../../../.designer/backup/iconos/clienteint.ico"))
        self.label_47.setScaledContents(True)

        self.gridLayout.addWidget(self.label_47, 0, 0, 1, 1)

        self.label_46 = QLabel(self.groupBox)
        self.label_46.setObjectName(u"label_46")
        self.label_46.setFont(font7)

        self.gridLayout.addWidget(self.label_46, 9, 0, 1, 1)

        self.verticalSpacer_4 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.gridLayout.addItem(self.verticalSpacer_4, 5, 0, 1, 1)

        self.remail = QLineEdit(self.groupBox)
        self.remail.setObjectName(u"remail")
        self.remail.setMaximumSize(QSize(250, 16777215))
        self.remail.setFont(font7)
        self.remail.setReadOnly(True)

        self.gridLayout.addWidget(self.remail, 7, 1, 1, 1)

        self.rrfc = QLineEdit(self.groupBox)
        self.rrfc.setObjectName(u"rrfc")
        self.rrfc.setMaximumSize(QSize(250, 16777215))
        self.rrfc.setFont(font7)
        self.rrfc.setReadOnly(True)

        self.gridLayout.addWidget(self.rrfc, 10, 0, 1, 1)

        self.label_45 = QLabel(self.groupBox)
        self.label_45.setObjectName(u"label_45")
        self.label_45.setFont(font7)

        self.gridLayout.addWidget(self.label_45, 6, 1, 1, 1)

        self.rtelefono = QLineEdit(self.groupBox)
        self.rtelefono.setObjectName(u"rtelefono")
        self.rtelefono.setMaximumSize(QSize(250, 16777215))
        self.rtelefono.setFont(font7)
        self.rtelefono.setReadOnly(True)

        self.gridLayout.addWidget(self.rtelefono, 2, 1, 1, 1)

        self.label_44 = QLabel(self.groupBox)
        self.label_44.setObjectName(u"label_44")
        self.label_44.setFont(font7)

        self.gridLayout.addWidget(self.label_44, 6, 0, 1, 1)

        self.label_43 = QLabel(self.groupBox)
        self.label_43.setObjectName(u"label_43")
        self.label_43.setFont(font7)

        self.gridLayout.addWidget(self.label_43, 1, 1, 1, 1)

        self.rdireccion = QLineEdit(self.groupBox)
        self.rdireccion.setObjectName(u"rdireccion")
        self.rdireccion.setMaximumSize(QSize(250, 16777215))
        self.rdireccion.setFont(font7)
        self.rdireccion.setReadOnly(True)

        self.gridLayout.addWidget(self.rdireccion, 7, 0, 1, 1)

        self.label_42 = QLabel(self.groupBox)
        self.label_42.setObjectName(u"label_42")
        self.label_42.setFont(font7)

        self.gridLayout.addWidget(self.label_42, 1, 0, 1, 1)

        self.widget_31 = QWidget(self.groupBox)
        self.widget_31.setObjectName(u"widget_31")
        self.horizontalLayout_24 = QHBoxLayout(self.widget_31)
        self.horizontalLayout_24.setObjectName(u"horizontalLayout_24")
        self.horizontalLayout_24.setContentsMargins(-1, 0, -1, 0)
        self.rbtneditaclient = QToolButton(self.widget_31)
        self.rbtneditaclient.setObjectName(u"rbtneditaclient")
        self.rbtneditaclient.setMinimumSize(QSize(0, 0))
        icon12 = QIcon()
        icon12.addFile(u":/iconos/iconos/Edit_User.ico", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.rbtneditaclient.setIcon(icon12)
        self.rbtneditaclient.setIconSize(QSize(30, 30))
        self.rbtneditaclient.setToolButtonStyle(Qt.ToolButtonStyle.ToolButtonTextUnderIcon)

        self.horizontalLayout_24.addWidget(self.rbtneditaclient)

        self.btnnuevocliente = QToolButton(self.widget_31)
        self.btnnuevocliente.setObjectName(u"btnnuevocliente")
        self.btnnuevocliente.setMinimumSize(QSize(0, 0))
        icon13 = QIcon()
        icon13.addFile(u":/iconos/iconos/Add_User.ico", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.btnnuevocliente.setIcon(icon13)
        self.btnnuevocliente.setIconSize(QSize(30, 30))
        self.btnnuevocliente.setToolButtonStyle(Qt.ToolButtonStyle.ToolButtonTextUnderIcon)

        self.horizontalLayout_24.addWidget(self.btnnuevocliente)


        self.gridLayout.addWidget(self.widget_31, 15, 0, 1, 1)

        self.verticalSpacer_6 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.gridLayout.addItem(self.verticalSpacer_6, 12, 0, 1, 1)

        self.verticalSpacer_5 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.gridLayout.addItem(self.verticalSpacer_5, 8, 0, 1, 1)


        self.horizontalLayout_22.addWidget(self.groupBox)


        self.verticalLayout_15.addWidget(self.widget_29)

        self.widget_33 = QWidget(self.widget_22)
        self.widget_33.setObjectName(u"widget_33")
        self.horizontalLayout_23 = QHBoxLayout(self.widget_33)
        self.horizontalLayout_23.setSpacing(4)
        self.horizontalLayout_23.setObjectName(u"horizontalLayout_23")
        self.horizontalLayout_23.setContentsMargins(-1, 5, -1, 0)
        self.horizontalSpacer_2 = QSpacerItem(80, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_23.addItem(self.horizontalSpacer_2)

        self.btninicior = QToolButton(self.widget_33)
        self.btninicior.setObjectName(u"btninicior")
        self.btninicior.setMinimumSize(QSize(62, 0))
        icon14 = QIcon()
        icon14.addFile(u":/iconos/iconos/inicio.ico", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.btninicior.setIcon(icon14)
        self.btninicior.setIconSize(QSize(40, 40))
        self.btninicior.setPopupMode(QToolButton.ToolButtonPopupMode.DelayedPopup)
        self.btninicior.setToolButtonStyle(Qt.ToolButtonStyle.ToolButtonTextUnderIcon)
        self.btninicior.setArrowType(Qt.ArrowType.NoArrow)

        self.horizontalLayout_23.addWidget(self.btninicior)

        self.btnant = QToolButton(self.widget_33)
        self.btnant.setObjectName(u"btnant")
        self.btnant.setMinimumSize(QSize(62, 0))
        self.btnant.setIcon(icon9)
        self.btnant.setIconSize(QSize(40, 40))
        self.btnant.setToolButtonStyle(Qt.ToolButtonStyle.ToolButtonTextUnderIcon)

        self.horizontalLayout_23.addWidget(self.btnant)

        self.btnsig = QToolButton(self.widget_33)
        self.btnsig.setObjectName(u"btnsig")
        icon15 = QIcon()
        icon15.addFile(u":/iconos/iconos/siguiente.ico", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.btnsig.setIcon(icon15)
        self.btnsig.setIconSize(QSize(40, 40))
        self.btnsig.setToolButtonStyle(Qt.ToolButtonStyle.ToolButtonTextUnderIcon)

        self.horizontalLayout_23.addWidget(self.btnsig)

        self.btnfin = QToolButton(self.widget_33)
        self.btnfin.setObjectName(u"btnfin")
        self.btnfin.setMinimumSize(QSize(62, 0))
        icon16 = QIcon()
        icon16.addFile(u":/iconos/iconos/fin.ico", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.btnfin.setIcon(icon16)
        self.btnfin.setIconSize(QSize(40, 40))
        self.btnfin.setToolButtonStyle(Qt.ToolButtonStyle.ToolButtonTextUnderIcon)

        self.horizontalLayout_23.addWidget(self.btnfin)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_23.addItem(self.horizontalSpacer)


        self.verticalLayout_15.addWidget(self.widget_33)

        self.widget_28 = QWidget(self.widget_22)
        self.widget_28.setObjectName(u"widget_28")
        self.horizontalLayout_21 = QHBoxLayout(self.widget_28)
        self.horizontalLayout_21.setObjectName(u"horizontalLayout_21")
        self.horizontalLayout_21.setContentsMargins(-1, -1, -1, 0)
        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_21.addItem(self.horizontalSpacer_3)

        self.btnnuevo = QToolButton(self.widget_28)
        self.btnnuevo.setObjectName(u"btnnuevo")
        self.btnnuevo.setMinimumSize(QSize(62, 0))
        icon17 = QIcon()
        icon17.addFile(u":/iconos/iconos/nuevo.ico", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.btnnuevo.setIcon(icon17)
        self.btnnuevo.setIconSize(QSize(40, 40))
        self.btnnuevo.setToolButtonStyle(Qt.ToolButtonStyle.ToolButtonTextUnderIcon)

        self.horizontalLayout_21.addWidget(self.btnnuevo)

        self.btneliminar = QToolButton(self.widget_28)
        self.btneliminar.setObjectName(u"btneliminar")
        self.btneliminar.setMinimumSize(QSize(62, 0))
        icon18 = QIcon()
        icon18.addFile(u":/iconos/iconos/eliminar.ico", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.btneliminar.setIcon(icon18)
        self.btneliminar.setIconSize(QSize(40, 40))
        self.btneliminar.setToolButtonStyle(Qt.ToolButtonStyle.ToolButtonTextUnderIcon)

        self.horizontalLayout_21.addWidget(self.btneliminar)

        self.btnguardar = QToolButton(self.widget_28)
        self.btnguardar.setObjectName(u"btnguardar")
        self.btnguardar.setMinimumSize(QSize(62, 0))
        icon19 = QIcon()
        icon19.addFile(u":/iconos/iconos/guardar.ico", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.btnguardar.setIcon(icon19)
        self.btnguardar.setIconSize(QSize(40, 40))
        self.btnguardar.setToolButtonStyle(Qt.ToolButtonStyle.ToolButtonTextUnderIcon)

        self.horizontalLayout_21.addWidget(self.btnguardar)

        self.horizontalSpacer_4 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_21.addItem(self.horizontalSpacer_4)


        self.verticalLayout_15.addWidget(self.widget_28)


        self.horizontalLayout_33.addWidget(self.widget_22)

        icon20 = QIcon(QIcon.fromTheme(u"accessories-dictionary"))
        self.tabregistros.addTab(self.tab_3, icon20, "")
        self.tab_4 = QWidget()
        self.tab_4.setObjectName(u"tab_4")
        self.tab_4.setFont(font7)
        self.verticalLayout_29 = QVBoxLayout(self.tab_4)
        self.verticalLayout_29.setObjectName(u"verticalLayout_29")
        self.widget_48 = QWidget(self.tab_4)
        self.widget_48.setObjectName(u"widget_48")
        self.horizontalLayout_36 = QHBoxLayout(self.widget_48)
        self.horizontalLayout_36.setObjectName(u"horizontalLayout_36")
        self.horizontalLayout_36.setContentsMargins(-1, -1, -1, 0)
        self.msjreg = QLabel(self.widget_48)
        self.msjreg.setObjectName(u"msjreg")

        self.horizontalLayout_36.addWidget(self.msjreg)

        self.horizontalSpacer_9 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_36.addItem(self.horizontalSpacer_9)

        self.widget_49 = QWidget(self.widget_48)
        self.widget_49.setObjectName(u"widget_49")
        self.horizontalLayout_35 = QHBoxLayout(self.widget_49)
        self.horizontalLayout_35.setObjectName(u"horizontalLayout_35")
        self.horizontalLayout_35.setContentsMargins(0, -1, -1, 0)
        self.buscar = QToolButton(self.widget_49)
        self.buscar.setObjectName(u"buscar")
        self.buscar.setEnabled(True)
        icon21 = QIcon(QIcon.fromTheme(u"edit-find"))
        self.buscar.setIcon(icon21)
        self.buscar.setIconSize(QSize(22, 22))
        self.buscar.setToolButtonStyle(Qt.ToolButtonStyle.ToolButtonIconOnly)

        self.horizontalLayout_35.addWidget(self.buscar)

        self.buscarreg = QLineEdit(self.widget_49)
        self.buscarreg.setObjectName(u"buscarreg")
        font9 = QFont()
        font9.setPointSize(12)
        font9.setWeight(QFont.Medium)
        font9.setKerning(True)
        self.buscarreg.setFont(font9)
        self.buscarreg.setFocusPolicy(Qt.FocusPolicy.StrongFocus)
        self.buscarreg.setAutoFillBackground(False)
        self.buscarreg.setClearButtonEnabled(True)

        self.horizontalLayout_35.addWidget(self.buscarreg)


        self.horizontalLayout_36.addWidget(self.widget_49)


        self.verticalLayout_29.addWidget(self.widget_48)

        self.tableViewregistros = QTableView(self.tab_4)
        self.tableViewregistros.setObjectName(u"tableViewregistros")
        self.tableViewregistros.setSelectionBehavior(QAbstractItemView.SelectionBehavior.SelectRows)
        self.tableViewregistros.horizontalHeader().setStretchLastSection(True)

        self.verticalLayout_29.addWidget(self.tableViewregistros)

        icon22 = QIcon(QIcon.fromTheme(u"user-bookmarks"))
        self.tabregistros.addTab(self.tab_4, icon22, "")
        self.tab_10 = QWidget()
        self.tab_10.setObjectName(u"tab_10")
        self.tab_10.setEnabled(True)
        self.verticalLayout_34 = QVBoxLayout(self.tab_10)
        self.verticalLayout_34.setObjectName(u"verticalLayout_34")
        self.scrollArea_5 = QScrollArea(self.tab_10)
        self.scrollArea_5.setObjectName(u"scrollArea_5")
        self.scrollArea_5.setWidgetResizable(True)
        self.scrollAreaWidgetContents_3 = QWidget()
        self.scrollAreaWidgetContents_3.setObjectName(u"scrollAreaWidgetContents_3")
        self.scrollAreaWidgetContents_3.setGeometry(QRect(0, 0, 636, 1142))
        self.verticalLayout_37 = QVBoxLayout(self.scrollAreaWidgetContents_3)
        self.verticalLayout_37.setObjectName(u"verticalLayout_37")
        self.groupBox_11 = QGroupBox(self.scrollAreaWidgetContents_3)
        self.groupBox_11.setObjectName(u"groupBox_11")
        self.groupBox_11.setEnabled(True)
        self.groupBox_11.setMinimumSize(QSize(0, 0))
        self.groupBox_11.setMaximumSize(QSize(16777215, 140))
        self.groupBox_11.setFont(font7)
        self.gridLayout_23 = QGridLayout(self.groupBox_11)
        self.gridLayout_23.setObjectName(u"gridLayout_23")
        self.label_111 = QLabel(self.groupBox_11)
        self.label_111.setObjectName(u"label_111")
        self.label_111.setFont(font7)

        self.gridLayout_23.addWidget(self.label_111, 0, 0, 1, 1)

        self.equipo_2 = QLineEdit(self.groupBox_11)
        self.equipo_2.setObjectName(u"equipo_2")
        self.equipo_2.setEnabled(True)
        self.equipo_2.setFont(font7)
        self.equipo_2.setReadOnly(True)

        self.gridLayout_23.addWidget(self.equipo_2, 0, 1, 1, 1)

        self.label_109 = QLabel(self.groupBox_11)
        self.label_109.setObjectName(u"label_109")
        self.label_109.setFont(font7)

        self.gridLayout_23.addWidget(self.label_109, 0, 2, 1, 1)

        self.marca_2 = QLineEdit(self.groupBox_11)
        self.marca_2.setObjectName(u"marca_2")
        self.marca_2.setFont(font7)
        self.marca_2.setReadOnly(True)

        self.gridLayout_23.addWidget(self.marca_2, 0, 3, 1, 1)

        self.label_112 = QLabel(self.groupBox_11)
        self.label_112.setObjectName(u"label_112")
        self.label_112.setFont(font7)

        self.gridLayout_23.addWidget(self.label_112, 1, 0, 1, 1)

        self.modelo_2 = QLineEdit(self.groupBox_11)
        self.modelo_2.setObjectName(u"modelo_2")
        self.modelo_2.setFont(font7)
        self.modelo_2.setReadOnly(True)

        self.gridLayout_23.addWidget(self.modelo_2, 1, 1, 1, 1)

        self.label_108 = QLabel(self.groupBox_11)
        self.label_108.setObjectName(u"label_108")
        self.label_108.setFont(font7)

        self.gridLayout_23.addWidget(self.label_108, 1, 2, 1, 1)

        self.nserie_2 = QLineEdit(self.groupBox_11)
        self.nserie_2.setObjectName(u"nserie_2")
        self.nserie_2.setFont(font7)
        self.nserie_2.setReadOnly(True)

        self.gridLayout_23.addWidget(self.nserie_2, 1, 3, 1, 1)


        self.verticalLayout_37.addWidget(self.groupBox_11)

        self.groupBox_13 = QGroupBox(self.scrollAreaWidgetContents_3)
        self.groupBox_13.setObjectName(u"groupBox_13")
        self.groupBox_13.setMinimumSize(QSize(0, 0))
        self.groupBox_13.setFont(font7)
        self.gridLayout_26 = QGridLayout(self.groupBox_13)
        self.gridLayout_26.setObjectName(u"gridLayout_26")
        self.gridLayout_26.setContentsMargins(-1, -1, -1, 0)
        self.label_121 = QLabel(self.groupBox_13)
        self.label_121.setObjectName(u"label_121")
        self.label_121.setFont(font7)

        self.gridLayout_26.addWidget(self.label_121, 1, 0, 1, 1)

        self.label_117 = QLabel(self.groupBox_13)
        self.label_117.setObjectName(u"label_117")
        self.label_117.setFont(font7)

        self.gridLayout_26.addWidget(self.label_117, 9, 0, 1, 1)

        self.label_118 = QLabel(self.groupBox_13)
        self.label_118.setObjectName(u"label_118")
        self.label_118.setFont(font7)

        self.gridLayout_26.addWidget(self.label_118, 6, 2, 1, 1)

        self.email_2 = QLineEdit(self.groupBox_13)
        self.email_2.setObjectName(u"email_2")
        self.email_2.setMaximumSize(QSize(16777215, 16777215))
        self.email_2.setFont(font7)
        self.email_2.setReadOnly(True)

        self.gridLayout_26.addWidget(self.email_2, 6, 3, 1, 1)

        self.label_119 = QLabel(self.groupBox_13)
        self.label_119.setObjectName(u"label_119")
        self.label_119.setFont(font7)

        self.gridLayout_26.addWidget(self.label_119, 6, 0, 1, 1)

        self.direccion_2 = QLineEdit(self.groupBox_13)
        self.direccion_2.setObjectName(u"direccion_2")
        self.direccion_2.setMaximumSize(QSize(16777215, 16777215))
        self.direccion_2.setFont(font7)
        self.direccion_2.setReadOnly(True)

        self.gridLayout_26.addWidget(self.direccion_2, 6, 1, 1, 1)

        self.verticalSpacer_9 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.gridLayout_26.addItem(self.verticalSpacer_9, 12, 0, 1, 1)

        self.telefono_2 = QLineEdit(self.groupBox_13)
        self.telefono_2.setObjectName(u"telefono_2")
        self.telefono_2.setMaximumSize(QSize(16777215, 16777215))
        self.telefono_2.setFont(font7)
        self.telefono_2.setReadOnly(True)

        self.gridLayout_26.addWidget(self.telefono_2, 1, 3, 1, 1)

        self.verticalSpacer_14 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.gridLayout_26.addItem(self.verticalSpacer_14, 8, 0, 1, 1)

        self.widget_64 = QWidget(self.groupBox_13)
        self.widget_64.setObjectName(u"widget_64")
        self.horizontalLayout_47 = QHBoxLayout(self.widget_64)
        self.horizontalLayout_47.setObjectName(u"horizontalLayout_47")

        self.gridLayout_26.addWidget(self.widget_64, 15, 0, 1, 1)

        self.verticalSpacer_8 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.gridLayout_26.addItem(self.verticalSpacer_8, 5, 0, 1, 1)

        self.rfc_2 = QLineEdit(self.groupBox_13)
        self.rfc_2.setObjectName(u"rfc_2")
        self.rfc_2.setMaximumSize(QSize(16777215, 16777215))
        self.rfc_2.setFont(font7)
        self.rfc_2.setReadOnly(True)

        self.gridLayout_26.addWidget(self.rfc_2, 9, 1, 1, 1)

        self.label_116 = QLabel(self.groupBox_13)
        self.label_116.setObjectName(u"label_116")
        self.label_116.setMinimumSize(QSize(10, 10))
        self.label_116.setMaximumSize(QSize(50, 50))
        self.label_116.setPixmap(QPixmap(u"../../../.designer/backup/iconos/clienteint.ico"))
        self.label_116.setScaledContents(True)

        self.gridLayout_26.addWidget(self.label_116, 0, 0, 1, 1)

        self.label_120 = QLabel(self.groupBox_13)
        self.label_120.setObjectName(u"label_120")
        self.label_120.setFont(font7)

        self.gridLayout_26.addWidget(self.label_120, 1, 2, 1, 1)

        self.nombre_2 = QLineEdit(self.groupBox_13)
        self.nombre_2.setObjectName(u"nombre_2")

        self.gridLayout_26.addWidget(self.nombre_2, 1, 1, 1, 1)


        self.verticalLayout_37.addWidget(self.groupBox_13)

        self.groupBox_9 = QGroupBox(self.scrollAreaWidgetContents_3)
        self.groupBox_9.setObjectName(u"groupBox_9")
        self.groupBox_9.setFont(font7)
        self.gridLayout_19 = QGridLayout(self.groupBox_9)
        self.gridLayout_19.setObjectName(u"gridLayout_19")
        self.gridLayout_19.setHorizontalSpacing(2)
        self.gridLayout_19.setVerticalSpacing(0)
        self.gridLayout_19.setContentsMargins(-1, 0, -1, 2)
        self.widget_61 = QWidget(self.groupBox_9)
        self.widget_61.setObjectName(u"widget_61")
        self.horizontalLayout_45 = QHBoxLayout(self.widget_61)
        self.horizontalLayout_45.setObjectName(u"horizontalLayout_45")
        self.horizontalLayout_45.setContentsMargins(-1, 0, -1, 0)
        self.label_102 = QLabel(self.widget_61)
        self.label_102.setObjectName(u"label_102")

        self.horizontalLayout_45.addWidget(self.label_102)

        self.rep_2 = QLabel(self.widget_61)
        self.rep_2.setObjectName(u"rep_2")

        self.horizontalLayout_45.addWidget(self.rep_2)

        self.label_103 = QLabel(self.widget_61)
        self.label_103.setObjectName(u"label_103")

        self.horizontalLayout_45.addWidget(self.label_103)

        self.rde_2 = QLabel(self.widget_61)
        self.rde_2.setObjectName(u"rde_2")

        self.horizontalLayout_45.addWidget(self.rde_2)

        self.horizontalSpacer_23 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_45.addItem(self.horizontalSpacer_23)

        self.repant_2 = QToolButton(self.widget_61)
        self.repant_2.setObjectName(u"repant_2")
        icon23 = QIcon(QIcon.fromTheme(u"media-seek-backward"))
        self.repant_2.setIcon(icon23)

        self.horizontalLayout_45.addWidget(self.repant_2)

        self.repsig_2 = QToolButton(self.widget_61)
        self.repsig_2.setObjectName(u"repsig_2")
        icon24 = QIcon(QIcon.fromTheme(u"media-seek-forward"))
        self.repsig_2.setIcon(icon24)

        self.horizontalLayout_45.addWidget(self.repsig_2)


        self.gridLayout_19.addWidget(self.widget_61, 1, 0, 1, 1)

        self.widget_59 = QWidget(self.groupBox_9)
        self.widget_59.setObjectName(u"widget_59")
        self.gridLayout_20 = QGridLayout(self.widget_59)
        self.gridLayout_20.setSpacing(1)
        self.gridLayout_20.setObjectName(u"gridLayout_20")
        self.gridLayout_20.setContentsMargins(-1, 0, -1, 0)

        self.gridLayout_19.addWidget(self.widget_59, 6, 0, 1, 1)

        self.widget_58 = QWidget(self.groupBox_9)
        self.widget_58.setObjectName(u"widget_58")
        self.horizontalLayout_42 = QHBoxLayout(self.widget_58)
        self.horizontalLayout_42.setObjectName(u"horizontalLayout_42")
        self.horizontalLayout_42.setContentsMargins(-1, 0, -1, 0)

        self.gridLayout_19.addWidget(self.widget_58, 4, 0, 1, 1)

        self.groupBox_12 = QGroupBox(self.groupBox_9)
        self.groupBox_12.setObjectName(u"groupBox_12")
        self.gridLayout_24 = QGridLayout(self.groupBox_12)
        self.gridLayout_24.setObjectName(u"gridLayout_24")
        self.total_2 = QDoubleSpinBox(self.groupBox_12)
        self.total_2.setObjectName(u"total_2")
        self.total_2.setWrapping(False)
        self.total_2.setFrame(True)
        self.total_2.setButtonSymbols(QAbstractSpinBox.ButtonSymbols.NoButtons)
        self.total_2.setAccelerated(False)
        self.total_2.setProperty(u"showGroupSeparator", False)
        self.total_2.setMaximum(999999.989999999990687)

        self.gridLayout_24.addWidget(self.total_2, 4, 3, 1, 1)

        self.servtec_2 = QDoubleSpinBox(self.groupBox_12)
        self.servtec_2.setObjectName(u"servtec_2")
        self.servtec_2.setButtonSymbols(QAbstractSpinBox.ButtonSymbols.NoButtons)
        self.servtec_2.setMaximum(999999.989999999990687)

        self.gridLayout_24.addWidget(self.servtec_2, 3, 3, 1, 1)

        self.label_100 = QLabel(self.groupBox_12)
        self.label_100.setObjectName(u"label_100")
        self.label_100.setMaximumSize(QSize(55, 16777215))

        self.gridLayout_24.addWidget(self.label_100, 2, 2, 1, 1)

        self.horizontalSpacer_22 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_24.addItem(self.horizontalSpacer_22, 0, 1, 1, 3)

        self.groupBox_10 = QGroupBox(self.groupBox_12)
        self.groupBox_10.setObjectName(u"groupBox_10")
        self.groupBox_10.setMinimumSize(QSize(0, 0))
        self.gridLayout_21 = QGridLayout(self.groupBox_10)
        self.gridLayout_21.setObjectName(u"gridLayout_21")
        self.gridLayout_21.setVerticalSpacing(0)
        self.gridLayout_21.setContentsMargins(-1, 0, 0, -1)
        self.label_97 = QLabel(self.groupBox_10)
        self.label_97.setObjectName(u"label_97")
        self.label_97.setMinimumSize(QSize(0, 0))
        self.label_97.setMaximumSize(QSize(16777215, 16777215))
        self.label_97.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)
        self.label_97.setMargin(0)

        self.gridLayout_21.addWidget(self.label_97, 1, 0, 1, 1)

        self.widget_60 = QWidget(self.groupBox_10)
        self.widget_60.setObjectName(u"widget_60")
        self.horizontalLayout_44 = QHBoxLayout(self.widget_60)
        self.horizontalLayout_44.setObjectName(u"horizontalLayout_44")
        self.repuestos_2 = QTableWidget(self.widget_60)
        if (self.repuestos_2.columnCount() < 2):
            self.repuestos_2.setColumnCount(2)
        __qtablewidgetitem = QTableWidgetItem()
        self.repuestos_2.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.repuestos_2.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        if (self.repuestos_2.rowCount() < 1):
            self.repuestos_2.setRowCount(1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.repuestos_2.setVerticalHeaderItem(0, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.repuestos_2.setItem(0, 0, __qtablewidgetitem3)
        __qtablewidgetitem4 = QTableWidgetItem()
        __qtablewidgetitem4.setTextAlignment(Qt.AlignTrailing|Qt.AlignVCenter)
        self.repuestos_2.setItem(0, 1, __qtablewidgetitem4)
        self.repuestos_2.setObjectName(u"repuestos_2")
        self.repuestos_2.setMinimumSize(QSize(0, 0))
        font10 = QFont()
        font10.setPointSize(9)
        self.repuestos_2.setFont(font10)
        self.repuestos_2.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.repuestos_2.setFrameShape(QFrame.Shape.StyledPanel)
        self.repuestos_2.setEditTriggers(QAbstractItemView.EditTrigger.AnyKeyPressed|QAbstractItemView.EditTrigger.DoubleClicked|QAbstractItemView.EditTrigger.EditKeyPressed)
        self.repuestos_2.setAlternatingRowColors(False)
        self.repuestos_2.setSelectionBehavior(QAbstractItemView.SelectionBehavior.SelectRows)
        self.repuestos_2.setShowGrid(True)
        self.repuestos_2.setGridStyle(Qt.PenStyle.SolidLine)
        self.repuestos_2.setSortingEnabled(False)
        self.repuestos_2.setWordWrap(True)
        self.repuestos_2.horizontalHeader().setVisible(True)
        self.repuestos_2.horizontalHeader().setCascadingSectionResizes(False)
        self.repuestos_2.horizontalHeader().setProperty(u"showSortIndicator", False)
        self.repuestos_2.horizontalHeader().setStretchLastSection(True)
        self.repuestos_2.verticalHeader().setVisible(True)
        self.repuestos_2.verticalHeader().setCascadingSectionResizes(False)
        self.repuestos_2.verticalHeader().setProperty(u"showSortIndicator", False)
        self.repuestos_2.verticalHeader().setStretchLastSection(False)

        self.horizontalLayout_44.addWidget(self.repuestos_2)

        self.anadir_2 = QToolButton(self.widget_60)
        self.anadir_2.setObjectName(u"anadir_2")
        self.anadir_2.setFont(font2)
        self.anadir_2.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        icon25 = QIcon()
        icon25.addFile(u":/iconos/iconos/rep.ico", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.anadir_2.setIcon(icon25)
        self.anadir_2.setIconSize(QSize(40, 40))
        self.anadir_2.setToolButtonStyle(Qt.ToolButtonStyle.ToolButtonTextUnderIcon)

        self.horizontalLayout_44.addWidget(self.anadir_2)

        self.btneliminarep_2 = QToolButton(self.widget_60)
        self.btneliminarep_2.setObjectName(u"btneliminarep_2")
        self.btneliminarep_2.setFont(font2)
        icon26 = QIcon(QIcon.fromTheme(u"edit-delete"))
        self.btneliminarep_2.setIcon(icon26)
        self.btneliminarep_2.setIconSize(QSize(35, 35))
        self.btneliminarep_2.setToolButtonStyle(Qt.ToolButtonStyle.ToolButtonTextUnderIcon)

        self.horizontalLayout_44.addWidget(self.btneliminarep_2)


        self.gridLayout_21.addWidget(self.widget_60, 0, 0, 1, 3)

        self.label_98 = QLabel(self.groupBox_10)
        self.label_98.setObjectName(u"label_98")
        self.label_98.setMinimumSize(QSize(10, 0))
        self.label_98.setMaximumSize(QSize(10, 16777215))

        self.gridLayout_21.addWidget(self.label_98, 1, 1, 1, 1)

        self.totalrep_2 = QLabel(self.groupBox_10)
        self.totalrep_2.setObjectName(u"totalrep_2")
        self.totalrep_2.setMinimumSize(QSize(0, 0))
        self.totalrep_2.setMaximumSize(QSize(160, 16777215))
        self.totalrep_2.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)

        self.gridLayout_21.addWidget(self.totalrep_2, 1, 2, 1, 1)


        self.gridLayout_24.addWidget(self.groupBox_10, 2, 0, 3, 2)

        self.label_99 = QLabel(self.groupBox_12)
        self.label_99.setObjectName(u"label_99")
        self.label_99.setMaximumSize(QSize(130, 16777215))

        self.gridLayout_24.addWidget(self.label_99, 4, 2, 1, 1)

        self.diagnostico_2 = QPlainTextEdit(self.groupBox_12)
        self.diagnostico_2.setObjectName(u"diagnostico_2")
        self.diagnostico_2.setMaximumSize(QSize(16777215, 100))
        self.diagnostico_2.setTabChangesFocus(True)

        self.gridLayout_24.addWidget(self.diagnostico_2, 1, 0, 1, 4)

        self.tecnico_2 = QComboBox(self.groupBox_12)
        self.tecnico_2.setObjectName(u"tecnico_2")

        self.gridLayout_24.addWidget(self.tecnico_2, 2, 3, 1, 1)

        self.label_101 = QLabel(self.groupBox_12)
        self.label_101.setObjectName(u"label_101")

        self.gridLayout_24.addWidget(self.label_101, 3, 2, 1, 1)

        self.stackinfrep_3 = QStackedWidget(self.groupBox_12)
        self.stackinfrep_3.setObjectName(u"stackinfrep_3")
        self.page_17 = QWidget()
        self.page_17.setObjectName(u"page_17")
        self.verticalLayout_35 = QVBoxLayout(self.page_17)
        self.verticalLayout_35.setObjectName(u"verticalLayout_35")
        self.label_104 = QLabel(self.page_17)
        self.label_104.setObjectName(u"label_104")

        self.verticalLayout_35.addWidget(self.label_104)

        self.stackinfrep_3.addWidget(self.page_17)
        self.page_18 = QWidget()
        self.page_18.setObjectName(u"page_18")
        self.gridLayout_22 = QGridLayout(self.page_18)
        self.gridLayout_22.setObjectName(u"gridLayout_22")
        self.horizontalSpacer_24 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_22.addItem(self.horizontalSpacer_24, 1, 5, 1, 1)

        self.label_105 = QLabel(self.page_18)
        self.label_105.setObjectName(u"label_105")

        self.gridLayout_22.addWidget(self.label_105, 2, 0, 1, 1)

        self.garantia_2 = QSpinBox(self.page_18)
        self.garantia_2.setObjectName(u"garantia_2")
        self.garantia_2.setMaximum(365)

        self.gridLayout_22.addWidget(self.garantia_2, 1, 4, 1, 1)

        self.label_106 = QLabel(self.page_18)
        self.label_106.setObjectName(u"label_106")

        self.gridLayout_22.addWidget(self.label_106, 1, 0, 1, 1)

        self.fecha_rep_2 = QLineEdit(self.page_18)
        self.fecha_rep_2.setObjectName(u"fecha_rep_2")
        self.fecha_rep_2.setMinimumSize(QSize(0, 0))
        self.fecha_rep_2.setMaximumSize(QSize(280, 16777215))
        self.fecha_rep_2.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)
        self.fecha_rep_2.setReadOnly(True)

        self.gridLayout_22.addWidget(self.fecha_rep_2, 1, 1, 1, 1)

        self.fecharep_2 = QDateTimeEdit(self.page_18)
        self.fecharep_2.setObjectName(u"fecharep_2")
        self.fecharep_2.setMaximumSize(QSize(20, 28))
        self.fecharep_2.setWrapping(False)
        self.fecharep_2.setReadOnly(False)
        self.fecharep_2.setButtonSymbols(QAbstractSpinBox.ButtonSymbols.NoButtons)
        self.fecharep_2.setAccelerated(True)
        self.fecharep_2.setMinimumDateTime(QDateTime(QDate(2000, 1, 1), QTime(0, 0, 0)))
        self.fecharep_2.setCalendarPopup(True)

        self.gridLayout_22.addWidget(self.fecharep_2, 1, 2, 1, 1)

        self.fechagarantia_2 = QLineEdit(self.page_18)
        self.fechagarantia_2.setObjectName(u"fechagarantia_2")
        self.fechagarantia_2.setMaximumSize(QSize(300, 16777215))
        self.fechagarantia_2.setReadOnly(True)

        self.gridLayout_22.addWidget(self.fechagarantia_2, 2, 1, 1, 2)

        self.label_107 = QLabel(self.page_18)
        self.label_107.setObjectName(u"label_107")

        self.gridLayout_22.addWidget(self.label_107, 1, 3, 1, 1)

        self.presupuesto_2 = QCheckBox(self.page_18)
        self.presupuesto_2.setObjectName(u"presupuesto_2")

        self.gridLayout_22.addWidget(self.presupuesto_2, 0, 0, 1, 1)

        self.stackinfrep_3.addWidget(self.page_18)

        self.gridLayout_24.addWidget(self.stackinfrep_3, 6, 0, 1, 4)

        self.label_96 = QLabel(self.groupBox_12)
        self.label_96.setObjectName(u"label_96")

        self.gridLayout_24.addWidget(self.label_96, 0, 0, 1, 1)


        self.gridLayout_19.addWidget(self.groupBox_12, 3, 0, 1, 1)

        self.widget_62 = QWidget(self.groupBox_9)
        self.widget_62.setObjectName(u"widget_62")
        self.gridLayout_25 = QGridLayout(self.widget_62)
        self.gridLayout_25.setObjectName(u"gridLayout_25")
        self.label_113 = QLabel(self.widget_62)
        self.label_113.setObjectName(u"label_113")
        self.label_113.setFont(font7)

        self.gridLayout_25.addWidget(self.label_113, 1, 0, 1, 1)

        self.widget_63 = QWidget(self.widget_62)
        self.widget_63.setObjectName(u"widget_63")
        self.horizontalLayout_46 = QHBoxLayout(self.widget_63)
        self.horizontalLayout_46.setObjectName(u"horizontalLayout_46")
        self.scrollArea_6 = QScrollArea(self.widget_63)
        self.scrollArea_6.setObjectName(u"scrollArea_6")
        self.scrollArea_6.setMinimumSize(QSize(0, 100))
        self.scrollArea_6.setWidgetResizable(True)
        self.accesorios_2 = QWidget()
        self.accesorios_2.setObjectName(u"accesorios_2")
        self.accesorios_2.setGeometry(QRect(0, 0, 159, 259))
        self.verticalLayout_36 = QVBoxLayout(self.accesorios_2)
        self.verticalLayout_36.setObjectName(u"verticalLayout_36")
        self.cableac_2 = QCheckBox(self.accesorios_2)
        self.cableac_2.setObjectName(u"cableac_2")

        self.verticalLayout_36.addWidget(self.cableac_2)

        self.controlr_2 = QCheckBox(self.accesorios_2)
        self.controlr_2.setObjectName(u"controlr_2")

        self.verticalLayout_36.addWidget(self.controlr_2)

        self.eliminador_2 = QCheckBox(self.accesorios_2)
        self.eliminador_2.setObjectName(u"eliminador_2")

        self.verticalLayout_36.addWidget(self.eliminador_2)

        self.base_2 = QCheckBox(self.accesorios_2)
        self.base_2.setObjectName(u"base_2")

        self.verticalLayout_36.addWidget(self.base_2)

        self.basepared_2 = QCheckBox(self.accesorios_2)
        self.basepared_2.setObjectName(u"basepared_2")

        self.verticalLayout_36.addWidget(self.basepared_2)

        self.pilas_2 = QCheckBox(self.accesorios_2)
        self.pilas_2.setObjectName(u"pilas_2")

        self.verticalLayout_36.addWidget(self.pilas_2)

        self.cables_2 = QCheckBox(self.accesorios_2)
        self.cables_2.setObjectName(u"cables_2")

        self.verticalLayout_36.addWidget(self.cables_2)

        self.accotro_2 = QLineEdit(self.accesorios_2)
        self.accotro_2.setObjectName(u"accotro_2")

        self.verticalLayout_36.addWidget(self.accotro_2)

        self.scrollArea_6.setWidget(self.accesorios_2)

        self.horizontalLayout_46.addWidget(self.scrollArea_6)


        self.gridLayout_25.addWidget(self.widget_63, 4, 3, 1, 2)

        self.infadi_2 = QTextEdit(self.widget_62)
        self.infadi_2.setObjectName(u"infadi_2")
        self.infadi_2.setMaximumSize(QSize(16777215, 80))
        self.infadi_2.setFont(font7)
        self.infadi_2.setTabChangesFocus(True)
        self.infadi_2.setReadOnly(True)

        self.gridLayout_25.addWidget(self.infadi_2, 1, 4, 1, 1)

        self.label_115 = QLabel(self.widget_62)
        self.label_115.setObjectName(u"label_115")
        self.label_115.setFont(font7)

        self.gridLayout_25.addWidget(self.label_115, 4, 2, 1, 1)

        self.falla_2 = QLineEdit(self.widget_62)
        self.falla_2.setObjectName(u"falla_2")
        self.falla_2.setFont(font7)
        self.falla_2.setReadOnly(True)

        self.gridLayout_25.addWidget(self.falla_2, 1, 1, 1, 1)

        self.estatus_2 = QLineEdit(self.widget_62)
        self.estatus_2.setObjectName(u"estatus_2")
        self.estatus_2.setReadOnly(True)

        self.gridLayout_25.addWidget(self.estatus_2, 4, 1, 1, 1)

        self.label_114 = QLabel(self.widget_62)
        self.label_114.setObjectName(u"label_114")

        self.gridLayout_25.addWidget(self.label_114, 4, 0, 1, 1)

        self.label_110 = QLabel(self.widget_62)
        self.label_110.setObjectName(u"label_110")
        self.label_110.setFont(font8)

        self.gridLayout_25.addWidget(self.label_110, 1, 2, 1, 1)

        self.label_60 = QLabel(self.widget_62)
        self.label_60.setObjectName(u"label_60")
        self.label_60.setFont(font7)

        self.gridLayout_25.addWidget(self.label_60, 0, 0, 1, 1)

        self.fecha_2 = QLabel(self.widget_62)
        self.fecha_2.setObjectName(u"fecha_2")
        self.fecha_2.setMinimumSize(QSize(100, 0))
        self.fecha_2.setMaximumSize(QSize(16777215, 25))
        self.fecha_2.setFont(font7)
        self.fecha_2.setStyleSheet(u"")
        self.fecha_2.setMargin(5)

        self.gridLayout_25.addWidget(self.fecha_2, 0, 1, 1, 1)


        self.gridLayout_19.addWidget(self.widget_62, 2, 0, 1, 1)


        self.verticalLayout_37.addWidget(self.groupBox_9)

        self.widget_65 = QWidget(self.scrollAreaWidgetContents_3)
        self.widget_65.setObjectName(u"widget_65")
        self.gridLayout_27 = QGridLayout(self.widget_65)
        self.gridLayout_27.setObjectName(u"gridLayout_27")
        self.label_122 = QLabel(self.widget_65)
        self.label_122.setObjectName(u"label_122")
        self.label_122.setFont(font7)

        self.gridLayout_27.addWidget(self.label_122, 0, 0, 1, 1)

        self.pagppend_2 = QCheckBox(self.widget_65)
        self.pagppend_2.setObjectName(u"pagppend_2")
        self.pagppend_2.setFont(font7)
        self.pagppend_2.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        icon27 = QIcon()
        icon27.addFile(u"iconos/$.ico", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.pagppend_2.setIcon(icon27)

        self.gridLayout_27.addWidget(self.pagppend_2, 4, 0, 1, 1)

        self.widget_66 = QWidget(self.widget_65)
        self.widget_66.setObjectName(u"widget_66")
        self.horizontalLayout_48 = QHBoxLayout(self.widget_66)
        self.horizontalLayout_48.setObjectName(u"horizontalLayout_48")
        self.porcentaje_2 = QLabel(self.widget_66)
        self.porcentaje_2.setObjectName(u"porcentaje_2")
        self.porcentaje_2.setFont(font7)

        self.horizontalLayout_48.addWidget(self.porcentaje_2)

        self.label_123 = QLabel(self.widget_66)
        self.label_123.setObjectName(u"label_123")
        self.label_123.setFont(font7)

        self.horizontalLayout_48.addWidget(self.label_123)

        self.btneditaporce_2 = QToolButton(self.widget_66)
        self.btneditaporce_2.setObjectName(u"btneditaporce_2")
        icon28 = QIcon()
        icon28.addFile(u":/iconos/iconos/pen.ico", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.btneditaporce_2.setIcon(icon28)
        self.btneditaporce_2.setIconSize(QSize(30, 30))
        self.btneditaporce_2.setPopupMode(QToolButton.ToolButtonPopupMode.DelayedPopup)
        self.btneditaporce_2.setToolButtonStyle(Qt.ToolButtonStyle.ToolButtonIconOnly)
        self.btneditaporce_2.setAutoRaise(True)
        self.btneditaporce_2.setArrowType(Qt.ArrowType.NoArrow)

        self.horizontalLayout_48.addWidget(self.btneditaporce_2)

        self.horizontalSpacer_25 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_48.addItem(self.horizontalSpacer_25)


        self.gridLayout_27.addWidget(self.widget_66, 3, 1, 1, 1)

        self.btnguardare_2 = QToolButton(self.widget_65)
        self.btnguardare_2.setObjectName(u"btnguardare_2")
        self.btnguardare_2.setEnabled(False)
        self.btnguardare_2.setMinimumSize(QSize(62, 0))
        self.btnguardare_2.setIcon(icon19)
        self.btnguardare_2.setIconSize(QSize(40, 40))
        self.btnguardare_2.setToolButtonStyle(Qt.ToolButtonStyle.ToolButtonTextUnderIcon)

        self.gridLayout_27.addWidget(self.btnguardare_2, 4, 4, 1, 1)

        self.fechaent = QLineEdit(self.widget_65)
        self.fechaent.setObjectName(u"fechaent")
        self.fechaent.setMinimumSize(QSize(0, 0))
        self.fechaent.setMaximumSize(QSize(280, 16777215))
        self.fechaent.setFont(font8)
        self.fechaent.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)
        self.fechaent.setReadOnly(True)

        self.gridLayout_27.addWidget(self.fechaent, 0, 1, 1, 1)

        self.horizontalSpacer_27 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_27.addItem(self.horizontalSpacer_27, 4, 1, 1, 3)

        self.label_124 = QLabel(self.widget_65)
        self.label_124.setObjectName(u"label_124")
        self.label_124.setFont(font7)

        self.gridLayout_27.addWidget(self.label_124, 3, 0, 1, 1)

        self.horizontalSpacer_26 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_27.addItem(self.horizontalSpacer_26, 0, 3, 1, 1)

        self.fechaentrega_2 = QDateTimeEdit(self.widget_65)
        self.fechaentrega_2.setObjectName(u"fechaentrega_2")
        self.fechaentrega_2.setMaximumSize(QSize(20, 28))
        self.fechaentrega_2.setWrapping(False)
        self.fechaentrega_2.setReadOnly(False)
        self.fechaentrega_2.setButtonSymbols(QAbstractSpinBox.ButtonSymbols.NoButtons)
        self.fechaentrega_2.setAccelerated(True)
        self.fechaentrega_2.setMinimumDateTime(QDateTime(QDate(2000, 1, 1), QTime(0, 0, 0)))
        self.fechaentrega_2.setCalendarPopup(True)

        self.gridLayout_27.addWidget(self.fechaentrega_2, 0, 2, 1, 1)


        self.verticalLayout_37.addWidget(self.widget_65)

        self.scrollArea_5.setWidget(self.scrollAreaWidgetContents_3)

        self.verticalLayout_34.addWidget(self.scrollArea_5)

        icon29 = QIcon(QIcon.fromTheme(u"dialog-information"))
        self.tabregistros.addTab(self.tab_10, icon29, "")

        self.verticalLayout_14.addWidget(self.tabregistros)

        self.stack.addWidget(self.page_2)
        self.page_3 = QWidget()
        self.page_3.setObjectName(u"page_3")
        self.page_3.setMaximumSize(QSize(16777215, 16777215))
        self.verticalLayout_19 = QVBoxLayout(self.page_3)
        self.verticalLayout_19.setObjectName(u"verticalLayout_19")
        self.stackreparaciones = QStackedWidget(self.page_3)
        self.stackreparaciones.setObjectName(u"stackreparaciones")
        self.page_10 = QWidget()
        self.page_10.setObjectName(u"page_10")
        self.verticalLayout_23 = QVBoxLayout(self.page_10)
        self.verticalLayout_23.setObjectName(u"verticalLayout_23")
        self.tabrepara = QTabWidget(self.page_10)
        self.tabrepara.setObjectName(u"tabrepara")
        self.tabrepara.setStyleSheet(u"#tabrepara{\n"
"		\n"
"	font: 700 11pt \"Segoe UI\";\n"
"}")
        self.tabrepara.setTabShape(QTabWidget.TabShape.Rounded)
        self.tabrepara.setIconSize(QSize(30, 30))
        self.tabrepara.setUsesScrollButtons(True)
        self.tabrepara.setDocumentMode(False)
        self.tabrepara.setMovable(True)
        self.tabrepara.setTabBarAutoHide(False)
        self.tab = QWidget()
        self.tab.setObjectName(u"tab")
        self.verticalLayout_20 = QVBoxLayout(self.tab)
        self.verticalLayout_20.setObjectName(u"verticalLayout_20")
        self.label_4 = QLabel(self.tab)
        self.label_4.setObjectName(u"label_4")
        font11 = QFont()
        font11.setPointSize(12)
        font11.setBold(True)
        self.label_4.setFont(font11)

        self.verticalLayout_20.addWidget(self.label_4)

        self.widget_81 = QWidget(self.tab)
        self.widget_81.setObjectName(u"widget_81")
        self.horizontalLayout_56 = QHBoxLayout(self.widget_81)
        self.horizontalLayout_56.setObjectName(u"horizontalLayout_56")
        self.horizontalLayout_56.setContentsMargins(-1, 0, -1, 0)
        self.filtrar = QCheckBox(self.widget_81)
        self.filtrar.setObjectName(u"filtrar")

        self.horizontalLayout_56.addWidget(self.filtrar)

        self.btneditafiltro = QToolButton(self.widget_81)
        self.btneditafiltro.setObjectName(u"btneditafiltro")
        self.btneditafiltro.setIcon(icon28)
        self.btneditafiltro.setIconSize(QSize(30, 30))
        self.btneditafiltro.setPopupMode(QToolButton.ToolButtonPopupMode.DelayedPopup)
        self.btneditafiltro.setToolButtonStyle(Qt.ToolButtonStyle.ToolButtonIconOnly)
        self.btneditafiltro.setAutoRaise(True)
        self.btneditafiltro.setArrowType(Qt.ArrowType.NoArrow)

        self.horizontalLayout_56.addWidget(self.btneditafiltro)

        self.horizontalSpacer_18 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_56.addItem(self.horizontalSpacer_18)

        self.checkmostocult = QRadioButton(self.widget_81)
        self.checkmostocult.setObjectName(u"checkmostocult")
        icon30 = QIcon()
        icon30.addFile(u":/iconos/iconos/ojo.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.checkmostocult.setIcon(icon30)
        self.checkmostocult.setIconSize(QSize(25, 25))
        self.checkmostocult.setChecked(False)

        self.horizontalLayout_56.addWidget(self.checkmostocult)


        self.verticalLayout_20.addWidget(self.widget_81)

        self.tableView = QTableView(self.tab)
        self.tableView.setObjectName(u"tableView")
        self.tableView.setEnabled(True)
        self.tableView.setContextMenuPolicy(Qt.ContextMenuPolicy.CustomContextMenu)
        self.tableView.setAlternatingRowColors(True)
        self.tableView.horizontalHeader().setCascadingSectionResizes(False)
        self.tableView.verticalHeader().setCascadingSectionResizes(True)

        self.verticalLayout_20.addWidget(self.tableView)

        self.tabrepara.addTab(self.tab, icon3, "")
        self.tab_2 = QWidget()
        self.tab_2.setObjectName(u"tab_2")
        self.verticalLayout_21 = QVBoxLayout(self.tab_2)
        self.verticalLayout_21.setObjectName(u"verticalLayout_21")
        self.widget_43 = QWidget(self.tab_2)
        self.widget_43.setObjectName(u"widget_43")
        self.verticalLayout_22 = QVBoxLayout(self.widget_43)
        self.verticalLayout_22.setSpacing(2)
        self.verticalLayout_22.setObjectName(u"verticalLayout_22")
        self.verticalLayout_22.setContentsMargins(-1, 0, -1, 0)
        self.label_57 = QLabel(self.widget_43)
        self.label_57.setObjectName(u"label_57")
        self.label_57.setFont(font11)

        self.verticalLayout_22.addWidget(self.label_57)

        self.widget_83 = QWidget(self.widget_43)
        self.widget_83.setObjectName(u"widget_83")
        self.horizontalLayout_57 = QHBoxLayout(self.widget_83)
        self.horizontalLayout_57.setObjectName(u"horizontalLayout_57")
        self.horizontalLayout_57.setContentsMargins(-1, 0, -1, 0)
        self.filtrar_2 = QCheckBox(self.widget_83)
        self.filtrar_2.setObjectName(u"filtrar_2")

        self.horizontalLayout_57.addWidget(self.filtrar_2)

        self.btneditafiltro_2 = QToolButton(self.widget_83)
        self.btneditafiltro_2.setObjectName(u"btneditafiltro_2")
        self.btneditafiltro_2.setIcon(icon28)
        self.btneditafiltro_2.setIconSize(QSize(30, 30))
        self.btneditafiltro_2.setPopupMode(QToolButton.ToolButtonPopupMode.DelayedPopup)
        self.btneditafiltro_2.setToolButtonStyle(Qt.ToolButtonStyle.ToolButtonIconOnly)
        self.btneditafiltro_2.setAutoRaise(True)
        self.btneditafiltro_2.setArrowType(Qt.ArrowType.NoArrow)

        self.horizontalLayout_57.addWidget(self.btneditafiltro_2)

        self.horizontalSpacer_20 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_57.addItem(self.horizontalSpacer_20)

        self.checkmostocult_2 = QRadioButton(self.widget_83)
        self.checkmostocult_2.setObjectName(u"checkmostocult_2")
        self.checkmostocult_2.setIcon(icon30)
        self.checkmostocult_2.setIconSize(QSize(25, 25))
        self.checkmostocult_2.setChecked(False)

        self.horizontalLayout_57.addWidget(self.checkmostocult_2)


        self.verticalLayout_22.addWidget(self.widget_83)

        self.tableView_2 = QTableView(self.widget_43)
        self.tableView_2.setObjectName(u"tableView_2")
        self.tableView_2.setContextMenuPolicy(Qt.ContextMenuPolicy.CustomContextMenu)
        self.tableView_2.setAlternatingRowColors(True)
        self.tableView_2.horizontalHeader().setCascadingSectionResizes(False)

        self.verticalLayout_22.addWidget(self.tableView_2)


        self.verticalLayout_21.addWidget(self.widget_43)

        icon31 = QIcon(QIcon.fromTheme(u"applications-development"))
        self.tabrepara.addTab(self.tab_2, icon31, "")

        self.verticalLayout_23.addWidget(self.tabrepara)

        self.stackreparaciones.addWidget(self.page_10)
        self.page_11 = QWidget()
        self.page_11.setObjectName(u"page_11")
        self.verticalLayout_26 = QVBoxLayout(self.page_11)
        self.verticalLayout_26.setObjectName(u"verticalLayout_26")
        self.groupBox_4 = QGroupBox(self.page_11)
        self.groupBox_4.setObjectName(u"groupBox_4")
        self.groupBox_4.setMinimumSize(QSize(0, 0))
        self.groupBox_4.setMaximumSize(QSize(16777215, 140))
        self.groupBox_4.setFont(font7)
        self.verticalLayout_27 = QVBoxLayout(self.groupBox_4)
        self.verticalLayout_27.setObjectName(u"verticalLayout_27")
        self.verticalLayout_27.setContentsMargins(-1, 0, -1, 2)
        self.scrollArea_7 = QScrollArea(self.groupBox_4)
        self.scrollArea_7.setObjectName(u"scrollArea_7")
        self.scrollArea_7.setWidgetResizable(True)
        self.scrollAreaWidgetContents_4 = QWidget()
        self.scrollAreaWidgetContents_4.setObjectName(u"scrollAreaWidgetContents_4")
        self.scrollAreaWidgetContents_4.setGeometry(QRect(0, 0, 551, 150))
        self.gridLayout_10 = QGridLayout(self.scrollAreaWidgetContents_4)
        self.gridLayout_10.setObjectName(u"gridLayout_10")
        self.label_80 = QLabel(self.scrollAreaWidgetContents_4)
        self.label_80.setObjectName(u"label_80")
        self.label_80.setFont(font7)

        self.gridLayout_10.addWidget(self.label_80, 2, 2, 1, 1)

        self.repequipo = QLineEdit(self.scrollAreaWidgetContents_4)
        self.repequipo.setObjectName(u"repequipo")
        self.repequipo.setEnabled(True)
        self.repequipo.setFont(font7)
        self.repequipo.setReadOnly(True)

        self.gridLayout_10.addWidget(self.repequipo, 0, 1, 1, 1)

        self.label_79 = QLabel(self.scrollAreaWidgetContents_4)
        self.label_79.setObjectName(u"label_79")
        self.label_79.setFont(font7)

        self.gridLayout_10.addWidget(self.label_79, 0, 2, 1, 1)

        self.label_76 = QLabel(self.scrollAreaWidgetContents_4)
        self.label_76.setObjectName(u"label_76")
        self.label_76.setFont(font8)

        self.gridLayout_10.addWidget(self.label_76, 4, 2, 1, 1)

        self.repmodelo = QLineEdit(self.scrollAreaWidgetContents_4)
        self.repmodelo.setObjectName(u"repmodelo")
        self.repmodelo.setFont(font7)
        self.repmodelo.setReadOnly(True)

        self.gridLayout_10.addWidget(self.repmodelo, 2, 1, 1, 1)

        self.repmarca = QLineEdit(self.scrollAreaWidgetContents_4)
        self.repmarca.setObjectName(u"repmarca")
        self.repmarca.setFont(font7)
        self.repmarca.setReadOnly(True)

        self.gridLayout_10.addWidget(self.repmarca, 0, 4, 1, 1)

        self.repnserie = QLineEdit(self.scrollAreaWidgetContents_4)
        self.repnserie.setObjectName(u"repnserie")
        self.repnserie.setFont(font7)
        self.repnserie.setReadOnly(True)

        self.gridLayout_10.addWidget(self.repnserie, 2, 4, 1, 1)

        self.repfalla = QLineEdit(self.scrollAreaWidgetContents_4)
        self.repfalla.setObjectName(u"repfalla")
        self.repfalla.setFont(font7)
        self.repfalla.setReadOnly(True)

        self.gridLayout_10.addWidget(self.repfalla, 4, 1, 1, 1)

        self.repinfadi = QTextEdit(self.scrollAreaWidgetContents_4)
        self.repinfadi.setObjectName(u"repinfadi")
        self.repinfadi.setMaximumSize(QSize(16777215, 80))
        self.repinfadi.setFont(font7)
        self.repinfadi.setTabChangesFocus(True)
        self.repinfadi.setReadOnly(True)

        self.gridLayout_10.addWidget(self.repinfadi, 4, 4, 1, 1)

        self.label_77 = QLabel(self.scrollAreaWidgetContents_4)
        self.label_77.setObjectName(u"label_77")
        self.label_77.setFont(font7)

        self.gridLayout_10.addWidget(self.label_77, 0, 0, 1, 1)

        self.label_78 = QLabel(self.scrollAreaWidgetContents_4)
        self.label_78.setObjectName(u"label_78")
        self.label_78.setFont(font7)

        self.gridLayout_10.addWidget(self.label_78, 2, 0, 1, 1)

        self.label_75 = QLabel(self.scrollAreaWidgetContents_4)
        self.label_75.setObjectName(u"label_75")
        self.label_75.setFont(font7)

        self.gridLayout_10.addWidget(self.label_75, 4, 0, 1, 1)

        self.scrollArea_7.setWidget(self.scrollAreaWidgetContents_4)

        self.verticalLayout_27.addWidget(self.scrollArea_7)


        self.verticalLayout_26.addWidget(self.groupBox_4)

        self.groupBox_2 = QGroupBox(self.page_11)
        self.groupBox_2.setObjectName(u"groupBox_2")
        self.groupBox_2.setFont(font7)
        self.gridLayout_4 = QGridLayout(self.groupBox_2)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.gridLayout_4.setHorizontalSpacing(2)
        self.gridLayout_4.setVerticalSpacing(0)
        self.gridLayout_4.setContentsMargins(-1, 0, -1, 2)
        self.widget_41 = QWidget(self.groupBox_2)
        self.widget_41.setObjectName(u"widget_41")
        self.horizontalLayout_29 = QHBoxLayout(self.widget_41)
        self.horizontalLayout_29.setObjectName(u"horizontalLayout_29")
        self.horizontalLayout_29.setContentsMargins(-1, 0, -1, 0)
        self.label_37 = QLabel(self.widget_41)
        self.label_37.setObjectName(u"label_37")

        self.horizontalLayout_29.addWidget(self.label_37)

        self.horizontalSpacer_11 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_29.addItem(self.horizontalSpacer_11)


        self.gridLayout_4.addWidget(self.widget_41, 2, 0, 1, 1)

        self.diagnostico = QPlainTextEdit(self.groupBox_2)
        self.diagnostico.setObjectName(u"diagnostico")
        self.diagnostico.setMaximumSize(QSize(16777215, 100))
        self.diagnostico.setTabChangesFocus(True)

        self.gridLayout_4.addWidget(self.diagnostico, 3, 0, 1, 1)

        self.widget_44 = QWidget(self.groupBox_2)
        self.widget_44.setObjectName(u"widget_44")
        self.gridLayout_5 = QGridLayout(self.widget_44)
        self.gridLayout_5.setSpacing(1)
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.gridLayout_5.setContentsMargins(-1, 0, -1, 0)
        self.groupBox_3 = QGroupBox(self.widget_44)
        self.groupBox_3.setObjectName(u"groupBox_3")
        self.groupBox_3.setMinimumSize(QSize(0, 0))
        self.gridLayout_6 = QGridLayout(self.groupBox_3)
        self.gridLayout_6.setObjectName(u"gridLayout_6")
        self.gridLayout_6.setVerticalSpacing(0)
        self.gridLayout_6.setContentsMargins(-1, 0, 0, -1)
        self.totalrep = QLabel(self.groupBox_3)
        self.totalrep.setObjectName(u"totalrep")
        self.totalrep.setMinimumSize(QSize(0, 0))
        self.totalrep.setMaximumSize(QSize(160, 16777215))
        self.totalrep.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)

        self.gridLayout_6.addWidget(self.totalrep, 1, 2, 1, 1)

        self.label_56 = QLabel(self.groupBox_3)
        self.label_56.setObjectName(u"label_56")
        self.label_56.setMinimumSize(QSize(0, 0))
        self.label_56.setMaximumSize(QSize(16777215, 16777215))
        self.label_56.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)
        self.label_56.setMargin(0)

        self.gridLayout_6.addWidget(self.label_56, 1, 0, 1, 1)

        self.widget_45 = QWidget(self.groupBox_3)
        self.widget_45.setObjectName(u"widget_45")
        self.horizontalLayout_30 = QHBoxLayout(self.widget_45)
        self.horizontalLayout_30.setObjectName(u"horizontalLayout_30")
        self.repuestos = QTableWidget(self.widget_45)
        if (self.repuestos.columnCount() < 2):
            self.repuestos.setColumnCount(2)
        __qtablewidgetitem5 = QTableWidgetItem()
        self.repuestos.setHorizontalHeaderItem(0, __qtablewidgetitem5)
        __qtablewidgetitem6 = QTableWidgetItem()
        self.repuestos.setHorizontalHeaderItem(1, __qtablewidgetitem6)
        if (self.repuestos.rowCount() < 1):
            self.repuestos.setRowCount(1)
        __qtablewidgetitem7 = QTableWidgetItem()
        self.repuestos.setVerticalHeaderItem(0, __qtablewidgetitem7)
        __qtablewidgetitem8 = QTableWidgetItem()
        self.repuestos.setItem(0, 0, __qtablewidgetitem8)
        __qtablewidgetitem9 = QTableWidgetItem()
        __qtablewidgetitem9.setTextAlignment(Qt.AlignTrailing|Qt.AlignVCenter)
        self.repuestos.setItem(0, 1, __qtablewidgetitem9)
        self.repuestos.setObjectName(u"repuestos")
        self.repuestos.setMinimumSize(QSize(0, 0))
        self.repuestos.setFont(font10)
        self.repuestos.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.repuestos.setFrameShape(QFrame.Shape.StyledPanel)
        self.repuestos.setEditTriggers(QAbstractItemView.EditTrigger.AnyKeyPressed|QAbstractItemView.EditTrigger.DoubleClicked|QAbstractItemView.EditTrigger.EditKeyPressed)
        self.repuestos.setAlternatingRowColors(False)
        self.repuestos.setSelectionBehavior(QAbstractItemView.SelectionBehavior.SelectRows)
        self.repuestos.setShowGrid(True)
        self.repuestos.setGridStyle(Qt.PenStyle.SolidLine)
        self.repuestos.setSortingEnabled(False)
        self.repuestos.setWordWrap(True)
        self.repuestos.horizontalHeader().setVisible(True)
        self.repuestos.horizontalHeader().setCascadingSectionResizes(False)
        self.repuestos.horizontalHeader().setProperty(u"showSortIndicator", False)
        self.repuestos.horizontalHeader().setStretchLastSection(True)
        self.repuestos.verticalHeader().setVisible(True)
        self.repuestos.verticalHeader().setCascadingSectionResizes(False)
        self.repuestos.verticalHeader().setProperty(u"showSortIndicator", False)
        self.repuestos.verticalHeader().setStretchLastSection(False)

        self.horizontalLayout_30.addWidget(self.repuestos)

        self.anadir = QToolButton(self.widget_45)
        self.anadir.setObjectName(u"anadir")
        self.anadir.setFont(font2)
        self.anadir.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.anadir.setIcon(icon25)
        self.anadir.setIconSize(QSize(40, 40))
        self.anadir.setToolButtonStyle(Qt.ToolButtonStyle.ToolButtonTextUnderIcon)

        self.horizontalLayout_30.addWidget(self.anadir)

        self.btneliminarep = QToolButton(self.widget_45)
        self.btneliminarep.setObjectName(u"btneliminarep")
        self.btneliminarep.setFont(font2)
        self.btneliminarep.setIcon(icon26)
        self.btneliminarep.setIconSize(QSize(35, 35))
        self.btneliminarep.setToolButtonStyle(Qt.ToolButtonStyle.ToolButtonTextUnderIcon)

        self.horizontalLayout_30.addWidget(self.btneliminarep)


        self.gridLayout_6.addWidget(self.widget_45, 0, 0, 1, 3)

        self.label_58 = QLabel(self.groupBox_3)
        self.label_58.setObjectName(u"label_58")
        self.label_58.setMinimumSize(QSize(10, 0))
        self.label_58.setMaximumSize(QSize(10, 16777215))

        self.gridLayout_6.addWidget(self.label_58, 1, 1, 1, 1)


        self.gridLayout_5.addWidget(self.groupBox_3, 0, 0, 3, 1)

        self.label_39 = QLabel(self.widget_44)
        self.label_39.setObjectName(u"label_39")
        self.label_39.setMaximumSize(QSize(130, 16777215))

        self.gridLayout_5.addWidget(self.label_39, 2, 3, 1, 1)

        self.label_41 = QLabel(self.widget_44)
        self.label_41.setObjectName(u"label_41")
        self.label_41.setMaximumSize(QSize(55, 16777215))

        self.gridLayout_5.addWidget(self.label_41, 0, 3, 1, 1)

        self.label_55 = QLabel(self.widget_44)
        self.label_55.setObjectName(u"label_55")

        self.gridLayout_5.addWidget(self.label_55, 1, 3, 1, 1)

        self.tecnico = QComboBox(self.widget_44)
        self.tecnico.setObjectName(u"tecnico")

        self.gridLayout_5.addWidget(self.tecnico, 0, 4, 1, 1)

        self.servtec = QDoubleSpinBox(self.widget_44)
        self.servtec.setObjectName(u"servtec")
        self.servtec.setButtonSymbols(QAbstractSpinBox.ButtonSymbols.NoButtons)
        self.servtec.setMaximum(999999.989999999990687)

        self.gridLayout_5.addWidget(self.servtec, 1, 4, 1, 1)

        self.total = QDoubleSpinBox(self.widget_44)
        self.total.setObjectName(u"total")
        self.total.setWrapping(False)
        self.total.setFrame(True)
        self.total.setButtonSymbols(QAbstractSpinBox.ButtonSymbols.NoButtons)
        self.total.setAccelerated(False)
        self.total.setProperty(u"showGroupSeparator", False)
        self.total.setMaximum(999999.989999999990687)

        self.gridLayout_5.addWidget(self.total, 2, 4, 1, 1)


        self.gridLayout_4.addWidget(self.widget_44, 5, 0, 1, 1)

        self.widget_38 = QWidget(self.groupBox_2)
        self.widget_38.setObjectName(u"widget_38")
        self.horizontalLayout_27 = QHBoxLayout(self.widget_38)
        self.horizontalLayout_27.setObjectName(u"horizontalLayout_27")
        self.horizontalLayout_27.setContentsMargins(-1, 0, -1, 0)

        self.gridLayout_4.addWidget(self.widget_38, 1, 0, 1, 1)

        self.stackinfrep = QStackedWidget(self.groupBox_2)
        self.stackinfrep.setObjectName(u"stackinfrep")
        self.page_8 = QWidget()
        self.page_8.setObjectName(u"page_8")
        self.verticalLayout_28 = QVBoxLayout(self.page_8)
        self.verticalLayout_28.setObjectName(u"verticalLayout_28")
        self.label_81 = QLabel(self.page_8)
        self.label_81.setObjectName(u"label_81")

        self.verticalLayout_28.addWidget(self.label_81)

        self.stackinfrep.addWidget(self.page_8)
        self.page_9 = QWidget()
        self.page_9.setObjectName(u"page_9")
        self.gridLayout_9 = QGridLayout(self.page_9)
        self.gridLayout_9.setObjectName(u"gridLayout_9")
        self.fecha_rep = QLineEdit(self.page_9)
        self.fecha_rep.setObjectName(u"fecha_rep")
        self.fecha_rep.setMinimumSize(QSize(0, 0))
        self.fecha_rep.setMaximumSize(QSize(280, 16777215))
        self.fecha_rep.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)
        self.fecha_rep.setReadOnly(True)

        self.gridLayout_9.addWidget(self.fecha_rep, 0, 2, 1, 1)

        self.horizontalSpacer_8 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_9.addItem(self.horizontalSpacer_8, 0, 6, 1, 1)

        self.label_83 = QLabel(self.page_9)
        self.label_83.setObjectName(u"label_83")

        self.gridLayout_9.addWidget(self.label_83, 0, 4, 1, 1)

        self.label_84 = QLabel(self.page_9)
        self.label_84.setObjectName(u"label_84")

        self.gridLayout_9.addWidget(self.label_84, 1, 0, 1, 1)

        self.fecharep = QDateTimeEdit(self.page_9)
        self.fecharep.setObjectName(u"fecharep")
        self.fecharep.setMaximumSize(QSize(20, 28))
        self.fecharep.setWrapping(False)
        self.fecharep.setReadOnly(False)
        self.fecharep.setButtonSymbols(QAbstractSpinBox.ButtonSymbols.NoButtons)
        self.fecharep.setAccelerated(True)
        self.fecharep.setMinimumDateTime(QDateTime(QDate(2000, 1, 1), QTime(0, 0, 0)))
        self.fecharep.setCalendarPopup(True)

        self.gridLayout_9.addWidget(self.fecharep, 0, 3, 1, 1)

        self.garantia = QSpinBox(self.page_9)
        self.garantia.setObjectName(u"garantia")
        self.garantia.setMaximum(365)

        self.gridLayout_9.addWidget(self.garantia, 0, 5, 1, 1)

        self.label_82 = QLabel(self.page_9)
        self.label_82.setObjectName(u"label_82")

        self.gridLayout_9.addWidget(self.label_82, 0, 0, 1, 1)

        self.hoy = QPushButton(self.page_9)
        self.hoy.setObjectName(u"hoy")
        sizePolicy2 = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.hoy.sizePolicy().hasHeightForWidth())
        self.hoy.setSizePolicy(sizePolicy2)
        self.hoy.setMaximumSize(QSize(35, 16777215))
        self.hoy.setFont(font10)

        self.gridLayout_9.addWidget(self.hoy, 0, 1, 1, 1)

        self.fechagarantia = QLineEdit(self.page_9)
        self.fechagarantia.setObjectName(u"fechagarantia")
        self.fechagarantia.setMaximumSize(QSize(300, 16777215))
        self.fechagarantia.setReadOnly(True)

        self.gridLayout_9.addWidget(self.fechagarantia, 1, 1, 1, 3)

        self.stackinfrep.addWidget(self.page_9)

        self.gridLayout_4.addWidget(self.stackinfrep, 6, 0, 1, 1)


        self.verticalLayout_26.addWidget(self.groupBox_2)

        self.widget_80 = QWidget(self.page_11)
        self.widget_80.setObjectName(u"widget_80")
        self.horizontalLayout_26 = QHBoxLayout(self.widget_80)
        self.horizontalLayout_26.setObjectName(u"horizontalLayout_26")
        self.horizontalLayout_26.setContentsMargins(-1, 0, -1, 0)
        self.btnconfirmar = QToolButton(self.widget_80)
        self.btnconfirmar.setObjectName(u"btnconfirmar")
        self.btnconfirmar.setMinimumSize(QSize(62, 0))
        self.btnconfirmar.setMaximumSize(QSize(16777215, 60))
        self.btnconfirmar.setIcon(icon10)
        self.btnconfirmar.setIconSize(QSize(40, 40))
        self.btnconfirmar.setToolButtonStyle(Qt.ToolButtonStyle.ToolButtonTextUnderIcon)

        self.horizontalLayout_26.addWidget(self.btnconfirmar)

        self.btnentsinrep = QToolButton(self.widget_80)
        self.btnentsinrep.setObjectName(u"btnentsinrep")
        icon32 = QIcon()
        icon32.addFile(u":/iconos/iconos/equis.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.btnentsinrep.setIcon(icon32)
        self.btnentsinrep.setIconSize(QSize(40, 40))
        self.btnentsinrep.setToolButtonStyle(Qt.ToolButtonStyle.ToolButtonTextUnderIcon)

        self.horizontalLayout_26.addWidget(self.btnentsinrep)


        self.verticalLayout_26.addWidget(self.widget_80)

        self.stackreparaciones.addWidget(self.page_11)

        self.verticalLayout_19.addWidget(self.stackreparaciones)

        self.stack.addWidget(self.page_3)
        self.page_4 = QWidget()
        self.page_4.setObjectName(u"page_4")
        self.verticalLayout_30 = QVBoxLayout(self.page_4)
        self.verticalLayout_30.setObjectName(u"verticalLayout_30")
        self.entregas = QTabWidget(self.page_4)
        self.entregas.setObjectName(u"entregas")
        self.entregas.setEnabled(True)
        self.entregas.setStyleSheet(u"#entregas {\n"
"	font: 700 12pt \"Segoe UI\";\n"
"}")
        self.entregas.setIconSize(QSize(30, 30))
        self.entregas.setUsesScrollButtons(True)
        self.entregas.setDocumentMode(False)
        self.entregas.setTabsClosable(False)
        self.entregas.setMovable(False)
        self.entregas.setTabBarAutoHide(False)
        self.tab_5 = QWidget()
        self.tab_5.setObjectName(u"tab_5")
        self.verticalLayout_24 = QVBoxLayout(self.tab_5)
        self.verticalLayout_24.setObjectName(u"verticalLayout_24")
        self.label_5 = QLabel(self.tab_5)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setFont(font7)

        self.verticalLayout_24.addWidget(self.label_5)

        self.listaentregas = QListView(self.tab_5)
        self.listaentregas.setObjectName(u"listaentregas")
        self.listaentregas.setStyleSheet(u"QListView {\n"
"        border: none;\n"
"        background-color: transparent; /* O el color de tu ventana */\n"
"        outline: none; /* Quita el recuadro de puntos al hacer clic */\n"
"    }\n"
"\n"
"QListView::item {\n"
"        background-color: rgba(7, 39, 67, 140);; /* Color de la tarjeta */\n"
"        border: 1px solid #ddd;\n"
"        border-radius: 10px;       /* <--- AQU\u00cd sucede la magia */\n"
"        padding: 10px;\n"
"        margin-bottom: 5px;        /* Espacio entre tarjetas */\n"
"        margin-left: 5px;\n"
"        margin-right: 5px;\n"
"    }\n"
"\n"
"QListView::item:selected {\n"
"        background-color: #3498db; /* Azul cuando se selecciona */\n"
"        color: white;\n"
"        border: 1px solid #2980b9;\n"
"    }\n"
"\n"
"QListView::item:hover {\n"
"        background-color: #3498db; /* Color al pasar el mouse */\n"
"    }")
        self.listaentregas.setIconSize(QSize(80, 80))
        self.listaentregas.setTextElideMode(Qt.TextElideMode.ElideNone)
        self.listaentregas.setHorizontalScrollMode(QAbstractItemView.ScrollMode.ScrollPerPixel)
        self.listaentregas.setMovement(QListView.Movement.Snap)
        self.listaentregas.setResizeMode(QListView.ResizeMode.Adjust)
        self.listaentregas.setLayoutMode(QListView.LayoutMode.SinglePass)
        self.listaentregas.setSpacing(1)
        self.listaentregas.setGridSize(QSize(220, 280))
        self.listaentregas.setViewMode(QListView.ViewMode.IconMode)
        self.listaentregas.setModelColumn(0)
        self.listaentregas.setUniformItemSizes(False)
        self.listaentregas.setItemAlignment(Qt.AlignmentFlag.AlignTop)

        self.verticalLayout_24.addWidget(self.listaentregas)

        icon33 = QIcon()
        icon33.addFile(u":/iconos/iconos/entregar.ico", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.entregas.addTab(self.tab_5, icon33, "")
        self.tab_6 = QWidget()
        self.tab_6.setObjectName(u"tab_6")
        self.verticalLayout_25 = QVBoxLayout(self.tab_6)
        self.verticalLayout_25.setSpacing(3)
        self.verticalLayout_25.setObjectName(u"verticalLayout_25")
        self.verticalLayout_25.setContentsMargins(-1, 0, -1, 0)
        self.widget_53 = QWidget(self.tab_6)
        self.widget_53.setObjectName(u"widget_53")
        self.horizontalLayout_38 = QHBoxLayout(self.widget_53)
        self.horizontalLayout_38.setSpacing(0)
        self.horizontalLayout_38.setObjectName(u"horizontalLayout_38")
        self.horizontalLayout_38.setContentsMargins(-1, 0, -1, 0)
        self.horizontalSpacer_16 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_38.addItem(self.horizontalSpacer_16)

        self.btnimprimir_e = QToolButton(self.widget_53)
        self.btnimprimir_e.setObjectName(u"btnimprimir_e")
        sizePolicy.setHeightForWidth(self.btnimprimir_e.sizePolicy().hasHeightForWidth())
        self.btnimprimir_e.setSizePolicy(sizePolicy)
        self.btnimprimir_e.setMaximumSize(QSize(60, 60))
        self.btnimprimir_e.setIcon(icon11)
        self.btnimprimir_e.setIconSize(QSize(40, 40))
        self.btnimprimir_e.setToolButtonStyle(Qt.ToolButtonStyle.ToolButtonTextUnderIcon)

        self.horizontalLayout_38.addWidget(self.btnimprimir_e)


        self.verticalLayout_25.addWidget(self.widget_53)

        self.groupBox_5 = QGroupBox(self.tab_6)
        self.groupBox_5.setObjectName(u"groupBox_5")
        self.groupBox_5.setMinimumSize(QSize(0, 200))
        self.groupBox_5.setFont(font11)
        self.gridLayout_7 = QGridLayout(self.groupBox_5)
        self.gridLayout_7.setObjectName(u"gridLayout_7")
        self.gridLayout_7.setHorizontalSpacing(2)
        self.gridLayout_7.setVerticalSpacing(0)
        self.gridLayout_7.setContentsMargins(-1, 0, -1, 2)
        self.widget_46 = QWidget(self.groupBox_5)
        self.widget_46.setObjectName(u"widget_46")
        self.horizontalLayout_32 = QHBoxLayout(self.widget_46)
        self.horizontalLayout_32.setObjectName(u"horizontalLayout_32")
        self.horizontalLayout_32.setContentsMargins(-1, 0, -1, 0)
        self.label_62 = QLabel(self.widget_46)
        self.label_62.setObjectName(u"label_62")
        font12 = QFont()
        font12.setPointSize(11)
        font12.setBold(False)
        self.label_62.setFont(font12)

        self.horizontalLayout_32.addWidget(self.label_62)

        self.horizontalSpacer_12 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_32.addItem(self.horizontalSpacer_12)


        self.gridLayout_7.addWidget(self.widget_46, 2, 0, 1, 1)

        self.diagnosticoe = QPlainTextEdit(self.groupBox_5)
        self.diagnosticoe.setObjectName(u"diagnosticoe")
        self.diagnosticoe.setMaximumSize(QSize(16777215, 100))
        self.diagnosticoe.setFont(font12)
        self.diagnosticoe.setStyleSheet(u"border: 2px solid rgb(61, 61, 61);\n"
"border-radius: 5px;")
        self.diagnosticoe.setTabChangesFocus(True)

        self.gridLayout_7.addWidget(self.diagnosticoe, 3, 0, 1, 1)

        self.widget_51 = QWidget(self.groupBox_5)
        self.widget_51.setObjectName(u"widget_51")
        self.widget_51.setFont(font12)
        self.horizontalLayout_37 = QHBoxLayout(self.widget_51)
        self.horizontalLayout_37.setObjectName(u"horizontalLayout_37")
        self.horizontalLayout_37.setContentsMargins(-1, 0, -1, 0)

        self.gridLayout_7.addWidget(self.widget_51, 1, 0, 1, 1)

        self.widget_47 = QWidget(self.groupBox_5)
        self.widget_47.setObjectName(u"widget_47")
        font13 = QFont()
        font13.setPointSize(12)
        font13.setBold(False)
        self.widget_47.setFont(font13)
        self.gridLayout_8 = QGridLayout(self.widget_47)
        self.gridLayout_8.setObjectName(u"gridLayout_8")
        self.groupBox_6 = QGroupBox(self.widget_47)
        self.groupBox_6.setObjectName(u"groupBox_6")
        self.groupBox_6.setMinimumSize(QSize(0, 40))
        self.groupBox_6.setFont(font8)
        self.gridLayout_11 = QGridLayout(self.groupBox_6)
        self.gridLayout_11.setObjectName(u"gridLayout_11")
        self.gridLayout_11.setVerticalSpacing(0)
        self.gridLayout_11.setContentsMargins(-1, 0, 0, -1)
        self.totalrepe = QLabel(self.groupBox_6)
        self.totalrepe.setObjectName(u"totalrepe")
        self.totalrepe.setMinimumSize(QSize(140, 0))
        self.totalrepe.setMaximumSize(QSize(160, 16777215))
        self.totalrepe.setFont(font12)
        self.totalrepe.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)

        self.gridLayout_11.addWidget(self.totalrepe, 1, 2, 1, 1)

        self.label_66 = QLabel(self.groupBox_6)
        self.label_66.setObjectName(u"label_66")
        self.label_66.setMinimumSize(QSize(0, 0))
        self.label_66.setMaximumSize(QSize(16777215, 16777215))
        self.label_66.setFont(font12)
        self.label_66.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)
        self.label_66.setMargin(0)

        self.gridLayout_11.addWidget(self.label_66, 1, 0, 1, 1)

        self.widget_50 = QWidget(self.groupBox_6)
        self.widget_50.setObjectName(u"widget_50")
        self.horizontalLayout_34 = QHBoxLayout(self.widget_50)
        self.horizontalLayout_34.setObjectName(u"horizontalLayout_34")
        self.repuestose = QTableWidget(self.widget_50)
        if (self.repuestose.columnCount() < 2):
            self.repuestose.setColumnCount(2)
        __qtablewidgetitem10 = QTableWidgetItem()
        self.repuestose.setHorizontalHeaderItem(0, __qtablewidgetitem10)
        __qtablewidgetitem11 = QTableWidgetItem()
        self.repuestose.setHorizontalHeaderItem(1, __qtablewidgetitem11)
        if (self.repuestose.rowCount() < 1):
            self.repuestose.setRowCount(1)
        __qtablewidgetitem12 = QTableWidgetItem()
        self.repuestose.setVerticalHeaderItem(0, __qtablewidgetitem12)
        __qtablewidgetitem13 = QTableWidgetItem()
        self.repuestose.setItem(0, 0, __qtablewidgetitem13)
        __qtablewidgetitem14 = QTableWidgetItem()
        __qtablewidgetitem14.setTextAlignment(Qt.AlignTrailing|Qt.AlignVCenter)
        self.repuestose.setItem(0, 1, __qtablewidgetitem14)
        self.repuestose.setObjectName(u"repuestose")
        self.repuestose.setMinimumSize(QSize(200, 90))
        font14 = QFont()
        font14.setPointSize(9)
        font14.setBold(False)
        self.repuestose.setFont(font14)
        self.repuestose.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.repuestose.setFrameShape(QFrame.Shape.StyledPanel)
        self.repuestose.setEditTriggers(QAbstractItemView.EditTrigger.AnyKeyPressed|QAbstractItemView.EditTrigger.DoubleClicked|QAbstractItemView.EditTrigger.EditKeyPressed)
        self.repuestose.setAlternatingRowColors(False)
        self.repuestose.setSelectionBehavior(QAbstractItemView.SelectionBehavior.SelectRows)
        self.repuestose.setShowGrid(True)
        self.repuestose.setGridStyle(Qt.PenStyle.SolidLine)
        self.repuestose.setSortingEnabled(False)
        self.repuestose.setWordWrap(True)
        self.repuestose.horizontalHeader().setVisible(True)
        self.repuestose.horizontalHeader().setCascadingSectionResizes(False)
        self.repuestose.horizontalHeader().setProperty(u"showSortIndicator", False)
        self.repuestose.horizontalHeader().setStretchLastSection(True)
        self.repuestose.verticalHeader().setVisible(True)
        self.repuestose.verticalHeader().setCascadingSectionResizes(False)
        self.repuestose.verticalHeader().setProperty(u"showSortIndicator", False)
        self.repuestose.verticalHeader().setStretchLastSection(False)

        self.horizontalLayout_34.addWidget(self.repuestose)

        self.anadire = QToolButton(self.widget_50)
        self.anadire.setObjectName(u"anadire")
        font15 = QFont()
        font15.setPointSize(10)
        font15.setBold(False)
        self.anadire.setFont(font15)
        self.anadire.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.anadire.setIcon(icon25)
        self.anadire.setIconSize(QSize(40, 40))
        self.anadire.setToolButtonStyle(Qt.ToolButtonStyle.ToolButtonTextUnderIcon)

        self.horizontalLayout_34.addWidget(self.anadire)

        self.btneliminarepe = QToolButton(self.widget_50)
        self.btneliminarepe.setObjectName(u"btneliminarepe")
        self.btneliminarepe.setFont(font15)
        self.btneliminarepe.setIcon(icon26)
        self.btneliminarepe.setIconSize(QSize(35, 35))
        self.btneliminarepe.setToolButtonStyle(Qt.ToolButtonStyle.ToolButtonTextUnderIcon)

        self.horizontalLayout_34.addWidget(self.btneliminarepe)


        self.gridLayout_11.addWidget(self.widget_50, 0, 0, 1, 3)

        self.label_67 = QLabel(self.groupBox_6)
        self.label_67.setObjectName(u"label_67")
        self.label_67.setMinimumSize(QSize(10, 0))
        self.label_67.setMaximumSize(QSize(10, 16777215))
        self.label_67.setFont(font12)

        self.gridLayout_11.addWidget(self.label_67, 1, 1, 1, 1)


        self.gridLayout_8.addWidget(self.groupBox_6, 0, 0, 5, 1)

        self.servtece = QDoubleSpinBox(self.widget_47)
        self.servtece.setObjectName(u"servtece")
        self.servtece.setFont(font12)
        self.servtece.setButtonSymbols(QAbstractSpinBox.ButtonSymbols.NoButtons)
        self.servtece.setMaximum(999999.989999999990687)

        self.gridLayout_8.addWidget(self.servtece, 1, 2, 1, 1)

        self.label_64 = QLabel(self.widget_47)
        self.label_64.setObjectName(u"label_64")
        self.label_64.setMaximumSize(QSize(55, 16777215))
        self.label_64.setFont(font12)

        self.gridLayout_8.addWidget(self.label_64, 0, 1, 1, 1)

        self.label_65 = QLabel(self.widget_47)
        self.label_65.setObjectName(u"label_65")
        self.label_65.setFont(font12)

        self.gridLayout_8.addWidget(self.label_65, 1, 1, 1, 1)

        self.totale = QDoubleSpinBox(self.widget_47)
        self.totale.setObjectName(u"totale")
        self.totale.setFont(font12)
        self.totale.setWrapping(False)
        self.totale.setFrame(True)
        self.totale.setButtonSymbols(QAbstractSpinBox.ButtonSymbols.NoButtons)
        self.totale.setAccelerated(False)
        self.totale.setProperty(u"showGroupSeparator", False)
        self.totale.setMaximum(999999.989999999990687)

        self.gridLayout_8.addWidget(self.totale, 2, 2, 1, 1)

        self.label_63 = QLabel(self.widget_47)
        self.label_63.setObjectName(u"label_63")
        self.label_63.setMaximumSize(QSize(130, 16777215))
        self.label_63.setFont(font12)

        self.gridLayout_8.addWidget(self.label_63, 2, 1, 1, 1)

        self.stackinfrep_2 = QStackedWidget(self.widget_47)
        self.stackinfrep_2.setObjectName(u"stackinfrep_2")
        self.stackinfrep_2.setFont(font12)
        self.page_12 = QWidget()
        self.page_12.setObjectName(u"page_12")
        self.verticalLayout_31 = QVBoxLayout(self.page_12)
        self.verticalLayout_31.setObjectName(u"verticalLayout_31")
        self.label_85 = QLabel(self.page_12)
        self.label_85.setObjectName(u"label_85")

        self.verticalLayout_31.addWidget(self.label_85)

        self.stackinfrep_2.addWidget(self.page_12)
        self.page_13 = QWidget()
        self.page_13.setObjectName(u"page_13")
        self.gridLayout_12 = QGridLayout(self.page_13)
        self.gridLayout_12.setObjectName(u"gridLayout_12")
        self.fecha_repe = QLineEdit(self.page_13)
        self.fecha_repe.setObjectName(u"fecha_repe")
        sizePolicy3 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Preferred)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.fecha_repe.sizePolicy().hasHeightForWidth())
        self.fecha_repe.setSizePolicy(sizePolicy3)
        self.fecha_repe.setMinimumSize(QSize(180, 0))
        self.fecha_repe.setMaximumSize(QSize(280, 16777215))
        self.fecha_repe.setFont(font12)
        self.fecha_repe.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)
        self.fecha_repe.setReadOnly(True)

        self.gridLayout_12.addWidget(self.fecha_repe, 0, 1, 1, 8)

        self.fechagarantiae = QLineEdit(self.page_13)
        self.fechagarantiae.setObjectName(u"fechagarantiae")
        self.fechagarantiae.setMaximumSize(QSize(300, 16777215))
        self.fechagarantiae.setFont(font12)
        self.fechagarantiae.setReadOnly(True)

        self.gridLayout_12.addWidget(self.fechagarantiae, 2, 1, 1, 9)

        self.label_87 = QLabel(self.page_13)
        self.label_87.setObjectName(u"label_87")
        self.label_87.setFont(font12)

        self.gridLayout_12.addWidget(self.label_87, 0, 0, 1, 1)

        self.label_86 = QLabel(self.page_13)
        self.label_86.setObjectName(u"label_86")
        self.label_86.setFont(font12)

        self.gridLayout_12.addWidget(self.label_86, 2, 0, 1, 1)

        self.fecharepe = QDateTimeEdit(self.page_13)
        self.fecharepe.setObjectName(u"fecharepe")
        self.fecharepe.setMaximumSize(QSize(20, 28))
        self.fecharepe.setWrapping(False)
        self.fecharepe.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)
        self.fecharepe.setReadOnly(False)
        self.fecharepe.setButtonSymbols(QAbstractSpinBox.ButtonSymbols.NoButtons)
        self.fecharepe.setAccelerated(True)
        self.fecharepe.setMinimumDateTime(QDateTime(QDate(2000, 1, 1), QTime(0, 0, 0)))
        self.fecharepe.setCalendarPopup(True)

        self.gridLayout_12.addWidget(self.fecharepe, 0, 9, 1, 1)

        self.horizontalSpacer_7 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_12.addItem(self.horizontalSpacer_7, 0, 10, 1, 1)

        self.label_88 = QLabel(self.page_13)
        self.label_88.setObjectName(u"label_88")
        self.label_88.setFont(font12)

        self.gridLayout_12.addWidget(self.label_88, 1, 0, 1, 1)

        self.garantiae = QSpinBox(self.page_13)
        self.garantiae.setObjectName(u"garantiae")
        self.garantiae.setFont(font12)
        self.garantiae.setMaximum(365)

        self.gridLayout_12.addWidget(self.garantiae, 1, 1, 1, 1)

        self.stackinfrep_2.addWidget(self.page_13)

        self.gridLayout_8.addWidget(self.stackinfrep_2, 4, 1, 1, 2)

        self.tecnicoe = QComboBox(self.widget_47)
        self.tecnicoe.setObjectName(u"tecnicoe")
        self.tecnicoe.setFont(font8)

        self.gridLayout_8.addWidget(self.tecnicoe, 0, 2, 1, 1)


        self.gridLayout_7.addWidget(self.widget_47, 5, 0, 1, 1)


        self.verticalLayout_25.addWidget(self.groupBox_5)

        self.widget_52 = QWidget(self.tab_6)
        self.widget_52.setObjectName(u"widget_52")
        self.gridLayout_13 = QGridLayout(self.widget_52)
        self.gridLayout_13.setObjectName(u"gridLayout_13")
        self.gridLayout_13.setHorizontalSpacing(3)
        self.gridLayout_13.setVerticalSpacing(0)
        self.gridLayout_13.setContentsMargins(-1, 2, 0, 4)
        self.label_70 = QLabel(self.widget_52)
        self.label_70.setObjectName(u"label_70")
        self.label_70.setFont(font7)

        self.gridLayout_13.addWidget(self.label_70, 1, 0, 1, 1)

        self.pagppend = QCheckBox(self.widget_52)
        self.pagppend.setObjectName(u"pagppend")
        self.pagppend.setFont(font7)
        self.pagppend.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.pagppend.setIcon(icon27)

        self.gridLayout_13.addWidget(self.pagppend, 2, 0, 1, 1)

        self.btnguardare = QToolButton(self.widget_52)
        self.btnguardare.setObjectName(u"btnguardare")
        self.btnguardare.setMinimumSize(QSize(62, 0))
        self.btnguardare.setIcon(icon19)
        self.btnguardare.setIconSize(QSize(40, 40))
        self.btnguardare.setToolButtonStyle(Qt.ToolButtonStyle.ToolButtonTextUnderIcon)

        self.gridLayout_13.addWidget(self.btnguardare, 2, 3, 1, 1)

        self.fechaentrega = QDateTimeEdit(self.widget_52)
        self.fechaentrega.setObjectName(u"fechaentrega")
        self.fechaentrega.setFont(font7)
        self.fechaentrega.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.fechaentrega.setCalendarPopup(True)

        self.gridLayout_13.addWidget(self.fechaentrega, 0, 1, 1, 1)

        self.widget_54 = QWidget(self.widget_52)
        self.widget_54.setObjectName(u"widget_54")
        self.horizontalLayout_39 = QHBoxLayout(self.widget_54)
        self.horizontalLayout_39.setObjectName(u"horizontalLayout_39")
        self.horizontalLayout_39.setContentsMargins(-1, 0, -1, 0)
        self.porcentaje = QLabel(self.widget_54)
        self.porcentaje.setObjectName(u"porcentaje")
        self.porcentaje.setFont(font7)

        self.horizontalLayout_39.addWidget(self.porcentaje)

        self.label_72 = QLabel(self.widget_54)
        self.label_72.setObjectName(u"label_72")
        self.label_72.setFont(font7)

        self.horizontalLayout_39.addWidget(self.label_72)

        self.btneditaporce = QToolButton(self.widget_54)
        self.btneditaporce.setObjectName(u"btneditaporce")
        self.btneditaporce.setIcon(icon28)
        self.btneditaporce.setIconSize(QSize(30, 30))
        self.btneditaporce.setPopupMode(QToolButton.ToolButtonPopupMode.DelayedPopup)
        self.btneditaporce.setToolButtonStyle(Qt.ToolButtonStyle.ToolButtonIconOnly)
        self.btneditaporce.setAutoRaise(True)
        self.btneditaporce.setArrowType(Qt.ArrowType.NoArrow)

        self.horizontalLayout_39.addWidget(self.btneditaporce)

        self.horizontalSpacer_17 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_39.addItem(self.horizontalSpacer_17)


        self.gridLayout_13.addWidget(self.widget_54, 1, 1, 1, 1)

        self.label_89 = QLabel(self.widget_52)
        self.label_89.setObjectName(u"label_89")
        self.label_89.setFont(font7)

        self.gridLayout_13.addWidget(self.label_89, 0, 0, 1, 1)

        self.horizontalSpacer_14 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_13.addItem(self.horizontalSpacer_14, 2, 2, 1, 1)

        self.horizontalSpacer_15 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_13.addItem(self.horizontalSpacer_15, 0, 2, 1, 2)


        self.verticalLayout_25.addWidget(self.widget_52)

        self.verticalSpacer_10 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_25.addItem(self.verticalSpacer_10)

        self.entregas.addTab(self.tab_6, icon4, "")

        self.verticalLayout_30.addWidget(self.entregas)

        self.stack.addWidget(self.page_4)
        self.page_5 = QWidget()
        self.page_5.setObjectName(u"page_5")
        self.gridLayout_3 = QGridLayout(self.page_5)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.widget_39 = QWidget(self.page_5)
        self.widget_39.setObjectName(u"widget_39")
        self.widget_39.setMinimumSize(QSize(0, 0))
        self.verticalLayout_18 = QVBoxLayout(self.widget_39)
        self.verticalLayout_18.setObjectName(u"verticalLayout_18")
        self.verticalLayout_18.setContentsMargins(-1, -1, -1, 0)
        self.widget_40 = QWidget(self.widget_39)
        self.widget_40.setObjectName(u"widget_40")
        self.horizontalLayout_28 = QHBoxLayout(self.widget_40)
        self.horizontalLayout_28.setObjectName(u"horizontalLayout_28")
        self.horizontalLayout_28.setContentsMargins(0, -1, -1, 0)
        self.toolButton = QToolButton(self.widget_40)
        self.toolButton.setObjectName(u"toolButton")
        self.toolButton.setEnabled(False)
        self.toolButton.setIcon(icon21)
        self.toolButton.setIconSize(QSize(22, 22))
        self.toolButton.setToolButtonStyle(Qt.ToolButtonStyle.ToolButtonIconOnly)

        self.horizontalLayout_28.addWidget(self.toolButton)

        self.buscarcliente = QLineEdit(self.widget_40)
        self.buscarcliente.setObjectName(u"buscarcliente")
        self.buscarcliente.setFont(font9)
        self.buscarcliente.setFocusPolicy(Qt.FocusPolicy.StrongFocus)
        self.buscarcliente.setAutoFillBackground(False)
        self.buscarcliente.setClearButtonEnabled(True)

        self.horizontalLayout_28.addWidget(self.buscarcliente)


        self.verticalLayout_18.addWidget(self.widget_40)

        self.listView = QListView(self.widget_39)
        self.listView.setObjectName(u"listView")
        self.listView.setStyleSheet(u"QListView::item {\n"
"        background-color: rgba(7, 39, 67, 140);; /* Color de la tarjeta */\n"
"        border: 1px solid #ddd;\n"
"        border-radius: 10px;       /* <--- AQU\u00cd sucede la magia */\n"
"        padding: 0px;\n"
"        margin: 0px;\n"
"		margin-bottom: 3px;\n"
"    }\n"
"\n"
"QListView::item:selected {\n"
"        background-color: #3498db; /* Azul cuando se selecciona */\n"
"        color: white;\n"
"        border: 1px solid #2980b9;\n"
"    }\n"
"\n"
"QListView::item:hover {\n"
"        background-color: #3498db; /* Color al pasar el mouse */\n"
"    }")
        self.listView.setAutoScrollMargin(16)
        self.listView.setEditTriggers(QAbstractItemView.EditTrigger.NoEditTriggers)
        self.listView.setAlternatingRowColors(True)
        self.listView.setIconSize(QSize(50, 50))
        self.listView.setHorizontalScrollMode(QAbstractItemView.ScrollMode.ScrollPerPixel)
        self.listView.setMovement(QListView.Movement.Static)

        self.verticalLayout_18.addWidget(self.listView)

        self.verticalSpacer_7 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)

        self.verticalLayout_18.addItem(self.verticalSpacer_7)

        self.label_31 = QLabel(self.widget_39)
        self.label_31.setObjectName(u"label_31")
        self.label_31.setMinimumSize(QSize(0, 0))
        font16 = QFont()
        font16.setPointSize(14)
        font16.setBold(True)
        self.label_31.setFont(font16)
        self.label_31.setMargin(0)

        self.verticalLayout_18.addWidget(self.label_31)

        self.listView_2 = QListView(self.widget_39)
        self.listView_2.setObjectName(u"listView_2")
        self.listView_2.setStyleSheet(u"QListView::item {\n"
"        background-color: rgba(7, 39, 67, 140);; /* Color de la tarjeta */\n"
"        border: 1px solid #ddd;\n"
"        border-radius: 10px;       /* <--- AQU\u00cd sucede la magia */\n"
"        padding: 0px;\n"
"        margin: 0px;\n"
"		margin-bottom: 3px;\n"
"    }\n"
"\n"
"QListView::item:selected {\n"
"        background-color: #3498db; /* Azul cuando se selecciona */\n"
"        color: white;\n"
"        border: 1px solid #2980b9;\n"
"    }\n"
"\n"
"QListView::item:hover {\n"
"        background-color: #3498db; /* Color al pasar el mouse */\n"
"    }")
        self.listView_2.setEditTriggers(QAbstractItemView.EditTrigger.NoEditTriggers)
        self.listView_2.setIconSize(QSize(100, 100))
        self.listView_2.setVerticalScrollMode(QAbstractItemView.ScrollMode.ScrollPerPixel)
        self.listView_2.setMovement(QListView.Movement.Static)
        self.listView_2.setFlow(QListView.Flow.TopToBottom)

        self.verticalLayout_18.addWidget(self.listView_2)


        self.gridLayout_3.addWidget(self.widget_39, 0, 2, 1, 1)

        self.widget_35 = QWidget(self.page_5)
        self.widget_35.setObjectName(u"widget_35")
        self.widget_35.setMaximumSize(QSize(450, 16777215))
        self.verticalLayout_16 = QVBoxLayout(self.widget_35)
        self.verticalLayout_16.setObjectName(u"verticalLayout_16")
        self.label_6 = QLabel(self.widget_35)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setPixmap(QPixmap(u"../../../.designer/backup/iconos/clientes.ico"))

        self.verticalLayout_16.addWidget(self.label_6)

        self.label_54 = QLabel(self.widget_35)
        self.label_54.setObjectName(u"label_54")
        self.label_54.setFont(font7)

        self.verticalLayout_16.addWidget(self.label_54)

        self.idcliente = QLineEdit(self.widget_35)
        self.idcliente.setObjectName(u"idcliente")
        self.idcliente.setMaximumSize(QSize(400, 16777215))
        self.idcliente.setFont(font7)
        self.idcliente.setReadOnly(True)

        self.verticalLayout_16.addWidget(self.idcliente)

        self.label_50 = QLabel(self.widget_35)
        self.label_50.setObjectName(u"label_50")
        self.label_50.setFont(font7)

        self.verticalLayout_16.addWidget(self.label_50)

        self.nombre = QLineEdit(self.widget_35)
        self.nombre.setObjectName(u"nombre")
        self.nombre.setMaximumSize(QSize(400, 16777215))
        self.nombre.setFont(font7)
        self.nombre.setReadOnly(False)

        self.verticalLayout_16.addWidget(self.nombre)

        self.label_52 = QLabel(self.widget_35)
        self.label_52.setObjectName(u"label_52")
        self.label_52.setFont(font7)

        self.verticalLayout_16.addWidget(self.label_52)

        self.telefono = QLineEdit(self.widget_35)
        self.telefono.setObjectName(u"telefono")
        self.telefono.setMaximumSize(QSize(400, 16777215))
        self.telefono.setFont(font7)

        self.verticalLayout_16.addWidget(self.telefono)

        self.label_49 = QLabel(self.widget_35)
        self.label_49.setObjectName(u"label_49")
        self.label_49.setFont(font7)

        self.verticalLayout_16.addWidget(self.label_49)

        self.email = QLineEdit(self.widget_35)
        self.email.setObjectName(u"email")
        self.email.setMaximumSize(QSize(400, 16777215))
        self.email.setFont(font7)

        self.verticalLayout_16.addWidget(self.email)

        self.label_51 = QLabel(self.widget_35)
        self.label_51.setObjectName(u"label_51")
        self.label_51.setFont(font7)

        self.verticalLayout_16.addWidget(self.label_51)

        self.rfc = QLineEdit(self.widget_35)
        self.rfc.setObjectName(u"rfc")
        self.rfc.setMaximumSize(QSize(400, 16777215))
        self.rfc.setFont(font7)
        self.rfc.setStyleSheet(u"")

        self.verticalLayout_16.addWidget(self.rfc)

        self.label_53 = QLabel(self.widget_35)
        self.label_53.setObjectName(u"label_53")
        self.label_53.setFont(font7)

        self.verticalLayout_16.addWidget(self.label_53)

        self.direccion = QTextEdit(self.widget_35)
        self.direccion.setObjectName(u"direccion")
        self.direccion.setMaximumSize(QSize(400, 50))
        self.direccion.setFont(font7)
        self.direccion.setStyleSheet(u"border: 5px ;\n"
"border-radius: 10px;\n"
"\n"
"")

        self.verticalLayout_16.addWidget(self.direccion)

        self.widget_37 = QWidget(self.widget_35)
        self.widget_37.setObjectName(u"widget_37")

        self.verticalLayout_16.addWidget(self.widget_37)

        self.verticalSpacer_3 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_16.addItem(self.verticalSpacer_3)

        self.widget_78 = QWidget(self.widget_35)
        self.widget_78.setObjectName(u"widget_78")
        self.horizontalLayout_54 = QHBoxLayout(self.widget_78)
        self.horizontalLayout_54.setObjectName(u"horizontalLayout_54")
        self.btnnuevoclient = QToolButton(self.widget_78)
        self.btnnuevoclient.setObjectName(u"btnnuevoclient")
        self.btnnuevoclient.setIcon(icon13)
        self.btnnuevoclient.setIconSize(QSize(55, 40))
        self.btnnuevoclient.setToolButtonStyle(Qt.ToolButtonStyle.ToolButtonTextUnderIcon)

        self.horizontalLayout_54.addWidget(self.btnnuevoclient)

        self.btneditaclient = QToolButton(self.widget_78)
        self.btneditaclient.setObjectName(u"btneditaclient")
        self.btneditaclient.setIcon(icon12)
        self.btneditaclient.setIconSize(QSize(55, 40))
        self.btneditaclient.setToolButtonStyle(Qt.ToolButtonStyle.ToolButtonTextUnderIcon)

        self.horizontalLayout_54.addWidget(self.btneditaclient)

        self.btnguardaclient = QToolButton(self.widget_78)
        self.btnguardaclient.setObjectName(u"btnguardaclient")
        self.btnguardaclient.setMinimumSize(QSize(62, 0))
        self.btnguardaclient.setIcon(icon19)
        self.btnguardaclient.setIconSize(QSize(40, 40))
        self.btnguardaclient.setToolButtonStyle(Qt.ToolButtonStyle.ToolButtonTextUnderIcon)

        self.horizontalLayout_54.addWidget(self.btnguardaclient)


        self.verticalLayout_16.addWidget(self.widget_78)


        self.gridLayout_3.addWidget(self.widget_35, 0, 1, 1, 1)

        self.stack.addWidget(self.page_5)
        self.page_6 = QWidget()
        self.page_6.setObjectName(u"page_6")
        self.gridLayout_14 = QGridLayout(self.page_6)
        self.gridLayout_14.setObjectName(u"gridLayout_14")
        self.gridLayout_14.setVerticalSpacing(0)
        self.gridLayout_14.setContentsMargins(-1, -1, 0, -1)
        self.scrollArea_2 = QScrollArea(self.page_6)
        self.scrollArea_2.setObjectName(u"scrollArea_2")
        self.scrollArea_2.setWidgetResizable(True)
        self.scrollAreaWidgetContents_2 = QWidget()
        self.scrollAreaWidgetContents_2.setObjectName(u"scrollAreaWidgetContents_2")
        self.scrollAreaWidgetContents_2.setGeometry(QRect(0, 0, 745, 282))
        self.verticalLayout_48 = QVBoxLayout(self.scrollAreaWidgetContents_2)
        self.verticalLayout_48.setObjectName(u"verticalLayout_48")
        self.verticalLayout_48.setContentsMargins(-1, -1, 0, -1)
        self.widget_79 = QWidget(self.scrollAreaWidgetContents_2)
        self.widget_79.setObjectName(u"widget_79")
        self.horizontalLayout_55 = QHBoxLayout(self.widget_79)
        self.horizontalLayout_55.setObjectName(u"horizontalLayout_55")
        self.horizontalLayout_55.setContentsMargins(-1, -1, 0, -1)
        self.widget_36 = QWidget(self.widget_79)
        self.widget_36.setObjectName(u"widget_36")
        self.verticalLayout_46 = QVBoxLayout(self.widget_36)
        self.verticalLayout_46.setObjectName(u"verticalLayout_46")
        self.widget_55 = QWidget(self.widget_36)
        self.widget_55.setObjectName(u"widget_55")
        self.gridLayout_15 = QGridLayout(self.widget_55)
        self.gridLayout_15.setObjectName(u"gridLayout_15")
        self.gridLayout_15.setContentsMargins(-1, -1, -1, 0)
        self.widget_68 = QWidget(self.widget_55)
        self.widget_68.setObjectName(u"widget_68")
        self.gridLayout_28 = QGridLayout(self.widget_68)
        self.gridLayout_28.setObjectName(u"gridLayout_28")
        self.label_90 = QLabel(self.widget_68)
        self.label_90.setObjectName(u"label_90")
        self.label_90.setFont(font12)

        self.gridLayout_28.addWidget(self.label_90, 0, 0, 1, 1)

        self.fechape_1 = QDateTimeEdit(self.widget_68)
        self.fechape_1.setObjectName(u"fechape_1")
        self.fechape_1.setMaximumSize(QSize(20, 28))
        self.fechape_1.setWrapping(False)
        self.fechape_1.setReadOnly(False)
        self.fechape_1.setButtonSymbols(QAbstractSpinBox.ButtonSymbols.NoButtons)
        self.fechape_1.setAccelerated(True)
        self.fechape_1.setMaximumDateTime(QDateTime(QDate(9999, 12, 12), QTime(23, 59, 59)))
        self.fechape_1.setMinimumDateTime(QDateTime(QDate(2000, 1, 1), QTime(0, 0, 0)))
        self.fechape_1.setCalendarPopup(True)

        self.gridLayout_28.addWidget(self.fechape_1, 0, 2, 1, 1)

        self.label_91 = QLabel(self.widget_68)
        self.label_91.setObjectName(u"label_91")
        self.label_91.setFont(font12)

        self.gridLayout_28.addWidget(self.label_91, 0, 3, 1, 1)

        self.fechap_1 = QLineEdit(self.widget_68)
        self.fechap_1.setObjectName(u"fechap_1")
        self.fechap_1.setMinimumSize(QSize(0, 0))
        self.fechap_1.setMaximumSize(QSize(280, 16777215))
        self.fechap_1.setFont(font12)
        self.fechap_1.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)
        self.fechap_1.setReadOnly(True)

        self.gridLayout_28.addWidget(self.fechap_1, 0, 1, 1, 1)

        self.fechap_2 = QLineEdit(self.widget_68)
        self.fechap_2.setObjectName(u"fechap_2")
        self.fechap_2.setMinimumSize(QSize(0, 0))
        self.fechap_2.setMaximumSize(QSize(280, 16777215))
        self.fechap_2.setFont(font12)
        self.fechap_2.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)
        self.fechap_2.setReadOnly(True)

        self.gridLayout_28.addWidget(self.fechap_2, 0, 5, 1, 1)

        self.fechape_2 = QDateTimeEdit(self.widget_68)
        self.fechape_2.setObjectName(u"fechape_2")
        self.fechape_2.setMaximumSize(QSize(20, 28))
        self.fechape_2.setWrapping(False)
        self.fechape_2.setReadOnly(False)
        self.fechape_2.setButtonSymbols(QAbstractSpinBox.ButtonSymbols.NoButtons)
        self.fechape_2.setAccelerated(True)
        self.fechape_2.setMinimumDateTime(QDateTime(QDate(2000, 1, 1), QTime(0, 0, 0)))
        self.fechape_2.setCalendarPopup(True)

        self.gridLayout_28.addWidget(self.fechape_2, 0, 6, 1, 1)

        self.horizontalSpacer_29 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_28.addItem(self.horizontalSpacer_29, 0, 8, 1, 1)

        self.btnlimpiar = QToolButton(self.widget_68)
        self.btnlimpiar.setObjectName(u"btnlimpiar")
        self.btnlimpiar.setMaximumSize(QSize(16777215, 30))
        self.btnlimpiar.setFont(font2)
        self.btnlimpiar.setIcon(icon26)
        self.btnlimpiar.setIconSize(QSize(20, 20))
        self.btnlimpiar.setToolButtonStyle(Qt.ToolButtonStyle.ToolButtonTextUnderIcon)

        self.gridLayout_28.addWidget(self.btnlimpiar, 0, 7, 1, 1)


        self.gridLayout_15.addWidget(self.widget_68, 2, 0, 1, 4)

        self.label_7 = QLabel(self.widget_55)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setFont(font7)

        self.gridLayout_15.addWidget(self.label_7, 0, 0, 1, 1)

        self.tecnico_p = QComboBox(self.widget_55)
        self.tecnico_p.setObjectName(u"tecnico_p")
        self.tecnico_p.setFont(font8)

        self.gridLayout_15.addWidget(self.tecnico_p, 0, 1, 1, 2)

        self.horizontalSpacer_28 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_15.addItem(self.horizontalSpacer_28, 0, 4, 1, 1)

        self.widget_56 = QWidget(self.widget_55)
        self.widget_56.setObjectName(u"widget_56")
        self.horizontalLayout_40 = QHBoxLayout(self.widget_56)
        self.horizontalLayout_40.setObjectName(u"horizontalLayout_40")
        self.toolButton_6 = QToolButton(self.widget_56)
        self.toolButton_6.setObjectName(u"toolButton_6")
        self.toolButton_6.setEnabled(False)
        self.toolButton_6.setIcon(icon21)
        self.toolButton_6.setIconSize(QSize(22, 22))
        self.toolButton_6.setToolButtonStyle(Qt.ToolButtonStyle.ToolButtonIconOnly)

        self.horizontalLayout_40.addWidget(self.toolButton_6)

        self.buscarp = QLineEdit(self.widget_56)
        self.buscarp.setObjectName(u"buscarp")
        self.buscarp.setFont(font9)
        self.buscarp.setFocusPolicy(Qt.FocusPolicy.StrongFocus)
        self.buscarp.setAutoFillBackground(False)
        self.buscarp.setClearButtonEnabled(True)

        self.horizontalLayout_40.addWidget(self.buscarp)


        self.gridLayout_15.addWidget(self.widget_56, 3, 1, 1, 2)

        self.horizontalSpacer_19 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_15.addItem(self.horizontalSpacer_19, 0, 3, 1, 1)

        self.seleccp = QCheckBox(self.widget_55)
        self.seleccp.setObjectName(u"seleccp")

        self.gridLayout_15.addWidget(self.seleccp, 3, 0, 1, 1)

        self.horizontalSpacer_13 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_15.addItem(self.horizontalSpacer_13, 3, 3, 1, 1)

        self.widget_4 = QWidget(self.widget_55)
        self.widget_4.setObjectName(u"widget_4")

        self.gridLayout_15.addWidget(self.widget_4, 1, 0, 1, 2)


        self.verticalLayout_46.addWidget(self.widget_55)

        self.tablapagos = QTableView(self.widget_36)
        self.tablapagos.setObjectName(u"tablapagos")
        self.tablapagos.setSelectionBehavior(QAbstractItemView.SelectionBehavior.SelectRows)
        self.tablapagos.horizontalHeader().setStretchLastSection(True)

        self.verticalLayout_46.addWidget(self.tablapagos)


        self.horizontalLayout_55.addWidget(self.widget_36)

        self.widget_71 = QWidget(self.widget_79)
        self.widget_71.setObjectName(u"widget_71")
        sizePolicy.setHeightForWidth(self.widget_71.sizePolicy().hasHeightForWidth())
        self.widget_71.setSizePolicy(sizePolicy)
        self.verticalLayout_47 = QVBoxLayout(self.widget_71)
        self.verticalLayout_47.setObjectName(u"verticalLayout_47")
        self.verticalLayout_47.setContentsMargins(0, 0, 0, 0)
        self.Graficas = QWidget(self.widget_71)
        self.Graficas.setObjectName(u"Graficas")
        sizePolicy.setHeightForWidth(self.Graficas.sizePolicy().hasHeightForWidth())
        self.Graficas.setSizePolicy(sizePolicy)
        self.Graficas.setMaximumSize(QSize(300, 16777215))
        self.verticalLayout_32 = QVBoxLayout(self.Graficas)
        self.verticalLayout_32.setObjectName(u"verticalLayout_32")
        self.verticalLayout_32.setContentsMargins(-1, 0, 0, -1)
        self.label_125 = QLabel(self.Graficas)
        self.label_125.setObjectName(u"label_125")
        self.label_125.setFont(font11)

        self.verticalLayout_32.addWidget(self.label_125)

        self.widget_77 = QWidget(self.Graficas)
        self.widget_77.setObjectName(u"widget_77")
        self.horizontalLayout_53 = QHBoxLayout(self.widget_77)
        self.horizontalLayout_53.setObjectName(u"horizontalLayout_53")
        self.horizontalLayout_53.setContentsMargins(-1, 0, -1, 0)
        self.labely = QLabel(self.widget_77)
        self.labely.setObjectName(u"labely")
        self.labely.setFont(font8)

        self.horizontalLayout_53.addWidget(self.labely)

        self.btncambiografica = QToolButton(self.widget_77)
        self.btncambiografica.setObjectName(u"btncambiografica")
        icon34 = QIcon(QIcon.fromTheme(u"go-next"))
        self.btncambiografica.setIcon(icon34)

        self.horizontalLayout_53.addWidget(self.btncambiografica)


        self.verticalLayout_32.addWidget(self.widget_77)

        self.labelPromedio = QLabel(self.Graficas)
        self.labelPromedio.setObjectName(u"labelPromedio")
        self.labelPromedio.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_32.addWidget(self.labelPromedio)

        self.grafica1 = QChartView(self.Graficas)
        self.grafica1.setObjectName(u"grafica1")

        self.verticalLayout_32.addWidget(self.grafica1)

        self.grafica2 = QChartView(self.Graficas)
        self.grafica2.setObjectName(u"grafica2")

        self.verticalLayout_32.addWidget(self.grafica2)

        self.grafica3 = QChartView(self.Graficas)
        self.grafica3.setObjectName(u"grafica3")

        self.verticalLayout_32.addWidget(self.grafica3)


        self.verticalLayout_47.addWidget(self.Graficas)

        self.widget_57 = QWidget(self.widget_71)
        self.widget_57.setObjectName(u"widget_57")
        sizePolicy.setHeightForWidth(self.widget_57.sizePolicy().hasHeightForWidth())
        self.widget_57.setSizePolicy(sizePolicy)
        self.gridLayout_16 = QGridLayout(self.widget_57)
        self.gridLayout_16.setObjectName(u"gridLayout_16")
        self.gridLayout_16.setContentsMargins(-1, -1, -1, 0)
        self.widget_70 = QWidget(self.widget_57)
        self.widget_70.setObjectName(u"widget_70")
        self.horizontalLayout_51 = QHBoxLayout(self.widget_70)
        self.horizontalLayout_51.setObjectName(u"horizontalLayout_51")
        self.btnautorizap = QToolButton(self.widget_70)
        self.btnautorizap.setObjectName(u"btnautorizap")
        self.btnautorizap.setMinimumSize(QSize(62, 0))
        self.btnautorizap.setIcon(icon10)
        self.btnautorizap.setIconSize(QSize(40, 40))
        self.btnautorizap.setToolButtonStyle(Qt.ToolButtonStyle.ToolButtonTextUnderIcon)

        self.horizontalLayout_51.addWidget(self.btnautorizap)


        self.gridLayout_16.addWidget(self.widget_70, 3, 0, 1, 1)

        self.widget_69 = QWidget(self.widget_57)
        self.widget_69.setObjectName(u"widget_69")
        self.horizontalLayout_50 = QHBoxLayout(self.widget_69)
        self.horizontalLayout_50.setObjectName(u"horizontalLayout_50")
        self.label_61 = QLabel(self.widget_69)
        self.label_61.setObjectName(u"label_61")
        self.label_61.setMaximumSize(QSize(20, 16777215))
        self.label_61.setFont(font6)
        self.label_61.setLayoutDirection(Qt.LayoutDirection.LeftToRight)

        self.horizontalLayout_50.addWidget(self.label_61)

        self.total_p = QLabel(self.widget_69)
        self.total_p.setObjectName(u"total_p")
        self.total_p.setFont(font11)

        self.horizontalLayout_50.addWidget(self.total_p)


        self.gridLayout_16.addWidget(self.widget_69, 2, 0, 1, 1)

        self.verticalSpacer_12 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Ignored)

        self.gridLayout_16.addItem(self.verticalSpacer_12, 1, 0, 1, 1)


        self.verticalLayout_47.addWidget(self.widget_57)


        self.horizontalLayout_55.addWidget(self.widget_71)


        self.verticalLayout_48.addWidget(self.widget_79)

        self.scrollArea_2.setWidget(self.scrollAreaWidgetContents_2)

        self.gridLayout_14.addWidget(self.scrollArea_2, 0, 0, 1, 2)

        self.stack.addWidget(self.page_6)
        self.page_7 = QWidget()
        self.page_7.setObjectName(u"page_7")
        self.horizontalLayout_41 = QHBoxLayout(self.page_7)
        self.horizontalLayout_41.setObjectName(u"horizontalLayout_41")
        self.listWidget = QListWidget(self.page_7)
        icon35 = QIcon()
        icon35.addFile(u":/iconos/iconos/big-data.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        __qlistwidgetitem = QListWidgetItem(self.listWidget)
        __qlistwidgetitem.setIcon(icon35)
        icon36 = QIcon()
        icon36.addFile(u":/iconos/iconos/company.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        __qlistwidgetitem1 = QListWidgetItem(self.listWidget)
        __qlistwidgetitem1.setIcon(icon36)
        icon37 = QIcon()
        icon37.addFile(u":/iconos/iconos/settings.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        __qlistwidgetitem2 = QListWidgetItem(self.listWidget)
        __qlistwidgetitem2.setIcon(icon37)
        __qlistwidgetitem2.setFlags(Qt.ItemIsSelectable|Qt.ItemIsDragEnabled|Qt.ItemIsUserCheckable)
        icon38 = QIcon()
        icon38.addFile(u":/iconos/iconos/acerca-de.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        __qlistwidgetitem3 = QListWidgetItem(self.listWidget)
        __qlistwidgetitem3.setIcon(icon38)
        self.listWidget.setObjectName(u"listWidget")
        self.listWidget.setEnabled(True)
        self.listWidget.setMaximumSize(QSize(300, 16777215))
        font17 = QFont()
        font17.setPointSize(12)
        font17.setItalic(False)
        self.listWidget.setFont(font17)
        self.listWidget.setMouseTracking(False)
        self.listWidget.setIconSize(QSize(40, 40))
        self.listWidget.setViewMode(QListView.ViewMode.ListMode)

        self.horizontalLayout_41.addWidget(self.listWidget)

        self.stackedWidget = QStackedWidget(self.page_7)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.stackedWidget.setFont(font7)
        self.page_16 = QWidget()
        self.page_16.setObjectName(u"page_16")
        self.verticalLayout_43 = QVBoxLayout(self.page_16)
        self.verticalLayout_43.setObjectName(u"verticalLayout_43")
        self.groupBox_16 = QGroupBox(self.page_16)
        self.groupBox_16.setObjectName(u"groupBox_16")
        self.groupBox_16.setEnabled(False)
        self.verticalLayout_44 = QVBoxLayout(self.groupBox_16)
        self.verticalLayout_44.setObjectName(u"verticalLayout_44")
        self.widget_75 = QWidget(self.groupBox_16)
        self.widget_75.setObjectName(u"widget_75")
        self.horizontalLayout_16 = QHBoxLayout(self.widget_75)
        self.horizontalLayout_16.setObjectName(u"horizontalLayout_16")
        self.label_8 = QLabel(self.widget_75)
        self.label_8.setObjectName(u"label_8")

        self.horizontalLayout_16.addWidget(self.label_8)

        self.horizontalSlider = QSlider(self.widget_75)
        self.horizontalSlider.setObjectName(u"horizontalSlider")
        self.horizontalSlider.setMaximumSize(QSize(30, 16777215))
        self.horizontalSlider.setStyleSheet(u"color: rgb(89, 255, 28)")
        self.horizontalSlider.setMaximum(1)
        self.horizontalSlider.setPageStep(1)
        self.horizontalSlider.setOrientation(Qt.Orientation.Horizontal)
        self.horizontalSlider.setInvertedAppearance(False)
        self.horizontalSlider.setInvertedControls(False)

        self.horizontalLayout_16.addWidget(self.horizontalSlider)

        self.horizontalSpacer_30 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_16.addItem(self.horizontalSpacer_30)


        self.verticalLayout_44.addWidget(self.widget_75)

        self.radioButton = QRadioButton(self.groupBox_16)
        self.radioButton.setObjectName(u"radioButton")
        self.radioButton.setFont(font8)

        self.verticalLayout_44.addWidget(self.radioButton)

        self.radioButton_2 = QRadioButton(self.groupBox_16)
        self.radioButton_2.setObjectName(u"radioButton_2")
        self.radioButton_2.setFont(font8)

        self.verticalLayout_44.addWidget(self.radioButton_2)

        self.label_12 = QLabel(self.groupBox_16)
        self.label_12.setObjectName(u"label_12")

        self.verticalLayout_44.addWidget(self.label_12)

        self.widget_76 = QWidget(self.groupBox_16)
        self.widget_76.setObjectName(u"widget_76")
        self.formLayout = QFormLayout(self.widget_76)
        self.formLayout.setObjectName(u"formLayout")
        self.label_15 = QLabel(self.widget_76)
        self.label_15.setObjectName(u"label_15")

        self.formLayout.setWidget(0, QFormLayout.ItemRole.LabelRole, self.label_15)

        self.lineEdit = QLineEdit(self.widget_76)
        self.lineEdit.setObjectName(u"lineEdit")

        self.formLayout.setWidget(0, QFormLayout.ItemRole.FieldRole, self.lineEdit)

        self.label_18 = QLabel(self.widget_76)
        self.label_18.setObjectName(u"label_18")

        self.formLayout.setWidget(1, QFormLayout.ItemRole.LabelRole, self.label_18)

        self.lineEdit_2 = QLineEdit(self.widget_76)
        self.lineEdit_2.setObjectName(u"lineEdit_2")

        self.formLayout.setWidget(1, QFormLayout.ItemRole.FieldRole, self.lineEdit_2)


        self.verticalLayout_44.addWidget(self.widget_76)

        self.verticalSpacer_11 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_44.addItem(self.verticalSpacer_11)


        self.verticalLayout_43.addWidget(self.groupBox_16)

        self.groupBox_17 = QGroupBox(self.page_16)
        self.groupBox_17.setObjectName(u"groupBox_17")
        self.gridLayout_29 = QGridLayout(self.groupBox_17)
        self.gridLayout_29.setObjectName(u"gridLayout_29")
        self.cprep = QToolButton(self.groupBox_17)
        self.cprep.setObjectName(u"cprep")
        icon39 = QIcon()
        icon39.addFile(u":/iconos/iconos/cpreparaciones.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.cprep.setIcon(icon39)
        self.cprep.setIconSize(QSize(50, 50))
        self.cprep.setToolButtonStyle(Qt.ToolButtonStyle.ToolButtonTextUnderIcon)

        self.gridLayout_29.addWidget(self.cprep, 1, 0, 1, 1)

        self.stackedprogres = QStackedWidget(self.groupBox_17)
        self.stackedprogres.setObjectName(u"stackedprogres")
        self.stackedprogres.setMaximumSize(QSize(16777215, 50))
        self.page_19 = QWidget()
        self.page_19.setObjectName(u"page_19")
        self.stackedprogres.addWidget(self.page_19)
        self.page_20 = QWidget()
        self.page_20.setObjectName(u"page_20")
        self.verticalLayout_45 = QVBoxLayout(self.page_20)
        self.verticalLayout_45.setObjectName(u"verticalLayout_45")
        self.progressBar = QProgressBar(self.page_20)
        self.progressBar.setObjectName(u"progressBar")
        self.progressBar.setEnabled(True)
        self.progressBar.setValue(0)

        self.verticalLayout_45.addWidget(self.progressBar)

        self.stackedprogres.addWidget(self.page_20)

        self.gridLayout_29.addWidget(self.stackedprogres, 2, 0, 1, 2)

        self.horizontalSpacer_31 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_29.addItem(self.horizontalSpacer_31, 1, 1, 1, 1)

        self.label_21 = QLabel(self.groupBox_17)
        self.label_21.setObjectName(u"label_21")

        self.gridLayout_29.addWidget(self.label_21, 0, 0, 1, 1)

        self.verticalSpacer_15 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.gridLayout_29.addItem(self.verticalSpacer_15, 3, 0, 1, 1)


        self.verticalLayout_43.addWidget(self.groupBox_17)

        self.stackedWidget.addWidget(self.page_16)
        self.page_14 = QWidget()
        self.page_14.setObjectName(u"page_14")
        self.verticalLayout_38 = QVBoxLayout(self.page_14)
        self.verticalLayout_38.setObjectName(u"verticalLayout_38")
        self.tabWidget = QTabWidget(self.page_14)
        self.tabWidget.setObjectName(u"tabWidget")
        self.tabWidget.setEnabled(True)
        self.tabWidget.setFont(font7)
        self.tab_7 = QWidget()
        self.tab_7.setObjectName(u"tab_7")
        self.gridLayout_17 = QGridLayout(self.tab_7)
        self.gridLayout_17.setObjectName(u"gridLayout_17")
        self.label_92 = QLabel(self.tab_7)
        self.label_92.setObjectName(u"label_92")

        self.gridLayout_17.addWidget(self.label_92, 4, 0, 1, 1)

        self.label_69 = QLabel(self.tab_7)
        self.label_69.setObjectName(u"label_69")
        self.label_69.setFrameShape(QFrame.Shape.NoFrame)
        self.label_69.setFrameShadow(QFrame.Shadow.Plain)

        self.gridLayout_17.addWidget(self.label_69, 0, 0, 1, 1)

        self.label_71 = QLabel(self.tab_7)
        self.label_71.setObjectName(u"label_71")

        self.gridLayout_17.addWidget(self.label_71, 1, 0, 1, 1)

        self.label_93 = QLabel(self.tab_7)
        self.label_93.setObjectName(u"label_93")

        self.gridLayout_17.addWidget(self.label_93, 5, 0, 1, 1)

        self.verticalSpacer_13 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.gridLayout_17.addItem(self.verticalSpacer_13, 8, 0, 1, 1)

        self.horizontalSpacer_21 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_17.addItem(self.horizontalSpacer_21, 9, 1, 1, 1)

        self.label_73 = QLabel(self.tab_7)
        self.label_73.setObjectName(u"label_73")

        self.gridLayout_17.addWidget(self.label_73, 2, 0, 1, 1)

        self.btnguardainfo = QToolButton(self.tab_7)
        self.btnguardainfo.setObjectName(u"btnguardainfo")
        self.btnguardainfo.setMinimumSize(QSize(62, 0))
        self.btnguardainfo.setIcon(icon19)
        self.btnguardainfo.setIconSize(QSize(40, 40))
        self.btnguardainfo.setToolButtonStyle(Qt.ToolButtonStyle.ToolButtonTextUnderIcon)

        self.gridLayout_17.addWidget(self.btnguardainfo, 9, 0, 1, 1)

        self.label_74 = QLabel(self.tab_7)
        self.label_74.setObjectName(u"label_74")

        self.gridLayout_17.addWidget(self.label_74, 3, 0, 1, 1)

        self.nombreemp = QLineEdit(self.tab_7)
        self.nombreemp.setObjectName(u"nombreemp")
        self.nombreemp.setClearButtonEnabled(False)

        self.gridLayout_17.addWidget(self.nombreemp, 0, 1, 1, 2)

        self.direccionemp = QLineEdit(self.tab_7)
        self.direccionemp.setObjectName(u"direccionemp")

        self.gridLayout_17.addWidget(self.direccionemp, 1, 1, 1, 2)

        self.tel1emp = QLineEdit(self.tab_7)
        self.tel1emp.setObjectName(u"tel1emp")

        self.gridLayout_17.addWidget(self.tel1emp, 2, 1, 1, 2)

        self.tel2emp = QLineEdit(self.tab_7)
        self.tel2emp.setObjectName(u"tel2emp")

        self.gridLayout_17.addWidget(self.tel2emp, 3, 1, 1, 2)

        self.pagweb = QLineEdit(self.tab_7)
        self.pagweb.setObjectName(u"pagweb")

        self.gridLayout_17.addWidget(self.pagweb, 4, 1, 1, 2)

        self.emailemp = QLineEdit(self.tab_7)
        self.emailemp.setObjectName(u"emailemp")

        self.gridLayout_17.addWidget(self.emailemp, 5, 1, 1, 2)

        self.groupBox_8 = QGroupBox(self.tab_7)
        self.groupBox_8.setObjectName(u"groupBox_8")
        self.groupBox_8.setEnabled(True)
        self.groupBox_8.setMaximumSize(QSize(16777215, 300))
        self.groupBox_8.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignTop)
        self.horizontalLayout_43 = QHBoxLayout(self.groupBox_8)
        self.horizontalLayout_43.setObjectName(u"horizontalLayout_43")
        self.horizontalLayout_43.setContentsMargins(-1, 0, -1, 0)
        self.logo = QLabel(self.groupBox_8)
        self.logo.setObjectName(u"logo")
        self.logo.setMinimumSize(QSize(200, 200))
        self.logo.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignTop)

        self.horizontalLayout_43.addWidget(self.logo)

        self.selarch = QPushButton(self.groupBox_8)
        self.selarch.setObjectName(u"selarch")
        self.selarch.setFont(font10)
        self.selarch.setAcceptDrops(False)
        self.selarch.setToolTipDuration(-1)
        self.selarch.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.selarch.setAutoFillBackground(False)
        icon40 = QIcon()
        icon40.addFile(u":/iconos/iconos/folder.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.selarch.setIcon(icon40)
        self.selarch.setIconSize(QSize(30, 30))

        self.horizontalLayout_43.addWidget(self.selarch)


        self.gridLayout_17.addWidget(self.groupBox_8, 0, 4, 6, 1)

        self.groupBox_7 = QGroupBox(self.tab_7)
        self.groupBox_7.setObjectName(u"groupBox_7")
        self.gridLayout_18 = QGridLayout(self.groupBox_7)
        self.gridLayout_18.setObjectName(u"gridLayout_18")
        self.label_94 = QLabel(self.groupBox_7)
        self.label_94.setObjectName(u"label_94")

        self.gridLayout_18.addWidget(self.label_94, 0, 0, 1, 1)

        self.notasal = QTextEdit(self.groupBox_7)
        self.notasal.setObjectName(u"notasal")

        self.gridLayout_18.addWidget(self.notasal, 1, 1, 1, 1)

        self.label_95 = QLabel(self.groupBox_7)
        self.label_95.setObjectName(u"label_95")

        self.gridLayout_18.addWidget(self.label_95, 1, 0, 1, 1)

        self.notaent = QTextEdit(self.groupBox_7)
        self.notaent.setObjectName(u"notaent")

        self.gridLayout_18.addWidget(self.notaent, 0, 1, 1, 1)


        self.gridLayout_17.addWidget(self.groupBox_7, 6, 0, 1, 5)

        self.tabWidget.addTab(self.tab_7, icon29, "")
        self.tab_8 = QWidget()
        self.tab_8.setObjectName(u"tab_8")
        self.tab_8.setEnabled(False)
        icon41 = QIcon(QIcon.fromTheme(u"document-open-recent"))
        self.tabWidget.addTab(self.tab_8, icon41, "")
        self.tab_9 = QWidget()
        self.tab_9.setObjectName(u"tab_9")
        self.tab_9.setEnabled(False)
        icon42 = QIcon(QIcon.fromTheme(u"document-properties"))
        self.tabWidget.addTab(self.tab_9, icon42, "")

        self.verticalLayout_38.addWidget(self.tabWidget)

        self.stackedWidget.addWidget(self.page_14)
        self.page_15 = QWidget()
        self.page_15.setObjectName(u"page_15")
        self.page_15.setFont(font2)
        self.label_68 = QLabel(self.page_15)
        self.label_68.setObjectName(u"label_68")
        self.label_68.setGeometry(QRect(240, 150, 111, 31))
        self.stackedWidget.addWidget(self.page_15)

        self.horizontalLayout_41.addWidget(self.stackedWidget)

        self.stack.addWidget(self.page_7)

        self.verticalLayout_2.addWidget(self.stack)


        self.horizontalLayout.addWidget(self.pprincipal)

        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)
        QWidget.setTabOrder(self.btninicio, self.btnregistros)
        QWidget.setTabOrder(self.btnregistros, self.btnreparaciones)
        QWidget.setTabOrder(self.btnreparaciones, self.btnentregas)
        QWidget.setTabOrder(self.btnentregas, self.btnclientes)
        QWidget.setTabOrder(self.btnclientes, self.btnpago)
        QWidget.setTabOrder(self.btnpago, self.btnconfig)
        QWidget.setTabOrder(self.btnconfig, self.scrollArea_4)
        QWidget.setTabOrder(self.scrollArea_4, self.cableac)
        QWidget.setTabOrder(self.cableac, self.controlr)
        QWidget.setTabOrder(self.controlr, self.eliminador)
        QWidget.setTabOrder(self.eliminador, self.base)
        QWidget.setTabOrder(self.base, self.basepared)
        QWidget.setTabOrder(self.basepared, self.pilas)
        QWidget.setTabOrder(self.pilas, self.cables)
        QWidget.setTabOrder(self.cables, self.accotro)
        QWidget.setTabOrder(self.accotro, self.rnombre)
        QWidget.setTabOrder(self.rnombre, self.rtelefono)
        QWidget.setTabOrder(self.rtelefono, self.rdireccion)
        QWidget.setTabOrder(self.rdireccion, self.remail)
        QWidget.setTabOrder(self.remail, self.rrfc)
        QWidget.setTabOrder(self.rrfc, self.rbtneditaclient)
        QWidget.setTabOrder(self.rbtneditaclient, self.btnnuevocliente)
        QWidget.setTabOrder(self.btnnuevocliente, self.btnimprimir)
        QWidget.setTabOrder(self.btnimprimir, self.btninicior)
        QWidget.setTabOrder(self.btninicior, self.btnant)
        QWidget.setTabOrder(self.btnant, self.btnsig)
        QWidget.setTabOrder(self.btnsig, self.btnfin)
        QWidget.setTabOrder(self.btnfin, self.btnnuevo)
        QWidget.setTabOrder(self.btnnuevo, self.btneliminar)
        QWidget.setTabOrder(self.btneliminar, self.btnguardar)
        QWidget.setTabOrder(self.btnguardar, self.tabregistros)
        QWidget.setTabOrder(self.tabregistros, self.buscarreg)
        QWidget.setTabOrder(self.buscarreg, self.tableViewregistros)
        QWidget.setTabOrder(self.tableViewregistros, self.listaentregas)
        QWidget.setTabOrder(self.listaentregas, self.idcliente)
        QWidget.setTabOrder(self.idcliente, self.nombre)
        QWidget.setTabOrder(self.nombre, self.telefono)
        QWidget.setTabOrder(self.telefono, self.email)
        QWidget.setTabOrder(self.email, self.rfc)
        QWidget.setTabOrder(self.rfc, self.direccion)
        QWidget.setTabOrder(self.direccion, self.buscarcliente)
        QWidget.setTabOrder(self.buscarcliente, self.listView)
        QWidget.setTabOrder(self.listView, self.listView_2)
        QWidget.setTabOrder(self.listView_2, self.toolButton)
        QWidget.setTabOrder(self.toolButton, self.buscar)
        QWidget.setTabOrder(self.buscar, self.btnmenu)

        self.retranslateUi(MainWindow)

        self.stack.setCurrentIndex(2)
        self.tabregistros.setCurrentIndex(0)
        self.stackinfrep_3.setCurrentIndex(1)
        self.stackreparaciones.setCurrentIndex(0)
        self.tabrepara.setCurrentIndex(1)
        self.stackinfrep.setCurrentIndex(1)
        self.entregas.setCurrentIndex(0)
        self.stackinfrep_2.setCurrentIndex(1)
        self.stackedWidget.setCurrentIndex(0)
        self.stackedprogres.setCurrentIndex(0)
        self.tabWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Martin Electronic's", None))
        self.btninicio.setText(QCoreApplication.translate("MainWindow", u"   Inicio", None))
        self.btnregistros.setText(QCoreApplication.translate("MainWindow", u"  Registros", None))
        self.btnreparaciones.setText(QCoreApplication.translate("MainWindow", u"   Reparaciones", None))
        self.btnentregas.setText(QCoreApplication.translate("MainWindow", u"   Entregas", None))
        self.btnclientes.setText(QCoreApplication.translate("MainWindow", u"   Clientes", None))
        self.btnpago.setText(QCoreApplication.translate("MainWindow", u"    Pago", None))
        self.btnconfig.setText(QCoreApplication.translate("MainWindow", u"Configuraci\u00f3n", None))
        self.btnmenu.setText("")
        self.atras.setText("")
        self.label.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\">Martin Electronic's</p></body></html>", None))
        self.label_59.setText(QCoreApplication.translate("MainWindow", u"Bienvenido: ", None))
        self.usuario.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.pendrev.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:20pt; font-weight:700;\">0</span></p></body></html>", None))
        self.label_13.setText("")
        self.label_9.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-weight:700;\">Pendientes de revici\u00f3n</span></p></body></html>", None))
        self.pendconf.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:20pt; font-weight:700;\">0</span></p></body></html>", None))
        self.label_16.setText("")
        self.label_17.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-weight:700;\">Pendientes de confirmaci\u00f3n</span></p></body></html>", None))
        self.pendrep.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:20pt; font-weight:700;\">0</span></p></body></html>", None))
        self.label_10.setText("")
        self.label_14.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-weight:700;\">Pendientes de reparaci\u00f3n</span></p></body></html>", None))
        self.teet.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:20pt; font-weight:700;\">0</span></p></body></html>", None))
        self.label_22.setText("")
        self.label_23.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-weight:700;\">Total de equipos en el taller</span></p></body></html>", None))
        self.totalreg.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:20pt; font-weight:700;\">0</span></p></body></html>", None))
        self.label_28.setText("")
        self.label_29.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-weight:700;\">Total de registros</span></p></body></html>", None))
        self.totalclientes.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:20pt; font-weight:700;\">0</span></p></body></html>", None))
        self.label_30.setText("")
        self.label_32.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-weight:700;\">Clientes</span></p></body></html>", None))
        self.label_19.setText("")
        self.pagact.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:20pt; font-weight:700;\">0</span></p></body></html>", None))
        self.label_20.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\">Pago actual</p></body></html>", None))
        self.groupBox_14.setTitle(QCoreApplication.translate("MainWindow", u"Top Clientes", None))
        self.groupBox_15.setTitle(QCoreApplication.translate("MainWindow", u"Top Tecnicos", None))
        self.label_11.setText(QCoreApplication.translate("MainWindow", u"Tiempo de entrega", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:11pt; font-weight:700;\">Presupuesto:</span></p></body></html>", None))
        self.btnconfirmarpre.setText(QCoreApplication.translate("MainWindow", u"Confirmar Presupuesto", None))
        self.label_36.setText(QCoreApplication.translate("MainWindow", u"Orden de servicio:", None))
        self.ods.setSpecialValueText(QCoreApplication.translate("MainWindow", u"--", None))
        self.label_38.setText(QCoreApplication.translate("MainWindow", u"Registro:", None))
        self.no.setText(QCoreApplication.translate("MainWindow", u"--", None))
        self.label_40.setText(QCoreApplication.translate("MainWindow", u"de", None))
        self.de.setText(QCoreApplication.translate("MainWindow", u"--", None))
        self.btnimprimir.setText(QCoreApplication.translate("MainWindow", u"Imprimir", None))
        self.label_48.setText(QCoreApplication.translate("MainWindow", u"Fecha de recepci\u00f3n: ", None))
        self.fecha.setText(QCoreApplication.translate("MainWindow", u"--", None))
        self.infoequipo.setTitle(QCoreApplication.translate("MainWindow", u"Informaci\u00f3n del equipo.", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Equipo:", None))
        self.label_24.setText(QCoreApplication.translate("MainWindow", u"Marca:", None))
        self.label_25.setText(QCoreApplication.translate("MainWindow", u"Modelo:", None))
        self.label_26.setText(QCoreApplication.translate("MainWindow", u"Numero de Serie:", None))
        self.label_33.setText(QCoreApplication.translate("MainWindow", u"Falla reportada:", None))
        self.label_34.setText(QCoreApplication.translate("MainWindow", u"Informaci\u00f3n adicional:", None))
        self.label_27.setText(QCoreApplication.translate("MainWindow", u"Estatus:", None))
        self.label_35.setText(QCoreApplication.translate("MainWindow", u"Accesorios:", None))
        self.cableac.setText(QCoreApplication.translate("MainWindow", u"Cable ac", None))
        self.controlr.setText(QCoreApplication.translate("MainWindow", u"Control remoto", None))
        self.eliminador.setText(QCoreApplication.translate("MainWindow", u"Eliminador", None))
        self.base.setText(QCoreApplication.translate("MainWindow", u"Base", None))
        self.basepared.setText(QCoreApplication.translate("MainWindow", u"Base de pared", None))
        self.pilas.setText(QCoreApplication.translate("MainWindow", u"Pilas", None))
        self.cables.setText(QCoreApplication.translate("MainWindow", u"Cables", None))
        self.groupBox.setTitle(QCoreApplication.translate("MainWindow", u"Informaci\u00f3n del cliente", None))
        self.rnombre.setPlaceholderText(QCoreApplication.translate("MainWindow", u"--Seleccione un cliente--", None))
        self.label_47.setText("")
        self.label_46.setText(QCoreApplication.translate("MainWindow", u"RFC:", None))
        self.label_45.setText(QCoreApplication.translate("MainWindow", u"e-mail:", None))
        self.label_44.setText(QCoreApplication.translate("MainWindow", u"Direcci\u00f3n:", None))
        self.label_43.setText(QCoreApplication.translate("MainWindow", u"Telefono:", None))
        self.label_42.setText(QCoreApplication.translate("MainWindow", u"Nombre:", None))
        self.rbtneditaclient.setText(QCoreApplication.translate("MainWindow", u"Editar cliente", None))
        self.btnnuevocliente.setText(QCoreApplication.translate("MainWindow", u"Nuevo cliente", None))
        self.btninicior.setText(QCoreApplication.translate("MainWindow", u"Inicio", None))
        self.btnant.setText(QCoreApplication.translate("MainWindow", u"Anterior", None))
        self.btnsig.setText(QCoreApplication.translate("MainWindow", u"Siguiente", None))
        self.btnfin.setText(QCoreApplication.translate("MainWindow", u"Fin", None))
        self.btnnuevo.setText(QCoreApplication.translate("MainWindow", u"Nuevo", None))
        self.btneliminar.setText(QCoreApplication.translate("MainWindow", u"Eliminar", None))
        self.btnguardar.setText(QCoreApplication.translate("MainWindow", u"Guardar", None))
        self.tabregistros.setTabText(self.tabregistros.indexOf(self.tab_3), QCoreApplication.translate("MainWindow", u"Registro", None))
        self.msjreg.setText(QCoreApplication.translate("MainWindow", u"Todos los registros:", None))
        self.buscar.setText(QCoreApplication.translate("MainWindow", u"...", None))
        self.buscarreg.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Buscar en todos los registros", None))
        self.tabregistros.setTabText(self.tabregistros.indexOf(self.tab_4), QCoreApplication.translate("MainWindow", u"Lista de registros", None))
        self.groupBox_11.setTitle(QCoreApplication.translate("MainWindow", u"Informacion del equipo:", None))
        self.label_111.setText(QCoreApplication.translate("MainWindow", u"Equipo:", None))
        self.label_109.setText(QCoreApplication.translate("MainWindow", u"Marca:", None))
        self.label_112.setText(QCoreApplication.translate("MainWindow", u"Modelo:", None))
        self.label_108.setText(QCoreApplication.translate("MainWindow", u"Numero de Serie:", None))
        self.groupBox_13.setTitle(QCoreApplication.translate("MainWindow", u"Informaci\u00f3n del cliente", None))
        self.label_121.setText(QCoreApplication.translate("MainWindow", u"Nombre:", None))
        self.label_117.setText(QCoreApplication.translate("MainWindow", u"RFC:", None))
        self.label_118.setText(QCoreApplication.translate("MainWindow", u"e-mail:", None))
        self.label_119.setText(QCoreApplication.translate("MainWindow", u"Direcci\u00f3n:", None))
        self.label_116.setText("")
        self.label_120.setText(QCoreApplication.translate("MainWindow", u"Telefono:", None))
        self.groupBox_9.setTitle(QCoreApplication.translate("MainWindow", u"Registro", None))
        self.label_102.setText(QCoreApplication.translate("MainWindow", u"Registro:", None))
        self.rep_2.setText(QCoreApplication.translate("MainWindow", u"--", None))
        self.label_103.setText(QCoreApplication.translate("MainWindow", u"de", None))
        self.rde_2.setText(QCoreApplication.translate("MainWindow", u"--", None))
        self.repant_2.setText("")
        self.repsig_2.setText("")
        self.groupBox_12.setTitle(QCoreApplication.translate("MainWindow", u"Reparaci\u00f3n", None))
        self.label_100.setText(QCoreApplication.translate("MainWindow", u"Tecnico:", None))
        self.groupBox_10.setTitle(QCoreApplication.translate("MainWindow", u"Repuestos:", None))
        self.label_97.setText(QCoreApplication.translate("MainWindow", u"   Total:", None))
        ___qtablewidgetitem = self.repuestos_2.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("MainWindow", u"Repuesto:", None))
        ___qtablewidgetitem1 = self.repuestos_2.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("MainWindow", u"Precio:", None))
        ___qtablewidgetitem2 = self.repuestos_2.verticalHeaderItem(0)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("MainWindow", u"1.", None))

        __sortingEnabled = self.repuestos_2.isSortingEnabled()
        self.repuestos_2.setSortingEnabled(False)
        ___qtablewidgetitem3 = self.repuestos_2.item(0, 0)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("MainWindow", u"pendiente", None))
        ___qtablewidgetitem4 = self.repuestos_2.item(0, 1)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("MainWindow", u"$0", None))
        self.repuestos_2.setSortingEnabled(__sortingEnabled)

        self.anadir_2.setText(QCoreApplication.translate("MainWindow", u" A\u00f1adir ", None))
        self.btneliminarep_2.setText(QCoreApplication.translate("MainWindow", u"Eliminar", None))
        self.label_98.setText(QCoreApplication.translate("MainWindow", u"$", None))
        self.totalrep_2.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.label_99.setText(QCoreApplication.translate("MainWindow", u"Costo Total:         $", None))
        self.tecnico_2.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Selecciona un tecnico", None))
        self.label_101.setText(QCoreApplication.translate("MainWindow", u"Servicio Tecnico:  $", None))
        self.label_104.setText("")
        self.label_105.setText(QCoreApplication.translate("MainWindow", u"Fecha de termino de la garantia:", None))
#if QT_CONFIG(tooltip)
        self.garantia_2.setToolTip(QCoreApplication.translate("MainWindow", u"Dias", None))
#endif // QT_CONFIG(tooltip)
        self.label_106.setText(QCoreApplication.translate("MainWindow", u"Fecha de reparacion:", None))
        self.fecha_rep_2.setPlaceholderText(QCoreApplication.translate("MainWindow", u"--Seleccione una fecha--", None))
        self.fecharep_2.setSpecialValueText(QCoreApplication.translate("MainWindow", u"--Seleccione la fecha de reparaci\u00f3n--", None))
        self.label_107.setText(QCoreApplication.translate("MainWindow", u"Garantia:", None))
        self.presupuesto_2.setText(QCoreApplication.translate("MainWindow", u"Presupuesto aceptado", None))
        self.label_96.setText(QCoreApplication.translate("MainWindow", u"Diagnostico:", None))
        self.label_113.setText(QCoreApplication.translate("MainWindow", u"Falla reportada:", None))
        self.cableac_2.setText(QCoreApplication.translate("MainWindow", u"Cable ac", None))
        self.controlr_2.setText(QCoreApplication.translate("MainWindow", u"Control remoto", None))
        self.eliminador_2.setText(QCoreApplication.translate("MainWindow", u"Eliminador", None))
        self.base_2.setText(QCoreApplication.translate("MainWindow", u"Base", None))
        self.basepared_2.setText(QCoreApplication.translate("MainWindow", u"Base de pared", None))
        self.pilas_2.setText(QCoreApplication.translate("MainWindow", u"Pilas", None))
        self.cables_2.setText(QCoreApplication.translate("MainWindow", u"Cables", None))
        self.label_115.setText(QCoreApplication.translate("MainWindow", u"Accesorios:", None))
        self.label_114.setText(QCoreApplication.translate("MainWindow", u"Estatus:", None))
        self.label_110.setText(QCoreApplication.translate("MainWindow", u"Informaci\u00f3n adicional:", None))
        self.label_60.setText(QCoreApplication.translate("MainWindow", u"Fecha de recepci\u00f3n: ", None))
        self.fecha_2.setText(QCoreApplication.translate("MainWindow", u"--", None))
        self.label_122.setText(QCoreApplication.translate("MainWindow", u"Fecha de entrega:", None))
        self.pagppend_2.setText(QCoreApplication.translate("MainWindow", u"Pago Pendiente", None))
        self.porcentaje_2.setText(QCoreApplication.translate("MainWindow", u"--", None))
        self.label_123.setText(QCoreApplication.translate("MainWindow", u"%", None))
        self.btneditaporce_2.setText(QCoreApplication.translate("MainWindow", u"cambiar", None))
        self.btnguardare_2.setText(QCoreApplication.translate("MainWindow", u"Guardar", None))
        self.fechaent.setPlaceholderText(QCoreApplication.translate("MainWindow", u"--Seleccione una fecha--", None))
        self.label_124.setText(QCoreApplication.translate("MainWindow", u"Porcentaje del tecnico:", None))
        self.fechaentrega_2.setSpecialValueText(QCoreApplication.translate("MainWindow", u"--Seleccione la fecha de reparaci\u00f3n--", None))
        self.tabregistros.setTabText(self.tabregistros.indexOf(self.tab_10), QCoreApplication.translate("MainWindow", u"Informaci\u00f3n", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"Equipos disponibles para revisi\u00f3n:", None))
        self.filtrar.setText(QCoreApplication.translate("MainWindow", u"Filtrar", None))
        self.btneditafiltro.setText(QCoreApplication.translate("MainWindow", u"cambiar", None))
#if QT_CONFIG(tooltip)
        self.checkmostocult.setToolTip(QCoreApplication.translate("MainWindow", u"Mostrar Ocultos", None))
#endif // QT_CONFIG(tooltip)
        self.checkmostocult.setText("")
        self.tabrepara.setTabText(self.tabrepara.indexOf(self.tab), QCoreApplication.translate("MainWindow", u"Revisiones", None))
        self.label_57.setText(QCoreApplication.translate("MainWindow", u"Equipos disponibles para reparaci\u00f3n:", None))
        self.filtrar_2.setText(QCoreApplication.translate("MainWindow", u"Filtrar", None))
        self.btneditafiltro_2.setText(QCoreApplication.translate("MainWindow", u"cambiar", None))
#if QT_CONFIG(tooltip)
        self.checkmostocult_2.setToolTip(QCoreApplication.translate("MainWindow", u"Mostrar Ocultos", None))
#endif // QT_CONFIG(tooltip)
        self.checkmostocult_2.setText("")
        self.tabrepara.setTabText(self.tabrepara.indexOf(self.tab_2), QCoreApplication.translate("MainWindow", u"Reparaciones", None))
        self.groupBox_4.setTitle(QCoreApplication.translate("MainWindow", u"Informacion del equipo:", None))
        self.label_80.setText(QCoreApplication.translate("MainWindow", u"Numero de Serie:", None))
        self.label_79.setText(QCoreApplication.translate("MainWindow", u"Marca:", None))
        self.label_76.setText(QCoreApplication.translate("MainWindow", u"Informaci\u00f3n adicional:", None))
        self.label_77.setText(QCoreApplication.translate("MainWindow", u"Equipo:", None))
        self.label_78.setText(QCoreApplication.translate("MainWindow", u"Modelo:", None))
        self.label_75.setText(QCoreApplication.translate("MainWindow", u"Falla reportada:", None))
        self.groupBox_2.setTitle(QCoreApplication.translate("MainWindow", u"Informacion de la reparaci\u00f3n", None))
        self.label_37.setText(QCoreApplication.translate("MainWindow", u"Diagnostico:", None))
        self.groupBox_3.setTitle(QCoreApplication.translate("MainWindow", u"Repuestos:", None))
        self.totalrep.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.label_56.setText(QCoreApplication.translate("MainWindow", u"   Total:", None))
        ___qtablewidgetitem5 = self.repuestos.horizontalHeaderItem(0)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("MainWindow", u"Repuesto:", None))
        ___qtablewidgetitem6 = self.repuestos.horizontalHeaderItem(1)
        ___qtablewidgetitem6.setText(QCoreApplication.translate("MainWindow", u"Precio:", None))
        ___qtablewidgetitem7 = self.repuestos.verticalHeaderItem(0)
        ___qtablewidgetitem7.setText(QCoreApplication.translate("MainWindow", u"1.", None))

        __sortingEnabled1 = self.repuestos.isSortingEnabled()
        self.repuestos.setSortingEnabled(False)
        ___qtablewidgetitem8 = self.repuestos.item(0, 0)
        ___qtablewidgetitem8.setText(QCoreApplication.translate("MainWindow", u"pendiente", None))
        ___qtablewidgetitem9 = self.repuestos.item(0, 1)
        ___qtablewidgetitem9.setText(QCoreApplication.translate("MainWindow", u"$0", None))
        self.repuestos.setSortingEnabled(__sortingEnabled1)

        self.anadir.setText(QCoreApplication.translate("MainWindow", u" A\u00f1adir ", None))
        self.btneliminarep.setText(QCoreApplication.translate("MainWindow", u"Eliminar", None))
        self.label_58.setText(QCoreApplication.translate("MainWindow", u"$", None))
        self.label_39.setText(QCoreApplication.translate("MainWindow", u"Costo Total:         $", None))
        self.label_41.setText(QCoreApplication.translate("MainWindow", u"Tecnico:", None))
        self.label_55.setText(QCoreApplication.translate("MainWindow", u"Servicio Tecnico:  $", None))
        self.tecnico.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Selecciona un tecnico", None))
        self.label_81.setText("")
        self.fecha_rep.setPlaceholderText(QCoreApplication.translate("MainWindow", u"--Seleccione una fecha--", None))
        self.label_83.setText(QCoreApplication.translate("MainWindow", u"Garantia:", None))
        self.label_84.setText(QCoreApplication.translate("MainWindow", u"Fecha de termino de la garantia:", None))
        self.fecharep.setSpecialValueText(QCoreApplication.translate("MainWindow", u"--Seleccione la fecha de reparaci\u00f3n--", None))
#if QT_CONFIG(tooltip)
        self.garantia.setToolTip(QCoreApplication.translate("MainWindow", u"Dias", None))
#endif // QT_CONFIG(tooltip)
        self.label_82.setText(QCoreApplication.translate("MainWindow", u"Fecha de reparacion:", None))
        self.hoy.setText(QCoreApplication.translate("MainWindow", u"hoy", None))
        self.btnconfirmar.setText(QCoreApplication.translate("MainWindow", u"confirmar revisi\u00f3n", None))
        self.btnentsinrep.setText(QCoreApplication.translate("MainWindow", u"Entregar sin reparar", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"Equipos disponibles para entrega:", None))
        self.entregas.setTabText(self.entregas.indexOf(self.tab_5), QCoreApplication.translate("MainWindow", u"Lista", None))
        self.btnimprimir_e.setText(QCoreApplication.translate("MainWindow", u"Imprimir", None))
        self.groupBox_5.setTitle(QCoreApplication.translate("MainWindow", u"Informacion de la reparaci\u00f3n", None))
        self.label_62.setText(QCoreApplication.translate("MainWindow", u"Diagnostico:", None))
        self.groupBox_6.setTitle(QCoreApplication.translate("MainWindow", u"Repuestos:", None))
        self.totalrepe.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.label_66.setText(QCoreApplication.translate("MainWindow", u"   Total:", None))
        ___qtablewidgetitem10 = self.repuestose.horizontalHeaderItem(0)
        ___qtablewidgetitem10.setText(QCoreApplication.translate("MainWindow", u"Repuesto:", None))
        ___qtablewidgetitem11 = self.repuestose.horizontalHeaderItem(1)
        ___qtablewidgetitem11.setText(QCoreApplication.translate("MainWindow", u"Precio:", None))
        ___qtablewidgetitem12 = self.repuestose.verticalHeaderItem(0)
        ___qtablewidgetitem12.setText(QCoreApplication.translate("MainWindow", u"1.", None))

        __sortingEnabled2 = self.repuestose.isSortingEnabled()
        self.repuestose.setSortingEnabled(False)
        ___qtablewidgetitem13 = self.repuestose.item(0, 0)
        ___qtablewidgetitem13.setText(QCoreApplication.translate("MainWindow", u"pendiente", None))
        ___qtablewidgetitem14 = self.repuestose.item(0, 1)
        ___qtablewidgetitem14.setText(QCoreApplication.translate("MainWindow", u"$0", None))
        self.repuestose.setSortingEnabled(__sortingEnabled2)

        self.anadire.setText(QCoreApplication.translate("MainWindow", u" A\u00f1adir ", None))
        self.btneliminarepe.setText(QCoreApplication.translate("MainWindow", u"Eliminar", None))
        self.label_67.setText(QCoreApplication.translate("MainWindow", u"$", None))
        self.label_64.setText(QCoreApplication.translate("MainWindow", u"Tecnico:", None))
        self.label_65.setText(QCoreApplication.translate("MainWindow", u"Servicio Tecnico:  $", None))
        self.label_63.setText(QCoreApplication.translate("MainWindow", u"Costo Total:         $", None))
        self.label_85.setText("")
        self.fecha_repe.setPlaceholderText(QCoreApplication.translate("MainWindow", u"--Seleccione una fecha--", None))
        self.label_87.setText(QCoreApplication.translate("MainWindow", u"Fecha de reparacion:", None))
        self.label_86.setText(QCoreApplication.translate("MainWindow", u"Fecha de termino de la garantia:", None))
        self.fecharepe.setSpecialValueText(QCoreApplication.translate("MainWindow", u"--Seleccione la fecha de reparaci\u00f3n--", None))
        self.label_88.setText(QCoreApplication.translate("MainWindow", u"Garantia:", None))
#if QT_CONFIG(tooltip)
        self.garantiae.setToolTip(QCoreApplication.translate("MainWindow", u"Dias", None))
#endif // QT_CONFIG(tooltip)
        self.tecnicoe.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Selecciona un tecnico", None))
        self.label_70.setText(QCoreApplication.translate("MainWindow", u"Porcentaje del tecnico:", None))
        self.pagppend.setText(QCoreApplication.translate("MainWindow", u"Pago Pendiente", None))
        self.btnguardare.setText(QCoreApplication.translate("MainWindow", u"Guardar", None))
        self.porcentaje.setText(QCoreApplication.translate("MainWindow", u"--", None))
        self.label_72.setText(QCoreApplication.translate("MainWindow", u"%", None))
        self.btneditaporce.setText(QCoreApplication.translate("MainWindow", u"cambiar", None))
        self.label_89.setText(QCoreApplication.translate("MainWindow", u"Fecha de entrega:", None))
        self.entregas.setTabText(self.entregas.indexOf(self.tab_6), QCoreApplication.translate("MainWindow", u"Entregar", None))
        self.toolButton.setText(QCoreApplication.translate("MainWindow", u"...", None))
        self.buscarcliente.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Buscar Cliente", None))
        self.label_31.setText(QCoreApplication.translate("MainWindow", u"Equipos del cliente:", None))
        self.label_6.setText("")
        self.label_54.setText(QCoreApplication.translate("MainWindow", u"Id Cliente:", None))
        self.label_50.setText(QCoreApplication.translate("MainWindow", u"Nombre:", None))
        self.label_52.setText(QCoreApplication.translate("MainWindow", u"Telefono:", None))
        self.telefono.setInputMask("")
        self.label_49.setText(QCoreApplication.translate("MainWindow", u"e-mail:", None))
        self.label_51.setText(QCoreApplication.translate("MainWindow", u"RFC:", None))
        self.label_53.setText(QCoreApplication.translate("MainWindow", u"Direcci\u00f3n:", None))
        self.btnnuevoclient.setText(QCoreApplication.translate("MainWindow", u"Nuevo", None))
        self.btneditaclient.setText(QCoreApplication.translate("MainWindow", u"Editar", None))
        self.btnguardaclient.setText(QCoreApplication.translate("MainWindow", u"Guardar", None))
        self.label_90.setText(QCoreApplication.translate("MainWindow", u"Fecha del:", None))
        self.fechape_1.setSpecialValueText(QCoreApplication.translate("MainWindow", u"--Seleccione la fecha de reparaci\u00f3n--", None))
        self.label_91.setText(QCoreApplication.translate("MainWindow", u"al", None))
        self.fechap_1.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Seleccione una fecha", None))
        self.fechap_2.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Seleccione una fecha", None))
        self.fechape_2.setSpecialValueText(QCoreApplication.translate("MainWindow", u"--Seleccione la fecha de reparaci\u00f3n--", None))
#if QT_CONFIG(tooltip)
        self.btnlimpiar.setToolTip(QCoreApplication.translate("MainWindow", u"limpiar", None))
#endif // QT_CONFIG(tooltip)
        self.btnlimpiar.setText("")
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"Tecnico:", None))
        self.tecnico_p.setCurrentText("")
        self.tecnico_p.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Seleccione un tecnico", None))
        self.toolButton_6.setText(QCoreApplication.translate("MainWindow", u"...", None))
        self.buscarp.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Buscar en la lista", None))
        self.seleccp.setText(QCoreApplication.translate("MainWindow", u"Seleccionar todo", None))
        self.label_125.setText(QCoreApplication.translate("MainWindow", u"Sueldo Mensual Promedio:", None))
        self.labely.setText("")
        self.btncambiografica.setText("")
        self.labelPromedio.setText("")
        self.btnautorizap.setText(QCoreApplication.translate("MainWindow", u"Autorizar pago", None))
        self.label_61.setText(QCoreApplication.translate("MainWindow", u"$", None))
        self.total_p.setText(QCoreApplication.translate("MainWindow", u"0", None))

        __sortingEnabled3 = self.listWidget.isSortingEnabled()
        self.listWidget.setSortingEnabled(False)
        ___qlistwidgetitem = self.listWidget.item(0)
        ___qlistwidgetitem.setText(QCoreApplication.translate("MainWindow", u"Almacenamiento", None))
        ___qlistwidgetitem1 = self.listWidget.item(1)
        ___qlistwidgetitem1.setText(QCoreApplication.translate("MainWindow", u"Empresa", None))
        ___qlistwidgetitem2 = self.listWidget.item(2)
        ___qlistwidgetitem2.setText(QCoreApplication.translate("MainWindow", u"Usuarios", None))
        ___qlistwidgetitem3 = self.listWidget.item(3)
        ___qlistwidgetitem3.setText(QCoreApplication.translate("MainWindow", u"Acerca de", None))
        self.listWidget.setSortingEnabled(__sortingEnabled3)

        self.groupBox_16.setTitle(QCoreApplication.translate("MainWindow", u"En la Nuve", None))
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"Activar", None))
#if QT_CONFIG(tooltip)
        self.radioButton.setToolTip(QCoreApplication.translate("MainWindow", u"Esta opcion guarda en la nuve todos los registros que que actualmente estan almacenados de manera local", None))
#endif // QT_CONFIG(tooltip)
        self.radioButton.setText(QCoreApplication.translate("MainWindow", u"Base de datos nueva", None))
#if QT_CONFIG(tooltip)
        self.radioButton_2.setToolTip(QCoreApplication.translate("MainWindow", u"Esta opci\u00f3n solo lee todo lo que esta en la nuve ", None))
#endif // QT_CONFIG(tooltip)
        self.radioButton_2.setText(QCoreApplication.translate("MainWindow", u"Base de datos con informaci\u00f3n", None))
        self.label_12.setText(QCoreApplication.translate("MainWindow", u"Turso-Database", None))
        self.label_15.setText(QCoreApplication.translate("MainWindow", u"Database name (url):", None))
        self.label_18.setText(QCoreApplication.translate("MainWindow", u"Token:", None))
        self.groupBox_17.setTitle(QCoreApplication.translate("MainWindow", u"Importar Informaci\u00f3n", None))
        self.cprep.setText(QCoreApplication.translate("MainWindow", u"CPReparaciones", None))
        self.label_21.setText(QCoreApplication.translate("MainWindow", u"Desde:", None))
        self.label_92.setText(QCoreApplication.translate("MainWindow", u"Pagina Web:", None))
        self.label_69.setText(QCoreApplication.translate("MainWindow", u"Nombre de la Empresa:", None))
        self.label_71.setText(QCoreApplication.translate("MainWindow", u"Direcci\u00f3n:", None))
        self.label_93.setText(QCoreApplication.translate("MainWindow", u"E-mail:", None))
        self.label_73.setText(QCoreApplication.translate("MainWindow", u"Telefono 1:", None))
        self.btnguardainfo.setText(QCoreApplication.translate("MainWindow", u"Guardar", None))
        self.label_74.setText(QCoreApplication.translate("MainWindow", u"Telefono 2:", None))
        self.groupBox_8.setTitle(QCoreApplication.translate("MainWindow", u"Logo", None))
        self.logo.setText("")
        self.selarch.setText("")
        self.groupBox_7.setTitle(QCoreApplication.translate("MainWindow", u"Notas al pie de reporte", None))
        self.label_94.setText(QCoreApplication.translate("MainWindow", u"Entrada:", None))
        self.label_95.setText(QCoreApplication.translate("MainWindow", u"Salida:", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_7), QCoreApplication.translate("MainWindow", u"Informaci\u00f3n", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_8), QCoreApplication.translate("MainWindow", u"Horario", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_9), QCoreApplication.translate("MainWindow", u"Preferencias", None))
        self.label_68.setText(QCoreApplication.translate("MainWindow", u"Usuarios", None))
    # retranslateUi

