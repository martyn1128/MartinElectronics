import sys
from PySide6.QtWidgets import QApplication
from selector import Seleccion

if __name__ == '__main__':
    app = QApplication(sys.argv)
    selec = Seleccion()
    selec.inicio()
    sys.exit(app.exec())