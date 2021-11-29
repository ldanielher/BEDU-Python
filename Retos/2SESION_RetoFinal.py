# Define una lista de números
numeros = [1, 0, 14, 25, 65, 19, 8, 3, 55, 55, 100, 64, 71 ,11 ,33, 33, 98, 42, 49, 77, 6, 100, 55]

# Define una función para procesar números
def procesar(lista):
	lista.sort()
	lista = set(lista)	
	return lista

# Almacena el resultado de la función en una variable
listado: list = list( procesar(numeros) )

#Imprime los valores uno a uno
for num in listado:
	print(num)
