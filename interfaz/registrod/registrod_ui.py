# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'registrod.ui'
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
from PySide6.QtWidgets import (QApplication, QCheckBox, QComboBox, QDateEdit,
    QDialog, QLabel, QLineEdit, QPushButton,
    QSizePolicy, QWidget)
from recursos import recursos_rc

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(556, 582)
        icon = QIcon()
        icon.addFile(u":/iconos/iconos/Logo.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        Dialog.setWindowIcon(icon)
        Dialog.setStyleSheet(u"QPushButton {\n"
"	background-color: rgb(8, 42, 73);\n"
"	color: rgb(255,255,255);\n"
"	font: 700 12pt \"Segoe UI\";\n"
"}\n"
"QPushButton: hover {\n"
"	background-color: rgb(76, 110, 184)\n"
"}")
        self.mensaje = QLabel(Dialog)
        self.mensaje.setObjectName(u"mensaje")
        self.mensaje.setGeometry(QRect(180, 360, 211, 20))
        self.mensaje.setStyleSheet(u"color: rgb(255, 0, 0);")
        self.email = QLineEdit(Dialog)
        self.email.setObjectName(u"email")
        self.email.setGeometry(QRect(20, 310, 221, 31))
        self.email.setStyleSheet(u"font: 700 12pt \"Segoe UI\";")
        self.email.setEchoMode(QLineEdit.EchoMode.Normal)
        self.email.setDragEnabled(False)
        self.tipo = QComboBox(Dialog)
        self.tipo.addItem("")
        self.tipo.addItem("")
        self.tipo.addItem("")
        self.tipo.setObjectName(u"tipo")
        self.tipo.setGeometry(QRect(320, 230, 221, 31))
        font = QFont()
        font.setFamilies([u"Segoe UI"])
        font.setPointSize(12)
        font.setBold(False)
        font.setItalic(False)
        self.tipo.setFont(font)
        self.tipo.setStyleSheet(u"font: 400 12pt \"Segoe UI\";")
        self.usuario = QLineEdit(Dialog)
        self.usuario.setObjectName(u"usuario")
        self.usuario.setGeometry(QRect(20, 230, 221, 31))
        self.usuario.setStyleSheet(u"border-bottom-color: rgb(0, 0, 0);\n"
"font: 700 12pt \"Segoe UI\";")
        self.cont = QLineEdit(Dialog)
        self.cont.setObjectName(u"cont")
        self.cont.setGeometry(QRect(320, 270, 221, 31))
        self.cont.setStyleSheet(u"font: 700 12pt \"Segoe UI\";")
        self.cont.setEchoMode(QLineEdit.EchoMode.Password)
        self.cont.setDragEnabled(False)
        self.sexo = QComboBox(Dialog)
        self.sexo.addItem("")
        self.sexo.addItem("")
        self.sexo.addItem("")
        self.sexo.setObjectName(u"sexo")
        self.sexo.setGeometry(QRect(20, 270, 221, 31))
        self.sexo.setStyleSheet(u"font: 400 12pt \"Segoe UI\";")
        self.fechna = QDateEdit(Dialog)
        self.fechna.setObjectName(u"fechna")
        self.fechna.setGeometry(QRect(320, 190, 221, 31))
        self.fechna.setStyleSheet(u"font: 700 12pt \"Segoe UI\";")
        self.label_5 = QLabel(Dialog)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(210, 30, 141, 131))
        self.label_5.setStyleSheet(u"image: url(:/iconos/iconos/Logo.png);\n"
"border-radius: 20px;")
        self.label_5.setScaledContents(True)
        self.cont_2 = QLineEdit(Dialog)
        self.cont_2.setObjectName(u"cont_2")
        self.cont_2.setGeometry(QRect(320, 310, 221, 31))
        self.cont_2.setStyleSheet(u"font: 700 12pt \"Segoe UI\";")
        self.cont_2.setEchoMode(QLineEdit.EchoMode.Password)
        self.cont_2.setDragEnabled(False)
        self.btnregistrarse = QPushButton(Dialog)
        self.btnregistrarse.setObjectName(u"btnregistrarse")
        self.btnregistrarse.setGeometry(QRect(200, 420, 171, 31))
        self.btnregistrarse.setStyleSheet(u"background-color: rgb(8, 42, 72);\n"
"font: 700 12pt \"Segoe UI\";")
        self.checkvercont = QCheckBox(Dialog)
        self.checkvercont.setObjectName(u"checkvercont")
        self.checkvercont.setGeometry(QRect(230, 390, 111, 20))
        self.btncancelar = QPushButton(Dialog)
        self.btncancelar.setObjectName(u"btncancelar")
        self.btncancelar.setGeometry(QRect(240, 470, 81, 31))
        self.btncancelar.setStyleSheet(u"background-color: rgb(8, 42, 72);\n"
"font: 700 10pt \"Segoe UI\";")
        self.nombre = QLineEdit(Dialog)
        self.nombre.setObjectName(u"nombre")
        self.nombre.setGeometry(QRect(20, 190, 221, 31))
        self.nombre.setStyleSheet(u"border-bottom-color: rgb(0, 0, 0);\n"
"font: 700 12pt \"Segoe UI\";")

        self.retranslateUi(Dialog)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Credenciales", None))
        self.mensaje.setText(QCoreApplication.translate("Dialog", u"<html><head/><body><p align=\"center\"><span style=\" font-size:10pt;\"><br/></span></p></body></html>", None))
        self.email.setPlaceholderText(QCoreApplication.translate("Dialog", u"e-mail", None))
        self.tipo.setItemText(0, QCoreApplication.translate("Dialog", u"Tecnico", None))
        self.tipo.setItemText(1, QCoreApplication.translate("Dialog", u"Administrativo", None))
        self.tipo.setItemText(2, "")

        self.tipo.setPlaceholderText(QCoreApplication.translate("Dialog", u"seleccione el tipo de usuario", None))
        self.usuario.setText("")
        self.usuario.setPlaceholderText(QCoreApplication.translate("Dialog", u"Usuario", None))
        self.cont.setPlaceholderText(QCoreApplication.translate("Dialog", u"Contrase\u00f1a", None))
        self.sexo.setItemText(0, QCoreApplication.translate("Dialog", u"Hombre", None))
        self.sexo.setItemText(1, QCoreApplication.translate("Dialog", u"Mujer", None))
        self.sexo.setItemText(2, QCoreApplication.translate("Dialog", u"Otro", None))

        self.sexo.setPlaceholderText(QCoreApplication.translate("Dialog", u"Seleccione su sexo", None))
        self.label_5.setText("")
        self.cont_2.setPlaceholderText(QCoreApplication.translate("Dialog", u"Confirmar contrase\u00f1a", None))
        self.btnregistrarse.setText(QCoreApplication.translate("Dialog", u"Registrarse", None))
        self.checkvercont.setText(QCoreApplication.translate("Dialog", u"Ver contrase\u00f1a", None))
        self.btncancelar.setText(QCoreApplication.translate("Dialog", u"cancelar", None))
        self.nombre.setText("")
        self.nombre.setPlaceholderText(QCoreApplication.translate("Dialog", u"Nombre", None))
    # retranslateUi

