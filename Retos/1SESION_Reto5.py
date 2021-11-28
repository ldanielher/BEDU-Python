# Generar menú
menu = """
1. Helado con oreo
2. Helado con m&m
3. Helado con fresas
4. Helado con brownie
"""
print(menu)

# Solicitar escoger opción 
opcion: str = input("Elige una opción: ")
opcion: int = int(opcion)

# Extraer precio
if opcion == 1: #oreo
	precio = 19
elif opcion == 2: #m&m
	precio = 25
elif opcion == 3: #fresas
	precio = 22
elif opcion == 4: #brownie
	precio = 28
else: 			  #error
	precio = -1 

# Devolver precio
if precio == -1:
	mensaje = "Elegiste una opción incorrecta"
else:
	mensaje = f"El precio del helado es de ${precio}"

print(mensaje)