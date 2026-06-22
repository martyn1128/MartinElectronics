from .db import DB

class MasterController:

    def accesom(self):
        con = DB().connect()
        cur = con.cursor()
        cur.execute("SELECT contraseña FROM masterc ")
        mast = cur.fetchone()
        return mast