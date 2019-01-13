# -*- coding: utf-8 -*-

class Horas():

    # Método que calcula la hora final de la proyección
    def getHoraFin (self, hora, duracion):
        hora_inicio_troceada = hora.split(':')
        duracion_troceada = duracion.split(':')
        horas = (int(hora_inicio_troceada[0])) + (int(duracion_troceada[0]))
        minutos = (int(hora_inicio_troceada[1])) + (int(duracion_troceada[1]))
        if minutos > 59:
            minutos = minutos - 60
            horas = horas + 1

        if horas > 23:
            horas = horas - 24
        horaString = ""
        minString = ""

        if horas < 10:
            horaString = "0" + str(horas)
        else:
            horaString = str(horas)

        if minutos < 10:
            minString = "0" + str(minutos)
        else:
            minString = str(minutos)

        return(horaString + ":" + minString)


    # Método que calcula si se solapan 2 intervalos de tiempo
    def seSolapanIntervalos (self, hora1, duracion1, hora2, duracion2):
        """
            hora:      hora a la que comienza la proyección
            duracion:  duración de la pelicula que proyecta
        """
        # Troceamos la hora de las proyecciones
        hora1_troceada = hora1.split(':')
        hora1_fin_troceada = self.getHoraFin(hora1, duracion1).split(':')

        # Troceamos la hora de la proyección que queremos insertar
        hora2_troceada = hora2.split(':')
        hora2_fin_troceada = self.getHoraFin(hora2, duracion2).split(':')

        solapadas = False

        horas1 = int(hora1_troceada[0])
        minutos1 = int(hora1_troceada[1])
        horas1fin = int(hora1_fin_troceada[0])
        minutos1fin = int(hora1_fin_troceada[1])
        horas2 = int(hora2_troceada[0])
        minutos2 = int(hora2_troceada[1])
        horas2fin = int(hora2_fin_troceada[0])
        minutos2fin = int(hora2_fin_troceada[1])

        if ((((horas1 > horas2) or ((horas1 == horas2) and  (minutos1 >= minutos2)))
         and ((horas1 < horas2fin) or ((horas1 == horas2fin) and (minutos1 <= minutos2fin)))) or
        (((horas2 > horas1) or ((horas2 == horas1) and  (minutos2 >= minutos1)))
        and ((horas2 < horas1fin) or  ((horas2 == horas1fin) and (minutos2 <= minutos1fin))))):

            solapadas = True

        return (solapadas)
