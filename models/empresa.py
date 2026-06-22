from models.db import DB


class EmpresaModel:
    def informacion(self):
        conn = DB().connect()
        cursor = conn.cursor()

        cursor.execute("""
                        SELECT * FROM empresa;
                       """)
        datos = cursor.fetchone()
        conn.close()
        return datos

    def actualiza(self, nom, dir, t1, t2, wb, em, n1, n2):
        con = DB().connect()
        cursor = con.cursor()

        cursor.execute("""
        INSERT INTO empresa (id, nombre, direccion, telefono1, telefono2, web, email, nota1, nota2)
        VALUES (?,?,?,?,?,?,?,?,?)
        ON CONFLICT (id)
        DO UPDATE SET
            nombre = excluded.nombre,
            direccion = excluded.direccion,
            telefono1 = excluded.telefono1,
            telefono2 = excluded.telefono2,
            web = excluded.web,
            email = excluded.email,
            nota1 = excluded.nota1,
            nota2 = excluded.nota2;
        """, (1, nom, dir, t1, t2, wb, em, n1, n2))
        con.commit()
        con.close()

    def actualiza_logo(self, img):
        con = DB().connect()
        cursor = con.cursor()

        cursor.execute("""
        UPDATE empresa 
        SET logo = ?
        WHERE id = ?
        """, (img, 1))
        con.commit()
        con.close()