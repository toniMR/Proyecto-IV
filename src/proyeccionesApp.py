# -*- coding: utf-8 -*-
from flask import Flask, jsonify, request

from Cine import Cine

import json
import sys,os.path

app = Flask(__name__)
cine = Cine()


# Devuelve un JSON con status OK
@app.route('/', methods = ['GET'])
def index():
	return jsonify(status="OK")

# Devuelve un JSON con status OK
@app.route('/status', methods = ['GET'])
def status():
	return jsonify(status="OK")


@app.route('/peliculas', methods = ['GET', 'POST', 'DELETE'])
def peliculas():
	# Devuelve todas las películas disponibles
	if request.method == 'GET':
		return jsonify(cine.getPeliculas())

	if request.method == 'POST':
		peliculas = request.get_json()
		return jsonify (cine.insertarPeliculas(peliculas))

	if request.method == 'DELETE':
		return jsonify (cine.borrarPeliculas())


# Acciones con una película identificada por su id
@app.route('/peliculas/<id>', methods = ['GET', 'PUT', 'DELETE'])
def accionesPelicula (id):
	if request.method == 'GET':
		# Devolvemos el JSON de la película
		return jsonify(cine.getPelicula(id))

	if request.method == 'PUT':
		datos = request.get_json()
		precio = datos['precio']
		return jsonify (cine.setPrecioPelicula (id, precio))

	if request.method == 'DELETE':
		# Borramos la película y todas las proyecciones que proyectaran esa película
		return jsonify (cine.borrarPelicula (id))


# Devuelve todas las proyecciones de cada dia
@app.route('/proyecciones', methods = ['GET', 'POST', 'DELETE'])
def proyecciones():
	if request.method == 'GET':
		return jsonify(cine.getProyecciones())

	if request.method == 'POST':
		proyecciones = request.get_json()
		return jsonify (cine.insertarProyecciones(proyecciones))

	if request.method == 'DELETE':
		return jsonify (cine.borrarProyecciones())


# Acciones con una poyeccion identificada por su id
# id = Dia-Hora-Sala . Por ejemplo, 10-12:30-7
@app.route('/proyecciones/<id>', methods = ['GET', 'PUT', 'DELETE'])
def accionesProyeccion(id):
	if request.method =='GET':
		return jsonify (cine.getProyeccion(id))
	"""
	if request.method == 'PUT':
		Me acabo de dar cuenta de que tenía otra cosa aquí, cuando termine
		el despliegue haré algo como cambiar la sala o hora si me da tiempo
	"""

	if request.method == 'DELETE':
		return jsonify (cine.borrarProyeccion (id))

# Devuelve todas las proyecciones que hay el dia 'd'
@app.route('/proyecciones/dia/<d>', methods = ['GET'])
def proyeccionesDia(d):
	return jsonify (cine.getProyeccionesDia(d))

# Devuelve todas las proyecciones que hay el dia 'd' a partir de las 'h'
# La hora se tiene que poner en formato hh:mm (Ej. 10:28)
@app.route('/proyecciones/dia/<d>/hora/<h>', methods = ['GET'])
def proyeccionesDiaHora(d,h):
	return jsonify (cine.getProyeccionesDiaHora(d,h))

# Devuelve todas las proyecciones que hay con peliculas que contengan 'n' en su nombre
@app.route('/proyecciones/pelicula/<n>', methods = ['GET'])
def proyeccionesNombre(n):
	return jsonify (cine.getProyeccionesPelicula(n))

# Devuelve las proyecciones de una película para un día concreto
@app.route('/proyecciones/pelicula/<n>/dia/<d>', methods = ['GET'])
def proyeccionesPeliculaDia (n, d):
	return jsonify (cine.getProyeccionesPeliculaDia(n, d))

# Devuelve las proyecciones de un día y sala concreta
@app.route('/proyecciones/dia/<d>/sala/<s>', methods = ['GET'])
def proyeccionesDiaSala (d, s):
	return jsonify (cine.getProyeccionesDiaSala(d, s))

# Borra todas las peliculas y proyecciones que hay e importa unas
# película y proyecciones de Ejemplo
@app.route('/importarDatosEjemplo', methods = ['GET'])
def importarDatosEjemplo ():
	return jsonify (cine.importarDatos())








if __name__ == "__main__":
	app.run(host='0.0.0.0', debug=False)
