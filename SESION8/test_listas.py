import listas
import pytest

@pytest.mark.parametrize("lista, resultado",
	[
		([1,2,3,4,5], [1,2,3,4,5]),
		([1,1,1,1,1], [1]),
		([1,1,2,3,4,4,5], [1,2,3,4,5]),
		([7,2,8,1,0,4,5,5], [0,1,2,4,5,7,8])
	]
	)
def test_procesa(lista, resultado):
	""" Batería de pruebas para procesa() """
	assert type( listas.procesa([1]) ) == list
	assert listas.procesa(lista) == resultado
	