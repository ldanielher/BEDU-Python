import operaciones

# Crear una función por cada elementos a probar en operaciones
def test_suma():
	""" Bateria de pruebas para la función suma() """
	assert operaciones.suma(3, 7) == 10
	assert operaciones.suma(3) == 3
	assert operaciones.suma("A", "B") == "AB"
	assert type(operaciones.suma("A", "B")) == int

def test_resta():
	""" Bateria de pruebas para la función resta() """
	assert operaciones.resta(7, 3) == 4
	assert operaciones.resta(3, 7) == -4
	assert operaciones.resta(3, 0) == 3

def test_producto():
	assert operaciones.producto(3, 7) == 21
	assert operaciones.producto(3) == 3
