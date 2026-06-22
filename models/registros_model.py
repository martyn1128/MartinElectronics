# models/registro_model.py
from .db import DB

class RegistroModel:

    def query_todos(self):
        return '''
               SELECT r.id       AS registro_id, \
                      e.id, \
                      e.equipo, \
                      e.marca, \
                      e.modelo, \
                      e.serie, \
                      r.problema, \
                      r.info_adicional, \
                      r.estatus, \
                      r.accesorios, \
                      r.fecha_llegada, \
                      r.fecha_entrega, \
                      c.id AS "ID Cliente",
                      c.nombre   AS cliente_nombre, \
                      c.telefono AS cliente_telefono
               FROM registros r
                        LEFT JOIN equipos e ON r.equipo_id = e.id
                        LEFT JOIN clientes c ON c.id = e.cliente_id
               ORDER BY r.id \
               '''

    def numero(self):
        con = DB().connect()
        cur = con.cursor()
        cur.execute("SELECT COUNT(id) FROM registros")
        res = cur.fetchone()
        con.close()
        return res

    def ultimo(self):
        con = DB().connect()
        cur = con.cursor()
        cur.execute("SELECT id FROM registros ORDER BY id DESC LIMIT 1;")
        res = cur.fetchone()
        con.close()
        return res

    def obtener_todos(self):
        con = DB().connect()
        cur = con.cursor()

        cur.execute("""
                    SELECT r.id,
                           e.id,
                           e.cliente_id,
                           e.equipo,
                           e.marca,
                           e.modelo,
                           e.serie,
                           r.problema,
                           r.accesorios,
                           r.info_adicional,
                           r.estatus,
                           r.fecha_llegada,
                           u.nombre
                    FROM registros r
                    LEFT JOIN equipos e ON r.equipo_id = e.id
                    LEFT JOIN usuarios u ON r.usuario_id = u.id
                    ORDER BY r.id
                    """)

        res = cur.fetchall()
        con.close()
        return res

    def obtener_por_cliente(self, cid):
        con = DB().connect()
        cur = con.cursor()

        cur.execute("""
        SELECT 
            r.id,
            e.id,
            e.cliente_id,
            e.equipo,
            e.marca,
            e.modelo,
            e.serie,
            r.problema,
            r.accesorios,
            r.info_adicional,
            r.estatus,
            r.fecha_llegada,
            u.nombre
        FROM registros r
        LEFT JOIN equipos e ON r.equipo_id = e.id
        LEFT JOIN usuarios u ON r.usuario_id = u.id
        WHERE e.cliente_id = ?
        """, (cid,))

        res = cur.fetchall()
        con.close()
        return res

    def obtener_por_idr(self, idr):
        con = DB().connect()
        cur = con.cursor()

        cur.execute("""
        SELECT 
            r.id,
            e.id,
            e.cliente_id,
            e.equipo,
            e.marca,
            e.modelo,
            e.serie,
            r.problema,
            r.accesorios,
            r.info_adicional,
            r.estatus,
            r.fecha_llegada,
            u.nombre
        FROM registros r
        LEFT JOIN equipos e ON r.equipo_id = e.id
        LEFT JOIN usuarios u ON r.usuario_id = u.id
        WHERE r.id = ?
        """, (idr,))

        res = cur.fetchall()
        con.close()
        return res

    def obtener_todo_por_id(self, id):
        con = DB().connect()
        cur = con.cursor()

        cur.execute("""
                    SELECT *
                    FROM registros 
                    WHERE id = ?
                    """, (id,))
        res = cur.fetchone()
        con.close()
        return res

    def insertar(self, data):
        con = DB().connect()
        cur = con.cursor()

        cur.execute("""
                    INSERT INTO registros (equipo_id,
                                           usuario_id,
                                           problema,
                                           accesorios,
                                           info_adicional,
                                           estatus,
                                           fecha_llegada,
                                           fecha_entrega,
                                           usuario_id)
                    VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
                    """, data)
        idreg = cur.lastrowid
        cur.execute("""
                INSERT INTO reparaciones(registro_id)
                VALUES (?)
        """, (idreg,))
        con.commit()
        con.close()

    def actualizar(self, equipo_id, data):
        con = DB().connect()
        cur = con.cursor()

        cur.execute("""
                    UPDATE registros
                    SET problema       = ?,
                        accesorios     = ?,
                        info_adicional = ?,
                        estatus        = ?,
                        fecha_llegada  = ?,
                        usuario_id     = ?
                    WHERE equipo_id = ?
                    """, (*data, equipo_id))

        con.commit()
        con.close()

    def actualizar_estatus(self, reg_id=None, rep_id = None, estatus="", fe=""):
        con = DB().connect()
        cur = con.cursor()
        if rep_id:
            cur.execute("""
                        UPDATE registros
                        SET estatus = ?,
                            fecha_entrega = ?
                        WHERE id = (select registro_id 
                                      from reparaciones 
                                      where id = ?)
                        """, (estatus, fe, rep_id))
        else:
            cur.execute("""
                        UPDATE registros
                        SET estatus        = ?
                        WHERE id = ?
                        """, (estatus, reg_id))

        con.commit()
        con.close()

    def existe(self, equipo_id):
        con = DB().connect()
        cur = con.cursor()

        cur.execute("SELECT id FROM registros WHERE equipo_id = ?", (equipo_id,))
        res = cur.fetchone()

        con.close()
        return res is not None

    def obtener_todos_por_idequipo(self, id):
        con = DB().connect()
        cur = con.cursor()

        cur.execute("""
                    SELECT *
                    FROM registros r
                    JOIN equipos e ON r.equipo_id = e.id
                    WHERE e.id = ?
                    """, (id,))
        res = cur.fetchall()
        con.close()
        return res

    def obtener_todos_por_equipo(self, equipo_id):
        con = DB().connect()
        cur = con.cursor()

        cur.execute("""
                    SELECT r.id,
                           e.id,
                           e.cliente_id,
                           e.equipo,
                           e.marca,
                           e.modelo,
                           e.serie,
                           r.problema,
                           r.accesorios,
                           r.info_adicional,
                           r.estatus,
                           r.fecha_llegada,
                           u.nombre
                    FROM registros r
                             LEFT JOIN equipos e ON r.equipo_id = e.id
                             LEFT JOIN usuarios u ON r.usuario_id = u.id
                    WHERE e.id = ?
                    ORDER BY r.id DESC LIMIT 1
                    """, (equipo_id,))
        res = cur.fetchall()
        con.close()
        return res

    def eliminar(self, registro_id):
        con = DB().connect()
        cur = con.cursor()

        try:
            # 1. eliminar reparaciones relacionadas
            cur.execute("""
                        DELETE
                        FROM reparaciones
                        WHERE registro_id = ?
                        """, (registro_id,))

            # 2. eliminar registro
            cur.execute("""
                        DELETE
                        FROM registros
                        WHERE id = ?
                        """, (registro_id,))

            con.commit()

        except Exception as e:
            con.rollback()
            print("Error al eliminar:", e)

        finally:
            con.close()

    def entregas(self):
        con = DB().connect()
        cur = con.cursor()

        cur.execute("""
        SELECT 
        CASE 
            WHEN (
                julianday(substr(fecha_entrega, 7, 4) || '-' || substr(fecha_entrega, 4, 2) || '-' || substr(fecha_entrega, 1, 2)) - 
                julianday(substr(fecha_llegada, 7, 4) || '-' || substr(fecha_llegada, 4, 2) || '-' || substr(fecha_llegada, 1, 2))
            ) <= 5 THEN '1-5 Días'
            
            WHEN (
                julianday(substr(fecha_entrega, 7, 4) || '-' || substr(fecha_entrega, 4, 2) || '-' || substr(fecha_entrega, 1, 2)) - 
                julianday(substr(fecha_llegada, 7, 4) || '-' || substr(fecha_llegada, 4, 2) || '-' || substr(fecha_llegada, 1, 2))
            ) <= 10 THEN '5-10 Días'
            
            ELSE '+10 Días'
        END AS rango,
        COUNT(*) AS total
        FROM registros
        WHERE fecha_entrega IS NOT NULL 
          AND fecha_llegada IS NOT NULL
          -- Filtro para el año actual basado en el sistema
          --AND substr(fecha_llegada, 7, 4) = strftime('%Y', 'now') 
        GROUP BY rango
        ORDER BY rango DESC;
                    """)
        res = cur.fetchall()
        con.close()
        return res