# -*- coding: utf-8 -*-

import unittest, json, requests
from requests import *

url = 'https://contenedor-proyecciones.herokuapp.com/'

proyeccionesJSON = {}
with open('data/datos.json', 'r') as f:
	proyeccionesJSON = json.loads(f.read())

class TestPelicula(unittest.TestCase):

	# Comprueba que en la ruta devuelve status OK
	def test_comprueba_status_raiz(self):
		response = requests.get(url)
		self.assertEqual(response.status_code,200, "Código correcto")
		self.assertEqual(response.json()['status'], "OK", "Estado correcto en '/'")

	# Comprueba que en la ruta status devuelve status OK
	def test_comprueba_status_status(self):
		response = requests.get(url + '/status')
		self.assertEqual(response.status_code,200, "Código correcto")
		self.assertEqual(response.json()['status'], "OK", "Estado correcto en '/status'")

	# Comprueba que se haya cargado bien el json de las proyecciones
	def test_comprueba_json_proyecciones(self):
		response = requests.get(url+'/proyecciones')
		self.assertEqual(response.json(),proyeccionesJSON, "Proyecciones correctas")

if __name__ == '__main__':
	unittest.main()
