import sqlite3

class TarjetaDB():
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
        signos: list = [ "?" for t in registros ] #lista de comprensión
        signos: str = ",".join(signos)
        sql = f"INSERT INTO {tabla} VALUES ({signos})"
        registro1 = tuple(registros)
        self.cur.execute(sql, registro1)
        self.conn.commit()
    
    def borrar(self, tabla, nombre):
        """Insertar registros en tabla"""
        sql = f'delete from {tabla} WHERE nombre = "{nombre}"'
        self.cur.execute(sql)
        self.conn.commit()

    def listar_todo(self, tabla):
        """Regresa la lista de todos los registros de la tabla"""
        sql = f"SELECT * FROM {tabla}"
        self.cur.execute(sql)
        res = self.cur.fetchall()
        return res

    def borrar_tarj_usuario(self, tabla, usuario, nombre):
        """Insertar registros en tabla"""
        sql = f'delete from {tabla} WHERE usuario = "{usuario}" and nombre = "{nombre}"'
        self.cur.execute(sql)
        self.conn.commit()

    def borrar_usuario(self, tabla, usuario):
        """Insertar registros en tabla"""
        sql = f'delete from {tabla} WHERE usuario = "{usuario}"'
        self.cur.execute(sql)
        self.conn.commit()

    def listar_todo_usuario(self, tabla, usuario):
        """Regresa la lista de todos los registros de la tabla"""
        sql = f'SELECT * FROM {tabla} WHERE usuario = "{usuario}"'
        self.cur.execute(sql)
        res = self.cur.fetchall()
        return res


