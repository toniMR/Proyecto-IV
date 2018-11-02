# -*- coding: utf-8 -*-
from flask import Flask, jsonify

from Proyeccion import Proyeccion
from Pelicula import Pelicula
from Cine import Cine
import time
import calendar

app = Flask(__name__)

@app.route('/')
def index():
	return jsonify(status="Ok")

@app.route('/peliculas')
def prueba():
	cine  = Cine()
	peliculas = []
	for p in cine.getPeliculas():
		peliculas.append(p.toString())
	return jsonify(peliculas=peliculas)



if __name__ == "__main__":
	app.run(host='0.0.0.0', debug=True)
