# -*- coding: utf-8 -*-

import json, os
from pymongo import MongoClient
from json import dumps
from Horas import Horas

class Cine():

    # Inicializacion
    def __init__(self):
        conn = MongoClient('localhost', 27017)
        self.db = conn.cine
        self.proyecciones = self.db.proyecciones
        self.peliculas = self.db.peliculas
        self.horas = Horas()



    # Método que devuelve los datos de la película identificada por su id
    def getPelicula (self, id):
        pelicula = ""
        pelicula = self.peliculas.find_one({'_id':id})
        return pelicula


    # Método que devuelve las películas disponibles
    def getPeliculas(self):
        peliculas = []
        pelicula = {}
        for doc in self.peliculas.find():
            pelicula['_id']= doc['_id']
            pelicula['nombre']= doc['nombre']
            pelicula['duracion']= doc['duracion']
            pelicula['precio']= doc['precio']
            peliculas.append(pelicula)
            pelicula = {}
        return(peliculas)


    # Método que inserta una nueva película
    """
        El JSON que se le pasa al POST de añadir puede ser un diccionario o un array de diccionarios
        Por eso comprobaremos si hay solo una película o varias. Esto nos permitirá usar este método
        para importar datos desde un JSON sin tener que meterlos 1 a 1.
    """
    def insertarPeliculas (self, peliculas):
        # Si peliculas es dict, es un diccionario hay uno solo (si no seria tipo list)
        array_peliculas = []
        if isinstance (peliculas, dict):
            array_peliculas.append(peliculas)
        else:
            array_peliculas = peliculas

        # Para notificar que películas se han podido insertar y cuáles no
        noInsertadas = []
        insertadas = []

        for pelicula in array_peliculas:
            _id = pelicula['_id']
            nombre = pelicula['nombre']
            precio = pelicula['precio']
            duracion = pelicula['duracion']

            # Comprobamos si existe una película que tenga ese id
            existe = self.peliculas.find_one({"_id":_id})
            if existe:
                noInsertadas.append(pelicula['_id'])
            else:
                # Se puede insertar
                self.peliculas.insert({"_id":_id, "nombre": nombre, "duracion": duracion, "precio":precio})
                insertadas.append(pelicula['_id'])

        resultado = {}
        resultado['mensaje'] = "Películas insertadas -> " + str(len(insertadas)) + ", Películas repetidas -> " + str(len(noInsertadas))
        resultado['insertadas'] = insertadas
        resultado['noInsertadas'] = noInsertadas
        return resultado


    # Método que cambia el precio de una película.
    def setPrecioPelicula (self, id, precio):
        resultado = {}
        pelicula = self.peliculas.find_one({'_id':id})
        if pelicula:
            self.peliculas.update({ '_id': id}, { "$set": {'precio':precio} })
            resultado["mensaje"] = "Precio de la película cambiado"
        else:
            resultado["mensaje"] = "No existe ningúna película con ese ID"
        return (resultado)

    # Método que elimina una película
    # En consecuencia, borrará todas las proyecciones que la proyectaran
    def borrarPelicula (self, id):
        resultado = {}
        # Comprobamos si existe la película con ese id
        existe = self.peliculas.find_one({"_id":id})
        if existe:
            # Borramos la película
            self.peliculas.delete_one({'_id':id})

            # Borramos las proyecciones que proyectarane esa película
            self.proyecciones.delete_many({'idPelicula':id})
            resultado["mensaje"] = "Película y proyecciones borradas"
        else:
            resultado["mensaje"] = "No existe ningúna película con ese ID"
        return (resultado)

    # Método que borra todas las películas
    # En consecuencia, borrará también todas las proyecciones, para que no
    # haya disponibles proyecciones que proyectan una película que no hay
    def borrarPeliculas (self):
        resultado = {}
        self.peliculas.delete_many({})
        self.proyecciones.delete_many({})
        resultado["mensaje"] = "Se han borrado todas las películas y proyecciones"
        resultado["code"] = "OK"
        return (resultado)


    # Método que devuelve todos los datos de una proyeccion identificada por su id
    def getProyeccion (self, id):
        resultado = {}
        # Comprobamos que haya una poyección con ese ID
        existe = self.proyecciones.find_one({'_id':id})
        if existe:
            resultado['_id'] = existe['_id']
            resultado['dia'] = existe['dia']
            resultado['hora'] = existe['hora']
            resultado['sala'] = existe['sala']
            idPelicula = existe['idPelicula']
            resultado['pelicula'] = self.peliculas.find_one({'_id':idPelicula})
        else:
            resultado ['mensaje'] = "No existe ninguna proyección con ese ID"
        return (resultado)


    # Método que devuelve todas las proyecciones de cada dia (datos.json)
    def getProyecciones(self):
        dias = {}
        # Mostramos los dias ordenados por _id (que es el dia)
        for i in range (1,32):
            proyecciones = self.getProyeccionesDia(i)
            if proyecciones:
                dias[i] = proyecciones
            proyecciones = {}
        return(dias)


    # Método que devuelve las proyecciones de un día
    def getProyeccionesDia (self, dia):
        proyecciones = {}
        proyeccionesDia = self.proyecciones.find({"dia":str(dia)})
        # Si hay alguna proyeccion ese dia
        if proyeccionesDia.count() > 0:
            for doc in proyeccionesDia:
                id = doc["_id"]
                dia = doc["dia"]
                hora = doc["hora"]
                sala = doc["sala"]
                idPelicula = doc["idPelicula"]
                pelicula = self.peliculas.find_one({"_id":idPelicula})
                proyeccion = {"_id":id, "dia":dia, "hora":hora, "sala":sala, "pelicula":pelicula}
                proyecciones[id] = proyeccion
        return (proyecciones)


    # Método que devuelve las proyecciones de un dia a partir de una hora
    def getProyeccionesDiaHora (self, dia, hora):
        proyeccionesDiaHora = {}
        if int(dia) > 0 and int(dia) < 32:
            hora_troceada = hora.split(':')
            proyeccionesDia = self.getProyeccionesDia(dia)
            for proyeccion in proyeccionesDia.values():
                hora_inicio_troceada = proyeccion["hora"].split(':')
                # Si la proyección comienza después de la hora indicada
                if ((hora_inicio_troceada[0] > hora_troceada[0]) or ((hora_inicio_troceada[0] == hora_troceada[0]) and (hora_inicio_troceada[1] >= hora_troceada[1]))):
                    id = proyeccion["_id"]
                    dia = proyeccion["dia"]
                    hora = proyeccion["hora"]
                    sala = proyeccion["sala"]
                    pelicula = proyeccion["pelicula"]
                    proyeccion = {"_id":id, "dia":dia, "hora":hora, "sala":sala, "pelicula":pelicula}
                    proyeccionesDiaHora[id] = proyeccion
        return (proyeccionesDiaHora)


    # Método que busca todas las proyecciones de la película nombrePelicula
    def getProyeccionesPelicula (self, idPelicula):
        proyecciones = {}
        proyeccionesPelicula = self.proyecciones.find({"idPelicula":idPelicula})
        # Si hay alguna proyeccion ese dia
        if proyeccionesPelicula.count() > 0:
            for doc in proyeccionesPelicula:
                id = doc["_id"]
                dia = doc["dia"]
                hora = doc["hora"]
                sala = doc["sala"]
                idPelicula = doc["idPelicula"]
                pelicula = self.peliculas.find_one({"_id":idPelicula})
                proyeccion = {"_id":id, "dia":dia, "hora":hora, "sala":sala, "pelicula":pelicula}
                proyecciones[id] = proyeccion
        return (proyecciones)


    # Método que busca las proyecciones de una película para un día concreto
    def getProyeccionesPeliculaDia (self, idPelicula, dia):
        proyecciones = {}
        proyeccionesPelicula = self.proyecciones.find({"idPelicula":idPelicula, "dia":dia})
        # Si hay alguna proyeccion ese dia
        if proyeccionesPelicula.count() > 0:
            for doc in proyeccionesPelicula:
                id = doc["_id"]
                dia = doc["dia"]
                hora = doc["hora"]
                sala = doc["sala"]
                idPelicula = doc["idPelicula"]
                pelicula = self.peliculas.find_one({"_id":idPelicula})
                proyeccion = {"_id":id, "dia":dia, "hora":hora, "sala":sala, "pelicula":pelicula}
                proyecciones[id] = proyeccion
        return (proyecciones)


    # Método que busca las proyecciones que hay un día en una sala concreta
    def getProyeccionesDiaSala (self, dia, sala):
        proyecciones = {}
        proyeccionesDiaSala = self.proyecciones.find({"dia":str(dia), "sala":sala})
        # Si hay alguna proyeccion ese dia
        if proyeccionesDiaSala.count() > 0:
            for doc in proyeccionesDiaSala:
                id = doc["_id"]
                dia = doc["dia"]
                hora = doc["hora"]
                sala = doc["sala"]
                idPelicula = doc["idPelicula"]
                pelicula = self.peliculas.find_one({"_id":idPelicula})
                proyeccion = {"_id":id, "dia":dia, "hora":hora, "sala":sala, "pelicula":pelicula}
                proyecciones[id] = proyeccion
        return (proyecciones)


    # Método que borra una proyección identiicada po su ID
    def borrarProyeccion (self, id):
        resultado = {}
        # Comrobamos que existe una proyeccion con ese ID
        existe = self.proyecciones.find_one({"_id":id})
        if existe:
            # La borramos
            self.proyecciones.delete_one({'_id':id})
            resultado['mensaje'] = "Proyección eliminada"
        else:
            resultado['mensaje'] = "No existe ninguna proyección con ese ID"
        return(resultado)


    # Método que borra todas las proyecciones
    def borrarProyecciones (self):
        resultado = {}
        self.proyecciones.delete_many({})
        resultado["mensaje"] = "Se han borrado todas las proyeciones correctamente"
        resultado["code"] = "OK"
        return(resultado)


    # Método que añade proyecciones
    # Admite tanto un json que sea un diccionario con los datos de la proyeccion
    # tanto un json que sea un array de diccionarios con los datos de la proyeccion
    def insertarProyecciones (self, proyecciones):
        """
            AÑADIR:
            - Si me da tiempo, comprobar que el formato de la hora sea correcto.
        """
        # Si proyecciones es dict, es un diccionario hay uno solo (si no seria tipo list)
        array_proyecciones = []
        if isinstance (proyecciones, dict):
            array_proyecciones.append(proyecciones)
        else:
            array_proyecciones = proyecciones

        # Para notificar que proyecciones se han podido insertar y cuáles no
        noInsertadas = []
        insertadas = []

        for proyeccion in array_proyecciones:
            dia = proyeccion['dia']
            hora = proyeccion['hora']
            sala = proyeccion['sala']
            idPelicula = proyeccion['idPelicula']
            id = dia + "-" + hora + "-" + sala

            error = None
            if int(dia) < 1 or int(dia) > 31:
                error = "Dia"

            # Mirar si existe la pelicula
            existePelicula = self.peliculas.find_one({"_id":idPelicula})
            if not existePelicula:
                error = "Película no disponible"

            if error == None:
                # Buscar la pelicula con nombrePelicula y mirar la duración
                duracionPeliculaInsertar = existePelicula["duracion"]

                # Si no hay proyecciones ese día se añade
                proyeccionesDia = self.proyecciones.find({'dia':dia})

                if proyeccionesDia.count() == 0:
                    self.proyecciones.insert({"_id":id, "dia":dia, "hora":hora, "sala":sala, "idPelicula":idPelicula})
                    insertadas.append(id)

                # Si ya hay proyecciones en ese dia lo añadiremos a esas proyecciones
                else:
                    # Comprobar que no choquen horas de proyecciones en el mismo dia y sala
                    algunaSolapada = False
                    for proyeccionDia in proyeccionesDia:
                        if proyeccionDia['sala'] == sala:
                            idPeli = proyeccionDia["idPelicula"]
                            pelicula = self.peliculas.find_one({"_id":idPeli})
                            solapadas = self.horas.seSolapanIntervalos (hora, duracionPeliculaInsertar, proyeccionDia['hora'], pelicula['duracion'])
                            if (solapadas):
                                algunaSolapada = True

                    if not algunaSolapada:
                        self.proyecciones.insert({"_id":id, "dia":dia, "hora":hora, "sala":sala, "idPelicula":idPelicula})
                        insertadas.append(id)
                    else:
                        noInsertadas.append(id)

            # Si hay algún error lo metemos en la parte de mal formadas
            else:
                noInsertadas.append(id)

        resultado = {}
        resultado['mensaje'] = "Proyecciones insertadas -> " + str(len(insertadas)) + ", Poyecciones no insertadas -> " + str(len(noInsertadas))
        resultado['insertadas'] = insertadas
        resultado['noInsertadas'] = noInsertadas
        return resultado

    def importarDatos (self):
        resultado = {}
        resultado['mensaje'] = "Error al importar los datos"
        try:
            if os.path.exists('../data/peliculas.json'):
                with open('../data/peliculas.json', 'r') as f:
                    peliculas = json.load(f)
            else:
                raise IOError("No se encuentra 'peliculas.json'")
                resultado['mensaje'] = "Error al buscar peliculas.json"

            if os.path.exists('../data/proyecciones.json'):
                with open('../data/proyecciones.json', 'r') as f:
                    proyecciones = json.load(f)
            else:
                raise IOError("No se encuentra 'proyecciones.json'")
                resultado['mensaje'] = "Error al buscar proyecciones.json"
            # Borramos las peliculas, este método borra también todas las proyecciones
            # ya que si no hay peliculas no es válida ninguna proyección.
            self.borrarPeliculas()

            # Primero insertamos las películas
            self.insertarPeliculas(peliculas)

            # Después las proyecciones
            self.insertarProyecciones(proyecciones)

            resultado["mensaje"] = "Datos importados correctamente"
            resultado["code"] = "OK"
        except IOError as fallo:
            print("Error {} leyendo *.json".format( fallo ) )
            resultado["code"] = "ERROR"
        return(resultado)
