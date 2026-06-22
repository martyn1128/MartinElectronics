import re

import pyodbc
import sqlite3


class MigradorAccess:

    def __init__(self, ruta_access, ruta_sqlite):
        self.ruta_access = ruta_access
        self.ruta_sqlite = ruta_sqlite
        self.tr = 0.0

    # =========================
    # AUXILIARES
    # =========================
    def bool_to_int(self, valor):
        return int(valor) if valor is not None else 0

    def safe_float(self, valor):
        return float(valor) if valor not in (None, "") else 0.0

    def safe_str(self, valor):
        return str(valor) if valor not in (None, "") else None

    def safe_nombre(self, valor):
        if valor and str(valor).strip():
            return str(valor)
        return f"Cliente sin nombre"

    def safe_repuestos(self, cadena):
        # Expresión regular para validar:
        # ^\$?      -> Opcionalmente inicia con $
        # \d+       -> Uno o más dígitos
        # (\.\d+)?  -> Opcionalmente un punto seguido de más dígitos
        # $         -> Fin de la cadena
        patron = r"^\$?\d+(\.\d+)?$"

        if re.match(patron, cadena):
            # Limpiamos el símbolo de pesos para el cálculo numérico
            valor_limpio = cadena.replace('$', '')

            # Convertimos a float y luego a string con un decimal para el formato '15.0'
            numero_formateado = str(float(valor_limpio))
            self.tr = float(valor_limpio)

            # Retornamos la estructura deseada

            return str([('pendiente', f'${valor_limpio}'), numero_formateado])
        self.tr = 0.0
        return str([('pendiente', f'$0'), '0.0'])

    # =========================
    # ESTATUS
    # =========================
    def obtener_estatus(self, data):
        if data["PReparar"] == 1 and data["PEntregar"] == 1:
            return "Pendiente de Revisión"
        elif data["PEntregar"] == 1:
            return "Pendiente de Entrega"
        elif data["PEntregar"] == 0:
            return "Completado"

    # =========================
    # MIGRACION
    # =========================
    def migrar_identificacion(self, callback_progreso=None):

        conn_access = pyodbc.connect(
            rf"DRIVER={{Microsoft Access Driver (*.mdb, *.accdb)}};"
            rf"DBQ={self.ruta_access};"
            rf"PWD=VB6CPRepair"
        )
        cur_access = conn_access.cursor()

        conn_sqlite = sqlite3.connect(self.ruta_sqlite)
        cur_sqlite = conn_sqlite.cursor()

        cur_access.execute("SELECT * FROM Identificacion")
        columnas = [col[0] for col in cur_access.description]

        total = 0
        clientes_nuevos = 0
        equipos_nuevos = 0
        cur_sqlite.execute("BEGIN TRANSACTION")
        for fila in cur_access.fetchall():
            data = dict(zip(columnas, fila))
            nombre = self.safe_nombre(data["Cliente"])
            try:
                # ===== CLIENTE =====
                cur_sqlite.execute(
                    "SELECT id FROM clientes WHERE nombre=? AND (telefono=? OR telefono is null)",
                    (nombre, data["Tel"])
                )
                existe = cur_sqlite.fetchone()

                if existe:
                    cliente_id = existe[0]
                else:
                    cur_sqlite.execute("""
                        INSERT INTO clientes (nombre, telefono, direccion, email)
                        VALUES (?, ?, ?, ?)
                    """, (
                        nombre,
                        self.safe_str(data["Tel"]),
                        self.safe_str(data["Domicilio"]),
                        self.safe_str(data["Email"])
                    ))
                    cliente_id = cur_sqlite.lastrowid
                    clientes_nuevos += 1

                # ===== EQUIPO =====
                cur_sqlite.execute("""
                    INSERT INTO equipos (cliente_id, equipo, marca, modelo, serie)
                    VALUES (?, ?, ?, ?, ?)
                """, (
                    cliente_id,
                    self.safe_str(data["Articulo"]),
                    self.safe_str(data["Marca"]),
                    self.safe_str(data["Modelo"]),
                    self.safe_str(data["NumSerie"])
                ))
                equipo_id = cur_sqlite.lastrowid
                equipos_nuevos += 1

                # ===== REGISTRO =====
                cur_sqlite.execute("""
                    INSERT INTO registros (
                        equipo_id, problema, info_adicional,
                        estatus, fecha_llegada, fecha_entrega
                    )
                    VALUES (?, ?, ?, ?, ?, ?)
                """, (
                    equipo_id,
                    self.safe_str(data["Problema"]),
                    self.safe_str(data["Notas"]),
                    self.obtener_estatus(data),
                    data["FRecepcion"].strftime("%d/%m/%Y %I:%M:%S %p") if data["FRecepcion"] else None,
                    data["FEntrega"].strftime("%d/%m/%Y %I:%M:%S %p") if data["FEntrega"] else None
                ))
                registro_id = cur_sqlite.lastrowid
                #====== TECNICO ========
                cur_sqlite.execute("""
                                   SELECT id FROM usuarios 
                                   WHERE nombre LIKE ?
                                  """, (f"%{data['Tecnico']}%" if data["Tecnico"] else "",))
                tecnico = cur_sqlite.fetchone()
                # ===== REPARACION =====
                repuestos = self.safe_repuestos(data["Repuestos"])
                servtec = float(data["Total"])-self.tr
                cur_sqlite.execute("""
                    INSERT INTO reparaciones (
                        registro_id, fecha_reparacion,
                        costo, diagnostico, repuestos,
                        garantia, ppagar, ptecnico, autorizada, 
                        comision, tecnico_id, servtec
                    )
                    VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
                """, (
                    registro_id,
                    data["FReparacion"].strftime("%d/%m/%Y %I:%M:%S %p") if data["FReparacion"] else None,
                    self.safe_float(data["Total"]),
                    self.safe_str(data["Diagnostico"]),
                    repuestos,
                    self.safe_str(30),
                    self.bool_to_int(data["PPagar"]),
                    self.bool_to_int(data["POtro"]),
                    0,
                    50,
                    tecnico[0] if tecnico else None,
                    servtec
                ))

                total += 1

                if callback_progreso:
                    callback_progreso(total)

            except Exception as e:
                print("❌ Error:", data.get("NumBoleta"), e)

        print(conn_sqlite)
        print(":)")
        print(total, clientes_nuevos,equipos_nuevos)
        conn_sqlite.commit()
        print("guardado")
        conn_access.close()
        conn_sqlite.close()

        return total, clientes_nuevos, equipos_nuevos