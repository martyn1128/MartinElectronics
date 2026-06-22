from .db import DB

class PagoModel:

    def query_pagos(self, f1=None, f2=None, id_tecnico=None):

        base_query = f'''
                     SELECT rep.costo AS Total, \
                            rep.servtec,
                            rep.comision, \
                            e.id      AS "ID Equipo", \
                            e.equipo, \
                            e.marca, \
                            e.modelo, \
                            e.serie, \
                            r.problema, \
                            r.estatus, \
                            c.nombre  AS "Nombre del cliente", \
                            rep.id    AS "ID Reparación", \
                            r.id      AS "ID Registro"
                     FROM equipos e
                              JOIN registros r ON r.equipo_id = e.id
                              JOIN reparaciones rep ON r.id = rep.registro_id
                              JOIN clientes c ON c.id = e.cliente_id
                     WHERE rep.tecnico_id = {id_tecnico} AND r.estatus = "Completado"
                       AND rep.ptecnico = 1 \
                     '''

        if f1 and f2:
            base_query += f" AND r.fecha_entrega BETWEEN '{f1}' AND '{f2}'"

        elif f1:
            base_query += f" AND r.fecha_entrega >= '{f1}'"

        elif f2:
            base_query += f" AND r.fecha_entrega <= '{f2}'"

        base_query += " ORDER BY r.fecha_entrega DESC"

        return base_query

    def promedio_por_mes(self, tecnico_id):
        conn = DB().connect()
        cursor = conn.cursor()

        cursor.execute("""
                        SELECT 
                            substr(fecha_reparacion, 7, 4) AS anio,
                            CAST(strftime('%m', substr(fecha_reparacion, 7, 4) || '-' || substr(fecha_reparacion, 4, 2) || '-' || substr(fecha_reparacion, 1, 2)) AS INTEGER) AS num_mes,
                            SUM((servtec * comision) / 100.0) AS total_mes
                        FROM reparaciones
                        WHERE tecnico_id = ?
                        GROUP BY anio, num_mes
                        ORDER BY anio, num_mes
                       """, (tecnico_id,))

        datos = cursor.fetchall()
        conn.close()
        return datos