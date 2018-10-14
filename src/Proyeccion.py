# -*- coding: utf-8 -*-

from Pelicula import Pelicula

class Proyeccion():
	pelicula = ''
	sala = ''
	hora = ''

	# Inicializacion
	def __init__(self, p, s, h):
		self.pelicula = p
		self.sala = s
		self.hora = h

	def setPelicula (p):
		self.pelicula = p

	def setSala (s):
		self.sala = s

	def setHora (h):
		self.hora = h

	def getPelicula (self):
		return (self.pelicula)

	def getSala (self):
		return (self.sala)

	def getHora (Self):
		return (self.hora)

	# Devuelve la hora en la que termina la proyección
	# La calcula a partir de la hora de inicio y la duración de la película.
	def getHoraFin (self):
		hora_inicio_troceada = (self.hora).split(':')
		duracion_troceada = (self.pelicula.getDuracion()).split(':')
		hora_fin = (int(hora_inicio_troceada[0])) + (int(duracion_troceada[0]))
		minutos_fin = (int(hora_inicio_troceada[1])) + (int(duracion_troceada[1]))
		return(str(hora_fin) + ':' + str(minutos_fin))

	def toString (self):
		return (self.pelicula.getNombre() + ', ' + str(self.sala) + ', ' + self.hora + '-' + self.getHoraFin())
