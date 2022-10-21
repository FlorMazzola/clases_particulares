from alumno import Alumno
import datetime

class Alumnado:
    '''Representa una colección de Notas que se pueden etiquetar, modificar, y
    buscar'''

    def __init__(self, lista_de_alumnos = []):
        '''Inicializa el anotador con una lista vacía de Notas'''
        self.alumnos = lista_de_alumnos

    def nuevo_alumno (self, dni, nombre, dia_dictado, horario_dictado, instrumento):
        '''Crea una nueva nota y la agrega a la lista'''
        fecha = dia_dictado.split('/')
        dia_dictado = datetime.date(int(fecha[0]),int(fecha[1]),int(fecha[2])) 
        hora = horario_dictado.split(':')
        horario_dictado = datetime.time(int(hora[0]),int(hora[1])) 
        nuevo_alumno = Alumno(dni, nombre, dia_dictado, horario_dictado, instrumento)
        self.alumnos.append(nuevo_alumno)
        return nuevo_alumno

    def buscar(self, nombre):
        '''Busca todas las notas que coincidan con el filtro dado'''
        self.alumnos_por_nombre = []
        for alumno in self.alumnos:
            if alumno.coincide(nombre):
                self.alumnos_por_nombre.append(alumno)
        return self.alumnos_por_nombre

    def _buscar_por_dni(self, dni_alumno):
        '''Buscar la nota con el id dado'''
        for alumno in self.alumnos:
            if str(alumno.dni) == str(dni_alumno):
                return alumno
        return None

    def filtrar(self, filtro):
        '''Busca todas las notas que coincidan con el filtro dado'''
        self.alumnos_por_instrumento = []
        for instrumento in self.alumnos:
            if instrumento.coincide(filtro.lower()):
                self.alumnos_por_instrumento.append(instrumento)
        return self.alumnos_por_instrumento

    def eliminar_alumno(self, dni_alumno):
        '''Busca la nota con el id dado y la elimina'''
        alumno = self._buscar_por_dni(dni_alumno)
        if alumno:
            self.alumnos.remove(alumno)
            return True
        return False

    def modificar_alumno(self, dni_alumno, nombre, dia_dictado, horario_dictado, instrumento):
        alumno = self._buscar_por_dni(dni_alumno)
        if alumno:
            alumno.nombre = nombre
            alumno.dia_dictado = dia_dictado
            alumno.horario_dictado = horario_dictado
            alumno.instrumento = instrumento
            return True
        return False