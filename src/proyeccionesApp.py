# -*- coding: utf-8 -*-
from flask import Flask, jsonify

from Cine import Cine

import json
import sys,os.path

app = Flask(__name__)
cine = Cine()

# Devuelve un JSON con status OK
@app.route('/')
def index():
	return jsonify(status="OK")

# Devuelve un JSON con status OK
@app.route('/status')
def status():
	return jsonify(status="OK")

# Devuelve todas las proyecciones de cada dia
@app.route('/proyecciones')
def data():
	return jsonify(cine.getData())

# Devuelve todas las proyecciones que hay el dia 'd'
@app.route('/proyecciones/dia/<d>')
def proyeccionesDia(d):
	return jsonify (cine.getProyeccionesDia(d))

# Devuelve todas las proyecciones que hay el dia 'd' a partir de las 'h'
# La hora se tiene que poner en formato hh:mm (Ej. 10:28)
@app.route('/proyecciones/dia/<d>/hora/<h>')
def proyeccionesDiaHora(d,h):
	return jsonify (cine.getProyeccionesDiaHora(d,h))

# Devuelve todas las proyecciones que hay con peliculas que contengan 'n' en su nombre
@app.route('/proyecciones/pelicula/<n>')
def proyeccionesNombre(n):
	return jsonify (cine.getProyeccionesPelicula(n))

# Devuelve las proyecciones de una película para un día concreto
@app.route('/proyecciones/pelicula/<n>/dia/<d>')
def proyeccionesPeliculaDia (n, d):
	return jsonify (cine.getProyeccionesPeliculaDia(n, d))


if __name__ == "__main__":
	app.run(host='0.0.0.0', debug=True)
