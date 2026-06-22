# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'creamaster.ui'
##
## Created by: Qt User Interface Compiler version 6.10.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QCheckBox, QLabel, QLineEdit,
    QMainWindow, QMenuBar, QPushButton, QSizePolicy,
    QStatusBar, QWidget)
from recursos import recursos_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(432, 386)
        icon = QIcon()
        icon.addFile(u":/iconos/iconos/Logo.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setStyleSheet(u"QPushButton {\n"
"	background-color: rgb(8, 42, 73);\n"
"	color: rgb(255,255,255);\n"
"	font: 700 12pt \"Segoe UI\";\n"
"}\n"
"QPushButton: hover {\n"
"	background-color: rgb(76, 110, 184)\n"
"}")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.mensaje = QLabel(self.centralwidget)
        self.mensaje.setObjectName(u"mensaje")
        self.mensaje.setGeometry(QRect(120, 190, 211, 20))
        self.mensaje.setStyleSheet(u"color: rgb(255, 0, 0);")
        self.btnsig = QPushButton(self.centralwidget)
        self.btnsig.setObjectName(u"btnsig")
        self.btnsig.setGeometry(QRect(140, 240, 171, 31))
        self.btnsig.setStyleSheet(u"")
        self.cont = QLineEdit(self.centralwidget)
        self.cont.setObjectName(u"cont")
        self.cont.setGeometry(QRect(130, 100, 191, 31))
        self.cont.setStyleSheet(u"font: 700 12pt \"Segoe UI\";")
        self.cont.setEchoMode(QLineEdit.EchoMode.Password)
        self.cont.setDragEnabled(False)
        self.checkvercont = QCheckBox(self.centralwidget)
        self.checkvercont.setObjectName(u"checkvercont")
        self.checkvercont.setGeometry(QRect(170, 210, 121, 20))
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(90, 40, 271, 51))
        self.cont_2 = QLineEdit(self.centralwidget)
        self.cont_2.setObjectName(u"cont_2")
        self.cont_2.setGeometry(QRect(130, 150, 191, 31))
        self.cont_2.setStyleSheet(u"font: 700 12pt \"Segoe UI\";")
        self.cont_2.setEchoMode(QLineEdit.EchoMode.Password)
        self.cont_2.setDragEnabled(False)
        self.btncerr = QPushButton(self.centralwidget)
        self.btncerr.setObjectName(u"btncerr")
        self.btncerr.setGeometry(QRect(140, 280, 171, 31))
        self.btncerr.setStyleSheet(u"")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 432, 33))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)
        QWidget.setTabOrder(self.cont, self.cont_2)
        QWidget.setTabOrder(self.cont_2, self.checkvercont)
        QWidget.setTabOrder(self.checkvercont, self.btnsig)
        QWidget.setTabOrder(self.btnsig, self.btncerr)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Bienvenido a -Martin Electronic's-", None))
        self.mensaje.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:10pt;\"><br/></span></p></body></html>", None))
        self.btnsig.setText(QCoreApplication.translate("MainWindow", u"siguiente", None))
        self.cont.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Contrase\u00f1a", None))
        self.checkvercont.setText(QCoreApplication.translate("MainWindow", u"Ver contrase\u00f1a", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:12pt; font-weight:700;\">Establezca una contrase\u00f1a maestra</span></p></body></html>", None))
        self.cont_2.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Confirmar contrase\u00f1a", None))
        self.btncerr.setText(QCoreApplication.translate("MainWindow", u"Cerrar", None))
    # retranslateUi

