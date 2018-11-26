# -*- coding: utf-8 -*-

import json, os

class Cine():
    
    # Inicializacion
    def __init__(self):
        try:
            if os.path.exists('../data/datos.json'):
                with open('../data/datos.json', 'r') as f:
                    self.data = json.load(f)
            else:
                raise IOError("No se encuentra 'datos.json'")
        except IOError as fallo:
            print("Error {} leyendo *.json".format( fallo ) )

    # Método que devuelve todas las proyecciones de cada dia (datos.json)
    def getData(self):
        return(self.data)

    # Método que devuelve las proyecciones de un día
    def getProyeccionesDia (self, dia):
        proyecciones = []

        if dia in self.data.keys():
            proyecciones = self.data[dia]

        return (proyecciones)

    # Método que devuelve las proyecciones de un dia a partir de una hora
    def getProyeccionesDiaHora (self, dia, hora):
        proyeccionesDiaHora = []
        if dia in self.data.keys():
            hora_troceada = hora.split(':')
            for proyeccion in self.data[str(dia)]:
                hora_inicio_troceada = proyeccion['hora'].split(':')
                # Si la proyección comienza después de la hora indicada
                if ((hora_inicio_troceada[0] > hora_troceada[0]) or ((hora_inicio_troceada[0] == hora_troceada[0]) and (hora_inicio_troceada[1] >= hora_troceada[1]))):
                    proyeccionesDiaHora.append(proyeccion)
        return (proyeccionesDiaHora)

    # Método que busca todas las proyecciones de la película nombrePelicula
    def getProyeccionesPelicula (self, nombrePelicula):
        proyeccionesPelicula = []
        for proyeccionesDia in self.data.values():
            for proyeccion in proyeccionesDia:
                if (nombrePelicula.lower() in proyeccion['pelicula']['nombre'].lower()):
                    proyeccionesPelicula.append(proyeccion)
        return (proyeccionesPelicula)

    # Método que busca las proyecciones de una película para un día concreto
    def getProyeccionesPeliculaDia (self, nombrePelicula, dia):
        proyeccionesPeliculaDia = []
        if dia in self.data.keys():
            proyeccionesDia = self.data[dia]
            for proyeccion in  proyeccionesDia:
                if (nombrePelicula.lower() in proyeccion['pelicula']['nombre'].lower()):
                    proyeccionesPeliculaDia.append(proyeccion)
        return (proyeccionesPeliculaDia)
