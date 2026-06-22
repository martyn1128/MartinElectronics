from .db import DB


class EquipoModel:

    def obtener_todos(self):
        con = DB().connect()
        cur = con.cursor()

        cur.execute("""
                    SELECT e.id, e.cliente_id, e.equipo, e.marca, e.modelo, e.serie
                    FROM equipos e
                    """)

        res = cur.fetchall()
        con.close()
        return res

    def obtener_por_serie(self, serie):
        con = DB().connect()
        cur = con.cursor()

        cur.execute("""
                    SELECT e.id, e.equipo, e.marca, e.modelo, e.serie, e.cliente_id
                    FROM equipos e
                    WHERE e.serie = ?
                    """, (serie,))

        res = cur.fetchone()
        self.id = res[0] if res else None
        self.equipo = res[1] if res else None
        self.marca = res[2] if res else None
        self.modelo = res[3] if res else None
        self.serie = res[4] if res else None
        self.clientid = res[5] if res else None
        con.close()
        return res

    def obtener_por_idc(self, idc):
        con = DB().connect()
        cur = con.cursor()

        cur.execute("""
                    SELECT e.id, e.equipo, e.marca, e.modelo, e.serie, r.estatus
                    FROM equipos e 
                        JOIN registros r ON e.id = r.equipo_id
                    WHERE e.cliente_id = ?
                    """, (idc,))

        res = cur.fetchall()
        con.close()
        return res

    def eliminar(self, id):
        con = DB().connect()
        cur = con.cursor()
        cur.execute("DELETE FROM equipos WHERE id = ?", (id,))
        con.commit()
        con.close()

    def insertar(self, data):
        con = DB().connect()
        cur = con.cursor()

        cur.execute("""
                    INSERT INTO equipos (cliente_id, equipo, marca, modelo, serie)
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
                    UPDATE equipos
                    SET cliente_id = ?,
                        equipo     = ?,
                        marca      = ?,
                        modelo     = ?,
                        serie      = ?
                    WHERE id = ?
                    """, (*data, id))

        con.commit()
        con.close()

    def equipos_en_taller(self):
        con = DB().connect()
        cur = con.cursor()
        cur.execute("""
                    SELECT COUNT(id) 
                    FROM registros
                    WHERE estatus != "Completado"
                    """)
        res = cur.fetchone()
        con.close()
        return res