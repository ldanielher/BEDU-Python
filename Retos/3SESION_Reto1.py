# Define la función para sumar o multiplicar múltiples valores
def operar_números(operacion, *numeros):
	if operacion == "+":
		resultado = 0
		for num in numeros:
			resultado += num
	elif operacion == "*":
		resultado = 1
		for num in numeros:
			resultado *= num
	return resultado

# Ejemplo
print( operar_números("*", 6, 8, 10, 9) )

# Define función para ordenar alfabéticamente un directorio de personas 
def ordenar_directorio(**personas):
	lista_llaves = sorted(personas)
	for llave in lista_llaves:
		for key, value in personas.items(): 
			if llave == key:
				print(f'{key}: {value}')
	


# Ejemplo
ordenar_directorio(Fredy=3213213213, Daniel=6546546546, Cesar=9879879879, Adriana=7417417417) 