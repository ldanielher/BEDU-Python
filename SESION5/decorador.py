def decorador(funcion):
	""" Funcion que define un decorador """
	def nueva_funcion():
		print("Se ejecuta antes de la función a decorar")
		funcion()
		print("Se ejecuta después de la función a decorar")
	return nueva_funcion()

@decorador
def hola_mundo():
	""" Función a decorar """
	print("Hola desde función a decorar")
	