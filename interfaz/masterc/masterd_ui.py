# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'masterd.ui'
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
from PySide6.QtWidgets import (QApplication, QCheckBox, QDialog, QLabel,
    QLineEdit, QPushButton, QSizePolicy, QWidget)
from recursos import recursos_rc

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(422, 377)
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
        self.cont = QLineEdit(Dialog)
        self.cont.setObjectName(u"cont")
        self.cont.setGeometry(QRect(120, 180, 191, 31))
        self.cont.setStyleSheet(u"font: 700 12pt \"Segoe UI\";")
        self.cont.setEchoMode(QLineEdit.EchoMode.Password)
        self.cont.setDragEnabled(False)
        self.label_5 = QLabel(Dialog)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(170, 60, 81, 81))
        self.label_5.setStyleSheet(u"border-image:  url(:/iconos/iconos/Logo.png) 0 0 0 0 stretch stretch;\n"
"background-repeat: no-repeat;\n"
"background-position: center;\n"
"border-radius: 15px;")
        self.label_5.setScaledContents(True)
        self.mensaje = QLabel(Dialog)
        self.mensaje.setObjectName(u"mensaje")
        self.mensaje.setGeometry(QRect(110, 210, 211, 20))
        self.mensaje.setStyleSheet(u"color: rgb(255, 0, 0);")
        self.btnsig = QPushButton(Dialog)
        self.btnsig.setObjectName(u"btnsig")
        self.btnsig.setGeometry(QRect(130, 280, 171, 31))
        self.btnsig.setStyleSheet(u"background-color: rgb(8, 42, 72);\n"
"font: 700 12pt \"Segoe UI\";")
        self.checkvercont = QCheckBox(Dialog)
        self.checkvercont.setObjectName(u"checkvercont")
        self.checkvercont.setGeometry(QRect(160, 230, 101, 20))

        self.retranslateUi(Dialog)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Credenciales", None))
        self.cont.setPlaceholderText(QCoreApplication.translate("Dialog", u"Contrase\u00f1a", None))
        self.label_5.setText("")
        self.mensaje.setText(QCoreApplication.translate("Dialog", u"<html><head/><body><p align=\"center\"><span style=\" font-size:10pt;\"><br/></span></p></body></html>", None))
        self.btnsig.setText(QCoreApplication.translate("Dialog", u"siguiente", None))
        self.checkvercont.setText(QCoreApplication.translate("Dialog", u"Ver contrase\u00f1a", None))
    # retranslateUi

