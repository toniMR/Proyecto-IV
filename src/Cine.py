# -*- coding: utf-8 -*-

from Proyeccion import Proyeccion
from Pelicula import Pelicula
import time
import calendar

class Cine():
    peliculas = []
    dias = []

	# Inicializacion
    def __init__(self):
        # Crear a mano una lista de Peliculas con nombres y duracion
    	self.peliculas.append(Pelicula("Venom", "2:20"))
    	self.peliculas.append(Pelicula("Johnny English: De nuevo en acción", "1:28"))
    	self.peliculas.append(Pelicula("La monja", "1:36"))
    	self.peliculas.append(Pelicula("Los Increíbles 2", "2:05"))
    	self.peliculas.append(Pelicula("El Depredador", "1:58"))

        # Ahora crearé un array donde cada casilla corresponderá a un dia del mes
    	# (Por ahora supongo que todos tienen 30 dias)
    	# En cada dia habra un array con todas las proyecciones del dia

    	# El cine estará abierto unas horas determinadas por ejemplo 8 (14:00 a 22:00)
    	# Cuando se añade una pelicula a las 14:00 y dura 2:30 ,por ejemplo, la siguiente
    	# pelicula comenzará a las 17:00. (Al comienzo de la hora siguiente)

    	for i in range (0,29):
    		proyecciones = []
    		for j in range(0,len(self.peliculas)):
    			pelicula = self.peliculas[j]
    			duracion = pelicula.getDuracion()
    			duracion_troceada = duracion.split(':')
    			horas_ocupadas_por_proyeccion = int(duracion_troceada[0])
    			if(int(duracion_troceada[1]) > 0):
    				horas_ocupadas_por_proyeccion += 1

    			hora_comienzo=12
    			while (hora_comienzo + horas_ocupadas_por_proyeccion < 22):
    				proyecciones.append(Proyeccion(pelicula, j, i, str(hora_comienzo)+':00'))
    				hora_comienzo += horas_ocupadas_por_proyeccion
    		self.dias.append(proyecciones)



    """
        	# Para cada dia
        	for i in range(0,len(self.dias)):
        		# Cada proyeccion del dia
        		print ("Dia: " + str(i+1))
        		for j in range(0,len(self.dias[i])):
        			proyeccion = self.dias[i][j]
        			pelicula = proyeccion.getPelicula()
        			print ("Proyeccion: " + proyeccion.toString())
    """

    # Método que devuelve las peliculas que hay en el Cine
    def getPeliculas (self):
        return(self.peliculas)

    # Método que devuelve todas las proyecciones
    # Devuelve un array de 30 elementos donde cada casilla tiene un array de proyecciones
    def getProyecciones (self):
        return (self.dias)

    # Método que devuelve las proyecciones de un día
    def getProyeccionesDia (self, dia):
        proyecciones = []
        if (dia <= 30 and dia > 0):
            proyecciones = self.dias[dia-1]
        return (self.dias[dia-1])

    # Método que busca todas las proyecciones de la pelicula nombrePelicula
    # PENDIENTE: Permitir busqueda parcial en vez del nombre completo de la película
    def getProyeccionesPelicula (self, nombrePelicula):
        proyeccionesPelicula = []
        for i in range (0, 30):
            for j in range (0,len(self.dias[i])):
                if (self.dias[i][j].getPelicula().getNombre() == nombrePelicula):
                    proyeccionesPelicula.append(self.dias[i][j])
        return (proyeccionesPelicula)

    # Método que devuelve las proyecciones de un dia a partir de una hora
    def getProyeccionesDiaHora (self, dia, hora):
        proyeccionesDiaHora = []
        hora_troceada = hora.split(':')
        for i in range (0,len(self.dias[dia-1])):
            hora_inicio_troceada = self.dias[dia-1][i].getHora().split(':')
            if ((hora_inicio_troceada[0] > hora_troceada[0]) or ((hora_inicio_troceada[0] == hora_troceada[0]) and (hora_inicio_troceada[1] >= hora_troceada[1]))):
                proyeccionesDiaHora.append(self.dias[dia-1][i])
        return (proyeccionesDiaHora)
