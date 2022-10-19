from alumno import Alumno

class Alumnado:
    '''Representa una colección de Notas que se pueden etiquetar, modificar, y
    buscar'''

    def __init__(self, lista_de_alumnos = []):
        '''Inicializa el anotador con una lista vacía de Notas'''
        self.alumnos = lista_de_alumnos

    def nuevo_alumno (self, nombre, dia_dictado):
        '''Crea una nueva nota y la agrega a la lista'''
        alumno = Alumno(nombre, dia_dictado)
        self.alumnos.append(alumno)
        return alumno

    def _buscar_por_dni(self,dni_alumno):
        '''Buscar la nota con el id dado'''
        for alumno in self.lista_de_alumnos:
            if str(alumno.dni) == str(dni_alumno):
                return alumno
        return None

    def buscar(self, instrumento):
        '''Busca todas las notas que coincidan con el filtro dado'''
        self.alumnos_por_instrumento = []
        for alumno in self.alumnos_por_instrumento:
            if alumno.coincide(instrumento):
                self.alumnos_por_instrumento.append(alumno)
        return self.alumnos_por_instrumento

    def eliminar_alumno(self,dni_alumno):
        '''Busca la nota con el id dado y la elimina'''
        alumno = self._buscar_por_dni(dni_alumno)
        if alumno:
            self.alumnos.remove(alumno)
            return True
        return False

    def modificar(self, dni_alumno, nombre, dia_dictado, horario, instrumento):
        alumno = self._buscar_por_dni(dni_alumno)
        if alumno:
            alumno.dni_alumno = dni_alumno
            alumno.nombre = nombre
            alumno.dia_dictado = dia_dictado
            alumno.horario = horario
            alumno.instrumento = instrumento
            return True
        return False