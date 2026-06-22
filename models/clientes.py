# models/cliente_model.py
from .db import DB


class ClienteModel:
    def __init__(self):
        self.id = None
        self.nombre = None
        self.telefono = None
        self.direccion = None
        self.email = None
        self.rfc = None

    def numero(self):
        con = DB().connect()
        cur = con.cursor()
        cur.execute("SELECT COUNT(id) FROM clientes")
        res = cur.fetchone()
        con.close()
        return res

    def obtener_todos(self):
        con = DB().connect()
        cur = con.cursor()
        cur.execute("SELECT * FROM clientes")
        res = cur.fetchall()
        con.close()
        return res

    def obtener_por_id(self, id):
        con = DB().connect()
        cur = con.cursor()
        cur.execute("SELECT * FROM clientes WHERE id = ?", (id,))
        res = cur.fetchone()
        con.close()
        self.id = res[0] if res else None
        self.nombre = res[1] if res else None
        self.telefono = res[2] if res else None
        self.direccion = res[3] if res else None
        self.email = res[4] if res else None
        self.rfc = res[5] if res else None
        return res

    def insertar(self, data):
        con = DB().connect()
        cur = con.cursor()

        cur.execute("""
                    INSERT INTO clientes (nombre, telefono, direccion, email, rfc)
                    VALUES (?, ?, ?, ?, ?)
                    """, data)

        con.commit()
        new_id = cur.lastrowid
        con.close()
        return new_id

    def actualizar(self, id, data):
        con = DB().connect()
        cur = con.cursor()

        cur.execute("""
                    UPDATE clientes
                    SET nombre    = ?,
                        telefono  = ?,
                        direccion = ?,
                        email     = ?,
                        rfc       = ?
                    WHERE id = ?
                    """, (*data, id))

        con.commit()
        con.close()

    def eliminar(self, id):
        con = DB().connect()
        cur = con.cursor()

        cur.execute("DELETE FROM clientes WHERE id = ?", (id,))
        con.commit()
        con.close()

    def top_clientes(self):
        con = DB().connect()
        cur = con.cursor()
        cur.execute("""
                    SELECT c.id, c.nombre, COUNT(e.id) as total_equipos
                    FROM clientes c
                    JOIN equipos e ON c.id = e.cliente_id
                    GROUP BY c.id, c.nombre
                    ORDER BY total_equipos DESC 
                    LIMIT 5;
                    """)
        res = cur.fetchall()
        con.close()
        return res