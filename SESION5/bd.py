import os
import sqlite3

class ArchivosDB():
    def __init__(self, ruta):
        """Constructor de la clase ArchivoDB"""
        self.ruta = ruta
        self.conn = sqlite3.connect(ruta)
        self.cur = self.conn.cursor()

    def cerrar(self):
        """Cierra la conexión a la BD"""
        self.cur.close()
        self.conn.close()

    def crear_tabla(self, tabla, campos):
        """Crear tabla con campos en la BD"""
        campos_texto = ",".join(campos)
        sql = f"CREATE TABLE IF NOT EXISTS {tabla} ({campos_texto})" 
        self.cur.execute(sql)

    def insertar(self, tabla, registros):
        """Insertar registros en tabla"""
        #signos = []
        #for t in registros[0]: # -> (12345, "01-02-2021", "uno.txt")
        #    signos.append("?")
        signos: list = [ "?" for t in registros[0] ] #lista de comprensión
        signos: str = ",".join(signos)
        sql = f"INSERT INTO {tabla} VALUES ({signos})"
        for reg in registros:
            self.cur.execute(sql, reg)
            self.conn.commit()

    def listar_todo(self, tabla):
        """Regresa la lista de todos los registros de la tabla"""
        sql = f"SELECT * FROM {tabla}"
        self.cur.execute(sql)
        res = self.cur.fetchall()
        return res


def main():
    """ función principal del módulo """
    r_archivos = (
        (12345, "01-02-2021 01:02:03", "uno.txt"),
        (23456, "01-02-2021 01:02:03", "dos.txt"),
        (34567, "02-02-2021 03:02:03", "tres.py"),
        (45678, "03-02-2021 05:02:03", "cuatro.csv"),
        (4512, "10-03-2021 09:02:03", "cinco.json")
    )
    DB = "test.sqlite3"
    t_archivos = "Archivo"
    c_archivos = (
        "tamanio INTEGERT",
        "fecha VARCHAR(19)",
        "nombre VARCHAR(512)"
    )

    archivos_db = ArchivosDB(DB)
    archivos_db.crear_tabla(t_archivos, c_archivos)
    archivos_db.insertar(t_archivos, r_archivos)
    for reg in archivos_db.listar_todo(t_archivos):
        print( "{:5}  {:10}  {}".format(*reg) )
    archivos_db.cerrar()
    if os.path.exists(DB):
        os.remove(DB)


if __name__ == "__main__":
    main()