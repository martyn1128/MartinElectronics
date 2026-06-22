from controllers.main_controller import MainController
import sys
from PySide6.QtWidgets import QApplication

if __name__ == '__main__':
    app = QApplication(sys.argv)
    try:
        vent = MainController((None,"Prueba"))
        vent.resize(2000, 900)
        vent.showMaximized()
        sys.exit(app.exec())
    except Exception as e:
        print(f"Ocurrio un error inesperado: {e}")
        

