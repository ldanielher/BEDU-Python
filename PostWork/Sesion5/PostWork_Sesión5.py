import tarjetaservicios as ts
import tarjeta as tj
from tarjetadb import TarjetaDB
import os

###############################
# Desarrollo 1: Captura 1 tarjeta
# tarjetaservicios1 = ts.Tarjeta_de_servicios()
# tarjetaservicios1.captura_nueva_deuda()
# tarjetaservicios1.generar_reporte()

###############################
# Desarrollo 2: Ingresar tarjetas a la BD
# Se conecta y Crea la tabla
database = "test.sqlite3"
tabla = "Tarjeta"
campos = (
        "nombre VARCHAR(20)",
        "tasa float",
        "deuda float",
        "pago float",
        "cargos float",
        "deuda_pago float",
        "interes_mes float",
        "deuda_recalculada float",
        "nueva_deuda float"
    )
archivos_db = TarjetaDB(database)
archivos_db.crear_tabla(tabla, campos)

#Inserta los datos
tarjeta1 = tj.Tarjeta()
registros1 = list(tarjeta1.datos.values())
archivos_db.insertar(tabla, registros1)

tarjeta2 = tj.Tarjeta()
registros2 = list(tarjeta2.datos.values())
archivos_db.insertar(tabla, registros2)

tarjeta3 = tj.Tarjeta()
registros3 = list(tarjeta3.datos.values())
archivos_db.insertar(tabla, registros3)

# Imprime lista de tarjetas
print('\nLista de tarjetas en la base de datos:')
print('--------------------------------------------------')
print('Nombre     Tasa(%)    Deuda     Pago Nuevos Cargos')
print('--------------------------------------------------')
for reg in archivos_db.listar_todo(tabla):
    print( "{:10} {:7} {:8} {:8} {:13}".format(*reg) )

# Cierra la conexión
archivos_db.cerrar()
if os.path.exists(database):
    os.remove(database)
