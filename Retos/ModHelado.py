# Variable global
MENU = (
(1, "Helado con oreo", 19),
(2, "Helado con m&m", 25),
(3, "Helado con fresas", 22),
(4, "Helado con brownie", 28)
)

# Funciones
def imprime_menu():
	""" Imprime la lista de topings en la salida estándar """
	print(f"{MENU[0][0]}. {MENU[0][1]}")
	print(f"{MENU[1][0]}. {MENU[1][1]}")
	print(f"{MENU[2][0]}. {MENU[2][1]}")
	print(f"{MENU[3][0]}. {MENU[3][1]}")


def lee_opcion():
	""" Lee la opción elegida por el usuario desde la entrada estándar """
	opcion: str = input("Elige una opción: ")
	opcion: int = int(opcion)
	return opcion


def imprime_precio(opcion):
	if opcion in (1, 2, 3, 4):
		print(f"El precio del helado es de ${MENU[opcion-1][2]}")
	else: 
		print("Elegiste una opción incorrecta")


