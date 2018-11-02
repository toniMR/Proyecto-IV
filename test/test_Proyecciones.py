# -*- coding: utf-8 -*-

import unittest
import sys, os.path

path = os.path.abspath(os.path.join(os.path.dirname(__file__),"../src"))
sys.path.append(path)

from Pelicula import Pelicula
from Proyeccion import Proyeccion
from Cine import Cine

class TestPelicula(unittest.TestCase):

	# Comprueba que una película se ha creado correctamente
	def test_comprueba_creacion_pelicula(self):
		p = Pelicula ("Venom", "2:20")
		self.assertEqual(p.toString(), "Venom, 2:20")

	# Comprueba que una proyección se ha creado correctamente
	def test_comprueba_creacion_proyeccion(self):
		p = Pelicula ("Venom", "2:20")
		proyeccion = Proyeccion (p, 1, 7, "14:00")
		self.assertEqual(proyeccion.toString(), "Nombre: Venom, Sala: 1, Dia: 7, Hora(Inicio-Fin): 14:00-16:20")

	# Comprueba que calcula la hora en la que acaba la película correctamente
	def test_comprueba_hora_fin(self):
		p = Pelicula ("Venom", "2:20")
		proyeccion = Proyeccion (p, 1, 7, "14:00")
		self.assertEqual(proyeccion.getHoraFin(), '16:20')

	# Comprueba que esas películas son las que crea el cine
	def test_comprueba_peliculas(self):
		c = Cine()
		peliculas = []
		peliculas.append(Pelicula("Venom", "2:20"))
		peliculas.append(Pelicula("Johnny English: De nuevo en acción", "1:28"))
		peliculas.append(Pelicula("La monja", "1:36"))
		peliculas.append(Pelicula("Los Increíbles 2", "2:05"))
		peliculas.append(Pelicula("El Depredador", "1:58"))

		peliculasCine = c.getPeliculas()
		for i in range (0,len(peliculas)):
			self.assertEqual(peliculas[i].toString(), peliculasCine[i].toString())

if __name__ == '__main__':
	unittest.main()
