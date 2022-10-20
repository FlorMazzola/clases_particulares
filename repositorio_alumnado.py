 #! /usr/bin/python3

from alumnado import Alumnado
from alumno import Alumno
import datetime

class RepositorioAlumnado:
    def __init__(self, archivo = "alumnado.txt"):
        self.archivo = archivo

    def obtener_todo(self):
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

    def alumno_a_texto(self, alumno):
        fc = alumno.fecha_inscripcion
        fecha_en_texto = str(fc.year) + '-' + str(fc.month) + '-' + str(fc.day)
        return alumno.texto + ',' + alumno.dia_dictado + ',' + fecha_en_texto + "\n"

    def texto_a_alumno(self, texto):
        texto = texto[:-1] # Sacamos el \n final
        alumno_como_lista = texto.split(',')
        a = Alumno(alumno_como_lista[1], alumno_como_lista[0], alumno_como_lista[2], alumno_como_lista[3], alumno_como_lista[4])
        fecha = alumno_como_lista[2].split('-')
        a.fecha_inscripcion = datetime.date(int(fecha[0]),int(fecha[1]),int(fecha[2])) 
        return a