import datetime

#Guardamos en una variable la próxima id disponible:
dni = 0

class Alumno:
    '''Representa un alumno en el alumnado. Tienen diferentes datos y se puede buscar'''
    def __init__(self, dni, nombre, dia_dictado, horario_dictado, instrumento):
        '''Inicializa la entrada con el nombre, dni, dia y horario en el que cursa.'''
        self.dni = dni
        self.nombre = nombre
        self.dia_dictado = self.convertiraFecha(dia_dictado)
        self.horario_dictado = self.convertiraHora(horario_dictado)
        self.instrumento = instrumento

    def convertiraFecha(self, dia_dictado):
        '''Transforma el str ingresado a formato fecha'''
        if type(dia_dictado)!=str:
            return dia_dictado
        x = dia_dictado.split('/')
        if len(x) == 1:
            x = dia_dictado.split('-')
        return datetime.date(int(x[0]), int(x[1]), int(x[2]))
    
    def convertiraHora(self, horario_dictado):
        '''Transforma el str ingresado a formato hora'''
        if type(horario_dictado)!=str:
            return horario_dictado
        x = horario_dictado.split(':')
        if len(x) == 1:
            x = horario_dictado.split('-')
        return datetime.time(int(x[0]), int(x[1]))

    def coincide(self, instrumento):
        '''Determina si el alumno coincide con el filtro de búsqueda. Retorna 
        True si es así y False de lo contrario'''

        return (instrumento in self.nombre) or (instrumento in self.instrumento)
