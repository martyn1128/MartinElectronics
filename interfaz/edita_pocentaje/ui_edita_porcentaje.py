# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'edita_porcentajexTiSob.ui'
##
## Created by: Qt User Interface Compiler version 6.9.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QMetaObject, QRect,
                            QSize, Qt)
from PySide6.QtGui import (QFont, QPixmap)
from PySide6.QtWidgets import (QDialogButtonBox,
                               QLabel, QSpinBox)


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(380, 160)
        Dialog.setMinimumSize(QSize(380, 160))
        Dialog.setMaximumSize(QSize(380, 160))
        self.buttonBox = QDialogButtonBox(Dialog)
        self.buttonBox.setObjectName(u"buttonBox")
        self.buttonBox.setGeometry(QRect(280, 70, 91, 191))
        self.buttonBox.setOrientation(Qt.Orientation.Vertical)
        self.buttonBox.setStandardButtons(QDialogButtonBox.StandardButton.Cancel|QDialogButtonBox.StandardButton.Ok)
        self.porcent = QSpinBox(Dialog)
        self.porcent.setObjectName(u"porcent")
        self.porcent.setGeometry(QRect(30, 120, 211, 31))
        font = QFont()
        font.setPointSize(12)
        self.porcent.setFont(font)
        self.label = QLabel(Dialog)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(30, 100, 221, 16))
        self.label.setFont(font)
        self.label_2 = QLabel(Dialog)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(90, 0, 101, 91))
        self.label_2.setPixmap(QPixmap(u":/iconos/iconos/estdistica.png"))
        self.label_2.setScaledContents(True)

        self.retranslateUi(Dialog)
        self.buttonBox.accepted.connect(Dialog.accept)
        self.buttonBox.rejected.connect(Dialog.reject)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Dialog", None))
        self.label.setText(QCoreApplication.translate("Dialog", u"Porcentaje para el Tecnico:", None))
        self.label_2.setText("")
    # retranslateUi

