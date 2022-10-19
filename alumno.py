import datetime

#Guardamos en una variable la próxima id disponible:
dni = 0

class Alumno:
    '''Representa una nota en el anotador. Tiene etiquetas y se puede buscar'''
    def __init__(self, nombre, dni, dia_dictado, horario, instrumento):
        '''Inicializa la nota con un texto, y opcionalmente, con etiquetas 
        separadas por espacios. Automáticamente define fecha de creación e id'''
        self.nombre = nombre
        self.dia_dictado = dia_dictado
        self.dni = dni
        self.horario = horario
        self.instrumento = instrumento

    def coincide(self, instrumento):
        '''Determina si la nota coincide con el filtro de búsqueda. Retorna 
        True si es así y False de lo contrario
        
        Busca tanto en el texto como en las etiquetas y distingue mayúsculas de
        minúsculas '''

        return (instrumento in self.nombre) or (instrumento in self.instrumento)

#DIA_DICTADO -> ETIQUETA
#NOMBRE -> TEXTO
#ALUMNADO -> NOTAS
#ALUMNO -> NOTA
#ID -> DNI
