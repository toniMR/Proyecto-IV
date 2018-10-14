# -*- coding: utf-8 -*-

class Pelicula():
	nombre = ''
	duracion = ''


	# Inicializacion
	def __init__(self, n, d):
		self.nombre = n
		self.duracion = d

	def setNombre (n):
		self.nombre = n

	def setDuracion(d):
		self.duracion = d

	def getNombre (self):
		return (self.nombre)

	def getDuracion(self):
		return (self.duracion)

	def toString(self):
		return (self.nombre + ', ' + self.duracion)
