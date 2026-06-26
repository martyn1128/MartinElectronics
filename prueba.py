from controllers.main_controller import MainController
import sys
from PySide6.QtWidgets import QApplication

if __name__ == '__main__':
    # En Windows es necesario asignar un AppUserModelID antes de crear ventanas para que el
    # icono personalizado se muestre en la barra de tareas (y usar preferiblemente un .ico).
    if sys.platform.startswith("win"):
        try:
            import ctypes
            ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID(u"martin.electronics.app")
        except Exception:
            pass

    app = QApplication(sys.argv)
    try:
        vent = MainController((None,"Prueba"))
        vent.resize(2000, 900)
        vent.showMaximized()
        sys.exit(app.exec())
    except Exception as e:
        print(f"Ocurrio un error inesperado: {e}")
        

