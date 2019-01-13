# -*- coding: utf-8 -*-

import sys, os.path

src = (os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
+ '/src/')
sys.path.append(src)

import unittest, json, requests
from requests import *
from Horas import Horas
horas = Horas()



url = 'https://proyecciones-cine.herokuapp.com/'
localhost = 'http://localhost:5000'


"""
	Los test los desarrollaré más tarde para ir desplegando en Azure, ya que
	cuando por ejemplo ejecuta al final el test de borrar_datos devuelve
	que se ha ejecuta correctamente pero al mirar la BD no se han borrado. No se
	si es porque al hacer los test hace algo para comprobarlo sin omdificar la BD

	Pero mi intención es crear una BD para realizar los test, pero de momento no se
	como hacerlo. Me voy a asegurar de realizar correctamente todo lo demás y dejaré eso
	para el final.
"""


class TestCine(unittest.TestCase):

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

	# Comprueba que importa los datos de ejemplo correctamente
	def test_importar_datos_ejemplo (self):
		response = requests.get(url + '/importarDatosEjemplo')
		self.assertEqual(response.json()['code'], "OK", "Datos de Ejemplo Importados Correctamente")

	# Comprueba que elimina todos los datos correctamente
	def test_borrar_datos (self):
		"""
			Mando petición DELETE a ruta /peliculas porque al borrar las peliculas
			también borra las proyecciones que haya al no haber peliculas que pueda proyectar
		"""
		response = requests.delete(url + '/peliculas')
		self.assertEqual(response.json()['code'], "OK", "Datos Borrados Correctamente")


class TestHoras(unittest.TestCase):

	# Comprueba que devuelve la hora en la que acaba un proyeccion correctamente
	def test_comprueba_hora_final (self):
		self.assertEqual(horas.getHoraFin("12:20", "1:45"), "14:05" , "Hora fin correcta")
		self.assertEqual(horas.getHoraFin("12:20", "01:45"), "14:05" , "Hora fin correcta")
		self.assertEqual(horas.getHoraFin("07:00", "02:45"), "09:45" , "Hora fin correcta")
		self.assertEqual(horas.getHoraFin("7:00", "02:45"), "09:45" , "Hora fin correcta")

	# Comprobar que devuelve correctamente si 2 proyecciones se solapan o no
	# Los parámetros son Hora inicio proyeccion 1, duracion1, Hora inicio proyeccion 2, duracion2
	def test_comprueba_intervalos_solapados (self):
		self.assertTrue(horas.seSolapanIntervalos("12:00", "1:45", "13:44", "02:20"), "Comprobacion Proyecciones Solapadas Correcta")
		self.assertTrue(horas.seSolapanIntervalos("13:44", "02:20", "12:00", "01:45"), "Comprobacion Proyecciones Solapadas Correcta")
		self.assertFalse(horas.seSolapanIntervalos("12:00", "1:45", "13:50", "02:20"), "Comprobacion Proyecciones Solapadas Correcta")
		self.assertFalse(horas.seSolapanIntervalos("13:50", "02:20", "12:00", "01:45"), "Comprobacion Proyecciones Solapadas Correcta")



if __name__ == '__main__':
	unittest.main()
