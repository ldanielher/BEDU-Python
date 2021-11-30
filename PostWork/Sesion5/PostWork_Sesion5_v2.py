import tarjetaservicios as ts
import tarjeta as tj
from tarjetadb import TarjetaDB
import tarjetadb.TarjetaDB
import usuario as us
import os.path
import time

###############################
# Desarrollo 1: Captura 1 tarjeta
# print('# Desarrollo 1: Captura 1 tarjeta de')
# tarjetaservicios1 = ts.Tarjeta_de_servicios()
# tarjetaservicios1.captura_nueva_deuda()
# tarjetaservicios1.generar_reporte()

###############################
# Desarrollo 2: Ingresar tarjetas a la BD
def imprimir_menu():
    """ Imprime menú """
    print("\nSeleccione una opción")
    print("-----------------------------------------")
    print("1. Agregar tarjeta a usuario")
    print("2. Borrar tarjeta de usuario")
    print("3. Listar tarjetas de usuario")
    print("4. Listar todas las tarjetas")
    print("0. Salir")
    print("-----------------------------------------")
    opcion = input("Opción: ")
    return opcion

# Inicializa varibales
miopcion = 1
database = "tarjetas.sqlite3"
tabla = "Usuario"
archivos_db = TarjetaDB(database)

while miopcion !="0":
    # Muestra Menu
    miopcion = imprimir_menu()

    if miopcion == "1":
        #Solicita e inserta los datos
        usuario = input("Ingrese usuario: ")
        tarjeta1 = tj.Tarjeta()
        registros1 = list(tarjeta1.datos.values())
        registros1.insert(0, usuario)
        archivos_db.insertar(tabla, registros1)
        print(f'Tarjeta {registros1[1]} creada!')
        time.sleep(1)
        os.system("cls")

    if miopcion == "2":
        #Solicita nombre tarjeta y la borra
        usuario = input("Ingrese usuario: ")
        registro2 = input("Digite el nombre de tarjeta a borrar: ")
        archivos_db.borrar_tarj_usuario(tabla, usuario, registro2)
        print(f'Tarjeta {registro2} de {usuario} borrada!')
        time.sleep(1)
        os.system("cls")

    if miopcion == "3":
        # Imprime lista de tarjetas de usuario
        usuario = input("Ingrese usuario: ")
        print(f'\nListado de tarjetas del usuario {usuario}:')
        print('--------------------------------------------------------------')
        print('Usuario   Nombre     Tasa(%)    Deuda     Pago Nuevos Cargos')
        print('--------------------------------------------------------------')
        for reg in archivos_db.listar_todo_usuario(tabla, usuario):
            print( "{:10} {:10} {:7} {:8} {:8} {:13}".format(*reg) )
        
        salir = input("\nPresione Enter para volver al menu...")
        os.system("cls")

    if miopcion == "4":
        # Imprime lista de tarjetas
        print('\nListado de tarjetas en la base de datos:')
        print('--------------------------------------------------------------')
        print('Usuario   Nombre     Tasa(%)    Deuda     Pago Nuevos Cargos')
        print('--------------------------------------------------------------')
        for reg in archivos_db.listar_todo(tabla):
            print( "{:10} {:10} {:7} {:8} {:8} {:13}".format(*reg) )

        
        salir = input("\nPresione Enter para volver al menu...")
        os.system("cls")

# database = "tarjetas.sqlite3"
# tabla = "Usuario"
# campos = (
#         "usuario VARCHAR(20)",
#         "nombre VARCHAR(20)",
#         "tasa float",
#         "deuda float",
#         "pago float",
#         "cargos float",
#         "deuda_pago float",
#         "interes_mes float",
#         "deuda_recalculada float",
#         "nueva_deuda float"
#     )
# archivos_db = TarjetaDB(database)
# archivos_db.crear_tabla(tabla, campos)    

# Cierra la conexión
archivos_db.cerrar()
# if os.path.exists(database):
#     os.remove(database)