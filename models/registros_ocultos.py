import os, pickle

from PySide6.QtCore import QSortFilterProxyModel


class FiltroModel(QSortFilterProxyModel):
    def __init__(self, parent=None):
        super().__init__()
        self.vprin = parent
        arch_dir = os.path.join(os.getenv('APPDATA'), 'Martin Electronics/preferences')
        os.makedirs(arch_dir, exist_ok=True)
        self.archivo_path = os.path.join(os.getenv('APPDATA'),'Martin Electronics/preferences/registros_ocultos.lm')
        self.archivo = None
        self.cargar()

    def filterAcceptsRow(self, source_row, source_parent):
        # Obtenemos el ID de la primera columna (columna 0)
        index = self.sourceModel().index(source_row, 0, source_parent)
        id_dato = self.sourceModel().data(index)

        # Ocultar si el ID está en la lista
        return (id_dato not in self.archivo and not self.vprin.checkmostocult.isChecked()) or (self.vprin.checkmostocult.isChecked() or self.vprin.checkmostocult_2.isChecked())

    def esta_oculto(self, idr):
        if idr in self.archivo:
            return True
        else:
            return False

    def cargar(self):
        try:
            with open(self.archivo_path, "rb") as archivo:
                self.archivo = pickle.load(archivo)
        except FileNotFoundError:
            with open(self.archivo_path, "wb") as archivo:
                pickle.dump([], archivo)
            self.cargar()

    def agregar(self, idr):
        if idr in self.archivo:
            pass
        else:
            self.archivo.append(idr)
        with open(self.archivo_path, "wb") as archivo:
            pickle.dump(self.archivo, archivo)
        self.actualizar_ocultos()

    def borrar(self, idr):
        aux = []
        if idr in self.archivo:
            for i in self.archivo:
                if idr == i:
                    continue
                aux.append(i)
            self.archivo = aux
        else:
            pass
        with open(self.archivo_path, "wb") as archivo:
            pickle.dump(self.archivo, archivo)
        self.actualizar_ocultos()

    def actualizar_ocultos(self):
        with open(self.archivo_path, "rb+") as archivo:
            self.archivo = pickle.load(archivo)
        self.invalidateFilter()