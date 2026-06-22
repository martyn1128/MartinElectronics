from PySide6.QtWidgets import QDialog

from interfaz.edita_pocentaje.ui_edita_porcentaje import Ui_Dialog


class EditaPorcentaje(QDialog):

    def __init__(self, vprin):
        super().__init__(parent=vprin)
        self.vprin = vprin.ui
        self.edita = Ui_Dialog()
        self.edita.setupUi(self)
        self.edita.porcent.setValue(int(self.vprin.porcentaje_2.text()))
        self.edita.buttonBox.accepted.connect(self.aplica_porcentaje)

    def aplica_porcentaje(self):
        self.vprin.porcentaje_2.setText(str(self.edita.porcent.value()))