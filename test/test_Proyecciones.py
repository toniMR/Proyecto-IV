# -*- coding: utf-8 -*-

import unittest
import sys, os.path

path = os.path.abspath(os.path.join(os.path.dirname(__file__),"../src"))
sys.path.append(path)

from Pelicula import Pelicula
from Proyeccion import Proyeccion

class TestPelicula(unittest.TestCase):

	def test_comprueba_creacion_pelicula(self):
		p = Pelicula ("Venom", "2:30")
		self.assertEqual(p.toString(), "Venom, 2:30")

	def test_comprueba_creacion_proyeccion(self):
		p = Pelicula ("Venom", "2:30")
		proyeccion = Proyeccion (p, 1, "14:00")
		self.assertEqual(proyeccion.toString(), "Venom, 1, 14:00-16:30")

	def test_comprueba_hora_fin(self):
		p = Pelicula ("Venom", "2:30")
		proyeccion = Proyeccion (p, 1, "14:00")
		self.assertEqual(proyeccion.getHoraFin(), '16:30')

if __name__ == '__main__':
	unittest.main()
