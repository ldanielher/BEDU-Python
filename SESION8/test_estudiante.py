import estudiante

db = estudiante.EstudianteDB()
db.connect("data.json")

def test_mario():
	data = db.get_data("Mario")
	assert type(data) == dict
	assert len(data) == 3
	assert data["id"] == 1
	assert data["nombre"] == "Mario"
	assert data["resultado"] == "aprobado"
