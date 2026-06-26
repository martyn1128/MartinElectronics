import sys
from PySide6.QtWidgets import QApplication
from selector import Seleccion

if __name__ == '__main__':
    if sys.platform.startswith("win"):
        try:
            import ctypes
            ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID(u"martin.electronics.app")
        except Exception:
            pass
    app = QApplication(sys.argv)
    selec = Seleccion()
    selec.inicio()
    sys.exit(app.exec())