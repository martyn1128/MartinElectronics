from PySide6.QtWidgets import QDialog

from interfaz.edita_pocentaje.ui_edita_porcentaje import Ui_Dialog


class EditaPorcentaje(QDialog):

    def __init__(self, vprin):
        super().__init__(parent=vprin)
        self.vprin = vprin.ui
        self.edita = Ui_Dialog()
        self.edita.setupUi(self)
        self.edita.porcent.blockSignals(True)
        self.edita.porcent.setValue(int(self.vprin.porcentaje.text()))
        self.edita.porcent.blockSignals(False)
        self.edita.porcent.valueChanged.connect(vprin.cambio_en_ent)
        self.edita.buttonBox.accepted.connect(self.aplica_porcentaje)

    def aplica_porcentaje(self):
        self.vprin.porcentaje.setText(str(self.edita.porcent.value()))