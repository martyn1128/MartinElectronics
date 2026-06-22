from PySide6.QtWidgets import QLineEdit, QMessageBox, QMainWindow
from PySide6.QtGui import QIcon
from PySide6.QtCore import QTimer, Signal
from interfaz.creamaster.creamaster_ui import Ui_MainWindow
import sqlite3, bcrypt, os


class Uno(QMainWindow):
    cambio_vent = Signal()
    def __init__(self):
        super().__init__()
        self.sales = False
        self.creamaster = Ui_MainWindow()
        self.creamaster.setupUi(self)
        #self.creamaster.show()
        #boton
        self.creamaster.checkvercont.stateChanged.connect(self.ver_cont)
        self.creamaster.btnsig.clicked.connect(self.master)
        self.creamaster.btncerr.clicked.connect(self.cancelar)
        #self.app1.exec()

    def ver_cont(s):
        if s.creamaster.checkvercont.isChecked():
            s.creamaster.cont.setEchoMode(QLineEdit.EchoMode.Normal)
            s.creamaster.cont_2.setEchoMode(QLineEdit.EchoMode.Normal)
        else:
            s.creamaster.cont.setEchoMode(QLineEdit.EchoMode.Password)
            s.creamaster.cont_2.setEchoMode(QLineEdit.EchoMode.Password)

    def master(self):
        msk = self.creamaster.cont.text()
        if len(msk)>=8:
            ban = False
            for l in msk:
                ban = True if l in "0123456789" else False
                if ban:
                    break
            if ban:
                if msk == self.creamaster.cont_2.text():
                    self.mostrar_advertencia("RECUERDE ESTA CONTRASEÑA, la necesitara para registrar usuarios")
                    cifmsk = bcrypt.hashpw(msk.encode('utf-8'), bcrypt.gensalt())
                    self.crea_bd(cifmsk.decode("utf-8"))
                    self.creamaster.mensaje.setText("Contraseña establecida")
                    QMessageBox.information(self, "Éxito", "Contraseña establecida")
                    QTimer.singleShot(1000, lambda: self.cambio_vent.emit())  # Oculta después de 1 segundo
                else:
                    self.creamaster.mensaje.setText("    Las contraseñas no coinsiden")
                    self.creamaster.cont_2.setFocus()
            else:
                self.creamaster.mensaje.setText("   La contraseña debe tener numeros")
        else:
            self.creamaster.mensaje.setText("La contraseña debe tener almenos 8 digitos")

    def crea_bd(self, msk):
        db_dir = os.path.join(os.getenv('APPDATA'), 'Martin Electronics/data')
        db_path = os.path.join(os.getenv('APPDATA'), 'Martin Electronics/data/me.db')
        os.makedirs(db_dir, exist_ok = True)
        cnx = sqlite3.connect(db_path)
        cur = cnx.cursor()
        cur.executescript('''
        CREATE TABLE masterc(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            contraseña TEXT NOT NULL  
        );
        CREATE TABLE empresa(
            id INTEGER PRIMARY KEY,
            nombre TEXT,
            direccion TEXT,
            telefono1 TEXT,
            telefono2 TEXT,
            web TEXT,
            email TEXT,
            logo BLOB,
            nota1 TEXT,
            nota2 TEXT
        );
        CREATE TABLE usuarios(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nombre TEXT NOT NULL,
            user TEXT NOT NULL,
            sexo TEXT,
            email TEXT,
            fech_nac DATE,
            contraseña TEXT NOT NULL,
            tipo TEXT         
        );
        CREATE TABLE clientes(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nombre TEXT NOT NULL ,
            telefono TEXT,
            direccion TEXT,
            email TEXT,
            rfc TEXT 
        );
        CREATE TABLE equipos(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            cliente_id INTEGER,
            equipo TEXT,
            marca TEXT,
            modelo TEXT,
            serie TEXT,
            FOREIGN KEY (cliente_id) REFERENCES clientes(id)
        );
        CREATE TABLE registros(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            equipo_id INTEGER,
            usuario_id INTEGER,
            problema TEXT,
            accesorios TEXT,
            info_adicional TEXT,
            estatus TEXT,
            fecha_llegada DATETIME,
            fecha_entrega DATETIME,
            FOREIGN KEY (equipo_id) REFERENCES equipos(id),
            FOREIGN KEY (usuario_id) REFERENCES usuarios(id)
        );
        CREATE TABLE reparaciones(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            registro_id INTEGER,
            tecnico_id INTEGER,
            fecha_reparacion DATETIME,
            costo REAL,
            servtec REAL,
            diagnostico TEXT,
            repuestos TEXT,
            garantia TEXT,
            ppagar BOOLEAN,
            ptecnico BOOLEAN,
            comision INTEGER,
            autorizada BOOLEAN,
            FOREIGN KEY (registro_id) REFERENCES registros(id),
            FOREIGN KEY (tecnico_id) REFERENCES usuarios(id)
        );
        CREATE TABLE inventario(
            id INTEGER PRIMARY KEY ,
            nombre TEXT,
            descripcion TEXT,
            modelo TEXT,
            precio REAL,
            cantidad INTEGER
        )
        ''')
        cur.execute('INSERT INTO masterc (contraseña) VALUES (?)', (msk,))
        cnx.commit()
        cnx.close()

    def mostrar_advertencia(self, msj):
        msg = QMessageBox(self)
        msg.setIcon(QMessageBox.Icon.Warning)
        msg.setWindowTitle("Advertencia")
        msg.setText(msj)
        msg.exec()

    def cancelar(self):
        self.cambio_vent.emit()

    def ejecute(self):
        return self.sales