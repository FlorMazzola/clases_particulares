 #! /usr/bin/python3

from alumnado import Alumnado
from alumno import Alumno
import datetime

class RepositorioAlumnado:
    def __init__(self, archivo = "alumnado.txt"):
        '''Almacena los datos en un .txt'''
        self.archivo = archivo

    def obtener_todo(self):
        '''Visualiza el .txt y en caso que se encuentren datos, 
        envia los datos sobre el/los alumno/s'''
        alumnado = []
        with open(self.archivo, 'r') as datos_texto:
            for alumno_como_texto in datos_texto:
                n = self.texto_a_alumno(alumno_como_texto)
                alumnado.append(n)
        return alumnado

    def guardar_todo(self, alumnos):
        with open(self.archivo, 'w') as datos_texto:
            for alumno in alumnos:
                alumno_como_texto = self.alumno_a_texto(alumno)
                datos_texto.write(alumno_como_texto)
            print("Guardado en "+ self.archivo)

    def texto_a_alumno(self, texto):
        texto = texto[:-1] # Sacamos el \n final
        alumno_como_lista = texto.split(',')
        a = Alumno(alumno_como_lista[1], alumno_como_lista[0], alumno_como_lista[2], alumno_como_lista[3], alumno_como_lista[4])
        fecha = alumno_como_lista[2].split('-')
        a.dia_dictado = datetime.date(int(fecha[0]),int(fecha[1]),int(fecha[2])) 
        hora = alumno_como_lista[3].split('-')
        a.horario_dictado = datetime.time(int(hora[0]),int(hora[1])) 
        return a

    def alumno_a_texto(self, alumno):
        fc = alumno.dia_dictado
        fecha_en_texto = str(fc.year) + '-' + str(fc.month) + '-' + str(fc.day)
        fc = alumno.horario_dictado
        hora_en_texto = str(fc.hour) + '-' + str(fc.minute)
        return alumno.nombre + ',' + alumno.dni + ',' + fecha_en_texto + ',' + hora_en_texto + ',' + alumno.instrumento + " \n"
