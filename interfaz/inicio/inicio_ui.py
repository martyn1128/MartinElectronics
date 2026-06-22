# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'inicio.ui'
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
    QMainWindow, QPushButton, QSizePolicy, QStatusBar,
    QWidget)
from recursos import recursos_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(574, 600)
        icon = QIcon()
        icon.addFile(u":/iconos/iconos/Logo.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setStyleSheet(u"QPushButton{\n"
"	background-color: rgba(7, 39, 67, 140);\n"
"	font: 700 10pt \"Segoe UI\";\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: rgb(76, 110, 184)\n"
"}")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.usuario = QLineEdit(self.centralwidget)
        self.usuario.setObjectName(u"usuario")
        self.usuario.setGeometry(QRect(200, 280, 191, 31))
        self.usuario.setCursor(QCursor(Qt.CursorShape.IBeamCursor))
        self.usuario.setStyleSheet(u"border-bottom-color: rgb(0, 0, 0);\n"
"font: 700 12pt \"Segoe UI\";")
        self.usuario.setCursorMoveStyle(Qt.CursorMoveStyle.VisualMoveStyle)
        self.cont = QLineEdit(self.centralwidget)
        self.cont.setObjectName(u"cont")
        self.cont.setGeometry(QRect(200, 350, 191, 31))
        self.cont.setStyleSheet(u"font: 700 12pt \"Segoe UI\";")
        self.cont.setEchoMode(QLineEdit.EchoMode.Password)
        self.cont.setDragEnabled(False)
        self.label_5 = QLabel(self.centralwidget)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(210, 80, 171, 161))
        self.label_5.setStyleSheet(u"image: url(:/iconos/iconos/Logo.png);\n"
"")
        self.label_5.setScaledContents(True)
        self.btniniciar = QPushButton(self.centralwidget)
        self.btniniciar.setObjectName(u"btniniciar")
        self.btniniciar.setGeometry(QRect(210, 460, 171, 31))
        self.btniniciar.setStyleSheet(u"")
        self.checkvercont = QCheckBox(self.centralwidget)
        self.checkvercont.setObjectName(u"checkvercont")
        self.checkvercont.setGeometry(QRect(240, 390, 121, 20))
        self.mensaje = QLabel(self.centralwidget)
        self.mensaje.setObjectName(u"mensaje")
        self.mensaje.setGeometry(QRect(170, 420, 241, 20))
        self.mensaje.setStyleSheet(u"color: rgb(255, 0, 0);")
        self.mensaje.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.btnregistrarse = QPushButton(self.centralwidget)
        self.btnregistrarse.setObjectName(u"btnregistrarse")
        self.btnregistrarse.setGeometry(QRect(480, 540, 81, 31))
        self.btnregistrarse.setStyleSheet(u"")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)
        QWidget.setTabOrder(self.usuario, self.cont)
        QWidget.setTabOrder(self.cont, self.checkvercont)
        QWidget.setTabOrder(self.checkvercont, self.btniniciar)
        QWidget.setTabOrder(self.btniniciar, self.btnregistrarse)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Martin Electronic's", None))
        self.usuario.setText("")
        self.usuario.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Usuario", None))
        self.cont.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Contrase\u00f1a", None))
        self.label_5.setText("")
        self.btniniciar.setText(QCoreApplication.translate("MainWindow", u"Iniciar seci\u00f3n", None))
        self.checkvercont.setText(QCoreApplication.translate("MainWindow", u"Ver contrase\u00f1a", None))
        self.mensaje.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:10pt;\"><br/></span></p></body></html>", None))
        self.btnregistrarse.setText(QCoreApplication.translate("MainWindow", u"Registrarse", None))
    # retranslateUi

