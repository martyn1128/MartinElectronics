# models/reparacion_model.py

from .db import DB

class ReparacionModel:

    def query_recibe(self):
        return '''
               SELECT e.id AS "ID Equipo", \
                      e.equipo, \
                      e.marca, \
                      e.modelo, \
                      e.serie, \
                      r.problema, \
                      r.info_adicional, \
                      r.estatus, \
                      r.fecha_llegada AS "Fecha de ingreso", \
                      c.nombre        AS "Nombre del cliente",
                      rep.id AS "ID Reparación",
                      r.id AS "ID Registro",
                      rep.diagnostico
               FROM equipos e
                        JOIN registros r ON r.equipo_id = e.id
                        JOIN reparaciones rep ON r.id = rep.registro_id
                        LEFT JOIN clientes c ON c.id = e.cliente_id
               WHERE r.estatus = "Pendiente de Revisión" \
               '''

    def query_reparacion(self):
        return '''
               SELECT e.id, \
                      e.equipo, \
                      e.marca, \
                      e.modelo, \
                      e.serie, \
                      r.problema, \
                      rep.diagnostico AS "Diagnostico", \
                      r.estatus, \
                      r.fecha_llegada AS "Fecha de ingreso", \
                      c.nombre        AS "Nombre del cliente", \
                      rep.tecnico_id, \
                      u.nombre        AS "Nombre del tecnico",
                      rep.id AS "ID Reparacion",
                      r.id AS "ID Registro",
                      rep.servtec
               FROM equipos e
                        JOIN registros r ON r.equipo_id = e.id
                        LEFT JOIN reparaciones rep ON rep.registro_id = r.id
                        LEFT JOIN usuarios u ON u.id = rep.tecnico_id
                        LEFT JOIN clientes c ON c.id = e.cliente_id
               WHERE r.estatus = "Pendiente de Reparación" \
               '''

    def query_pconf(self):
        return '''
               SELECT e.id AS "ID Equipo", \
                      rep.costo AS "Total",
                      rep.diagnostico,
                      c.nombre  AS "Nombre del cliente",
                      c.telefono,
                      e.equipo, \
                      e.marca, \
                      e.modelo, \
                      e.serie, \
                      r.problema, \
                      r.estatus, \
                      r.fecha_llegada AS "Fecha de ingreso", \
                      r.id AS "ID Registro",
                      rep.id AS "ID Rep"
               FROM equipos e
                        JOIN registros r ON r.equipo_id = e.id
                        JOIN reparaciones rep ON r.id = rep.registro_id
                        JOIN clientes c ON c.id = e.cliente_id
               WHERE (rep.autorizada IS NULL OR rep.autorizada = 0) AND r.estatus = "Pendiente de Reparación"
               '''

    def obtener_entregas(self):
        con = DB().connect()
        cur = con.cursor()

        cur.execute("""
        SELECT 
            r.id,
            reg.id,
            e.equipo,
            e.marca,
            e.modelo,
            e.serie,
            c.nombre,
            c.telefono,
            r.costo
        FROM reparaciones r
        JOIN registros reg ON r.registro_id = reg.id
        JOIN equipos e ON reg.equipo_id = e.id
        JOIN clientes c ON e.cliente_id = c.id
        WHERE reg.estatus = "Pendiente de Entrega"
        """)

        res = cur.fetchall()
        con.close()
        return res

    def obtener_por_id(self, idrep):
        con = DB().connect()
        cur = con.cursor()

        cur.execute("""
                    SELECT rep.id,
                           t.nombre,
                           rep.costo,
                           rep.diagnostico,
                           rep.repuestos,
                           rep.fecha_reparacion,
                           rep.garantia,
                           t.id,
                           rep.servtec
                    FROM reparaciones rep
                    LEFT JOIN usuarios t ON rep.tecnico_id = t.id
                    WHERE rep.id = ?
                    """, (idrep,))
        res = cur.fetchall()
        con.close()
        return res

    def obtener_todo_por_idr(self, idr):
        con = DB().connect()
        cur = con.cursor()

        cur.execute("""
                    SELECT rep.*
                    FROM reparaciones rep
                             LEFT JOIN registros r ON rep.registro_id = r.id
                    WHERE r.id = ?
                    """, (idr,))
        res = cur.fetchone()
        con.close()
        return res

    def insertar(self, data):
        con = DB().connect()
        cur = con.cursor()

        cur.execute("""
                    INSERT INTO reparaciones (registro_id,
                                              tecnico_id,
                                              fecha_reparacion,
                                              costo,
                                              diagnostico,
                                              repuestos,
                                              garantia,
                                              ppagar,
                                              ptecnico,
                                              comision)
                    VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
                    """, data)

        con.commit()
        new_id = cur.lastrowid
        con.close()
        return new_id

    def actualizar(self, id, data):
        con = DB().connect()
        cur = con.cursor()
        cur.execute("""
                    UPDATE reparaciones
                    SET tecnico_id       = ?,
                        fecha_reparacion = ?,
                        costo            = ?,
                        diagnostico      = ?,
                        repuestos        = ?,
                        garantia         = ?,
                        ppagar           = ?,
                        ptecnico         = ?,
                        comision         = ?,
                        servtec          = ?
                    WHERE id = ?
                    """, (*data, id))

        con.commit()
        con.close()

    def obtener_por_reg(self, reg_id):
        con = DB().connect()
        cur = con.cursor()

        cur.execute("""
                    SELECT e.id,
                           e.cliente_id,
                           rep.costo,
                           rep.diagnostico,
                           rep.repuestos,
                           rep.fecha_reparacion,
                           rep.garantia,
                           rep.tecnico_id,
                           e.equipo,
                           e.marca,
                           e.modelo,
                           e.serie,
                           r.problema,
                           r.accesorios,
                           r.info_adicional,
                           r.fecha_entrega,
                           t.nombre,
                           (select nombre from usuarios where id = r.usuario_id)
                    FROM equipos e
                             LEFT JOIN registros r ON r.equipo_id = e.id
                             LEFT JOIN reparaciones rep ON rep.registro_id = r.id
                             LEFT JOIN usuarios t ON rep.tecnico_id = t.id
                    WHERE r.id = ?
                    """, (reg_id,))

        res = cur.fetchone()
        con.close()
        return res

    def pend_rep(self):
        con = DB().connect()
        cur = con.cursor()
        cur.execute("""
                    SELECT COUNT(id) 
                    FROM registros
                    WHERE estatus = "Pendiente de Reparación"
                    """)
        res = cur.fetchone()
        con.close()
        return res

    def pend_conf(self):
        con = DB().connect()
        cur = con.cursor()
        cur.execute("""
                    SELECT COUNT(r.id) From reparaciones r
                    LEFT JOIN registros reg ON registro_id = reg.id
                    WHERE (r.autorizada IS NULL OR r.autorizada != 1) AND reg.estatus = "Pendiente de Reparación"
                    """)
        res = cur.fetchone()
        con.close()
        return res

    def pend_rev(self):
        con = DB().connect()
        cur = con.cursor()
        cur.execute("""
                    SELECT COUNT(id)
                    FROM registros
                    WHERE estatus = "Pendiente de Revisión"
                    """)
        res = cur.fetchone()
        con.close()
        return res

    def autorizar(self, id):
        con = DB().connect()
        cur = con.cursor()
        cur.execute("""
                    UPDATE reparaciones
                    SET autorizada = ?
                    WHERE id = ?
                    """, (1, id))
        con.commit()
        con.close()

    def actualizar_ptecnico(self, id):
        con = DB().connect()
        cur = con.cursor()

        cur.execute("""
                    UPDATE reparaciones
                    SET ptecnico = 0
                    WHERE id = ?
                    """, (id,))

        con.commit()
        con.close()