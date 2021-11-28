from flask import Flask, render_template, request
from tree import Carpeta, genera_html

# Constantes
CARPETA_DATOS = "."

app = Flask(__name__)

@app.route("/")
def index():
	return "<h2>Página de inicio</h2>"

@app.route("/uno")
def uno():
	return render_template("pagina.html")

@app.route("/hola/<string:usuario>/")
def hola(usuario):
	""" Responde a la petición GET /hola/<usuario>/ """
	return f"<h2>Hola como estás {usuario.title()}, saludos desde Flask!</h2>"

@app.route("/archivos/", defaults={"filtro": None})
@app.route("/archivos/<string:filtro>/")
def archivos(filtro):
	""" Atiende la petición GET /archivos/ """
	carpeta = Carpeta(CARPETA_DATOS)
	elementos = carpeta.lista_elementos() # [Objetos...]
	if filtro != None:
		# lista_filtrada = []
		# for ele in elementos:
		# 	if filtro in ele.get_ruta:
		# 		lista_filtrada.append(ele)
		elementos = [ele for ele in elementos
			if filtro in ele.get_ruta or filtro in ele.fecha_str]

	return genera_html(elementos)  # [Objeto si contiene filtro, ...]

@app.route("/consultas/", methods = ['GET', 'POST'])
def consultas():
	""" Atiende la petición GET, POST /consultas/ """
	html = f"""
	<!DOCTYPE html>
	<html lang="es">
	<head>
		<meta charset="UTF-8">
	</head>
	<body>
		<h1>Consultas a realizar a la lista de archivos</h1>
		<hr />
		<form method="POST">
		  <div>
			<label>Por ruta:</label><input type="text" name="ruta" />
		  </div>
		  <div>
			<label>Por fecha:</label><input type="text" name="fecha" />
		  </div>
		  <div>
			<input type="submit" value="Buscar" />
		  </div>
		</form>
		<hr />
	</body>
	</html>
	"""
	if request.method == "POST":
		ruta = request.form["ruta"]
		fecha = request.form["fecha"]
		if ruta != "":
			carpeta = Carpeta(CARPETA_DATOS)
			elementos = carpeta.lista_elementos() # [Objetos...]
			elementos = [ele for ele in elementos
				if ruta in ele.get_ruta]

			return genera_html(elementos)  # generado como respuestas al POST
			
		if fecha != "":
			pass

	return html  # generado como respuesta al GET


if __name__ == "__main__":
	app.run(debug=True)
