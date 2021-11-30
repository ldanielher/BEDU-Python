import tarjetaservicios as ts
import tarjeta as tj
from tarjetadb import TarjetaDB
import usuario as us
import os
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
    print("1. Agregar tarjeta")
    print("2. Borrar tarjeta")
    print("3. Listar tarjetas")
    print("0. Salir")
    print("-----------------------------------------")
    opcion = input("Opción: ")
    return opcion

# Inicializa varibales
miopcion = 1
database = "tarjetas.sqlite3"
tabla = "Tarjeta"
archivos_db = TarjetaDB(database)

while miopcion !="0":
    # Muestra Menu
    miopcion = imprimir_menu()

    if miopcion == "1":
        #Solicita e inserta los datos
        tarjeta1 = tj.Tarjeta()
        registros1 = list(tarjeta1.datos.values())
        archivos_db.insertar(tabla, registros1)
        print(f'Tarjeta {registros1[0]} creada!')
        time.sleep(1)
        os.system("cls")

    if miopcion == "2":
        #Solicita nombre tarjeta y la borra
        registro2 = input("Digite el nombre de tarjeta a borrar: ")
        archivos_db.borrar(tabla, registro2)
        print(f'Tarjeta {registro2} borrada!')
        time.sleep(1)
        os.system("cls")

    if miopcion == "3":
        # Imprime lista de tarjetas
        print('\nLista de tarjetas en la base de datos:')
        print('--------------------------------------------------')
        print('Nombre     Tasa(%)    Deuda     Pago Nuevos Cargos')
        print('--------------------------------------------------')
        for reg in archivos_db.listar_todo(tabla):
            print( "{:10} {:7} {:8} {:8} {:13}".format(*reg) )
        
        salir = input("\nPresione cualquier tecla para volver al menu...")
        os.system("cls")

# Cierra la conexión
archivos_db.cerrar()
# if os.path.exists(database):
#     os.remove(database)
