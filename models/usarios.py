from .db import DB
class UsuariosModel:
    def obtener_tecnicos(self):
        con = DB().connect()
        cur = con.cursor()

        cur.execute(
            "SELECT id, nombre FROM usuarios WHERE tipo = ?",
            ("Tecnico",)
        )

        res = cur.fetchall()
        con.close()
        return res

    def top_tecnicos(self):
        con = DB().connect()
        cur = con.cursor()
        cur.execute("""
                    SELECT u.id, u.nombre, COUNT(r.id) as total_rep
                    FROM usuarios u 
                             JOIN reparaciones r ON u.id = r.tecnico_id
                    GROUP BY u.id, u.nombre
                    ORDER BY total_rep DESC
                    LIMIT 5;
                    """)
        res = cur.fetchall()
        con.close()
        return res

    def autenticacion(self, usuario):
        con = DB().connect()
        cur = con.cursor()
        cur.execute('SELECT contraseña, nombre, id FROM usuarios WHERE user = ? ', (usuario,))
        cont = cur.fetchone()
        return cont

    def nuevo(self, datos):
        con = DB().connect()
        cur = con.cursor()
        cur.execute('INSERT INTO usuarios (nombre, user, sexo, email, fech_nac, contraseña, tipo) VALUES (?,?,?,?,?,?,?)',
                    datos)
        con.commit()
        con.close()